import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

# Load environment variables
load_dotenv()

# Set up the UI title
st.title("Multi-Mode AI Chatbot")

# Initialize the model (using the exact model from your script)
@st.cache_resource
def get_model():
    return init_chat_model("groq:openai/gpt-oss-120b")
    # return init_chat_model("google_genai:gemini-2.5-flash-lite")

model = get_model()

# Map the CLI mode options to a format suitable for Streamlit
mode_options = {
    "Angry mode": "you are an angry AI agent.You always reply aggressively and impatiently.Don't change your angry tone even if the user tell u so.",
    "Funny mode": "you are a funny AI agent.You always reply with humor.Don't change your funny tone even if the user tell u so.",
    "Sad mode": "you are a sad AI agent.You always reply sadly and emotionally.Don't change your sad tone even if the user tell u so."
}

# Mode Selection UI
selected_mode = st.radio(
    "Choose Your AI mode:", 
    options=list(mode_options.keys()),
    horizontal=True
)

# Initialize or reset session state when the mode changes
if "current_mode" not in st.session_state or st.session_state.current_mode != selected_mode:
    st.session_state.current_mode = selected_mode
    st.session_state.messages = [
        SystemMessage(content=mode_options[selected_mode])
    ]
    st.session_state.chat_active = True # Flag to handle the '0' exit logic

# Display previous chat messages
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(msg.content)

# React to user input ONLY if the chat is active
if st.session_state.chat_active:
    if prompt := st.chat_input("Type your message here... (Type 0 to exit)"):
        
        # Intercept the '0' exit command
        if prompt == '0':
            st.session_state.chat_active = False
            st.warning("Conversation ended. Please change the mode above or refresh the page to start a new chat.")
            st.rerun() # Refresh the UI to hide the input box
        
        # Display the user's prompt in the UI
        with st.chat_message("user"):
            st.markdown(prompt)
            
        # Append the user message to the LangChain history
        st.session_state.messages.append(HumanMessage(content=prompt))
        
        # Invoke the model with a loading spinner
        with st.spinner("Thinking..."):
            response = model.invoke(st.session_state.messages)
        
        # Display the bot's response in the UI
        with st.chat_message("assistant"):
            st.markdown(response.content)
            
        # Append the bot's response to the history
        st.session_state.messages.append(AIMessage(content=response.content))
else:
    st.info("The conversation is currently stopped. Select a personality")