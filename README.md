# Multi-Mode-AI-Chatbot-
An interactive web application built with Streamlit and LangChain that showcases dynamic AI personality shifting. The chatbot can pivot between distinct behavioral modes instantly using a uniform message history interface.

## What It Does    
Dynamic Persona Injection: Implements persona constraints via LangChain's native SystemMessage mapping. Users can toggle between Angry, Funny, or Sad modes dynamically through a clean horizontal radio UI layout.  

Stateful Personality Switching: Actively monitors selection changes using st.session_state. When a user toggles to a new mode, the application automatically clears the existing thread history and swaps the underlying SystemMessage system prompt block without requiring an app restart.  

Unified Message Stream: Feeds a sequence list of SystemMessage, HumanMessage, and AIMessage directly to the language model. This retains context within active loops while strictly sticking to the assigned character behaviors.  

Graceful Exit Controls: Retains CLI-inspired terminal features by intercepting a 0 escape string in the text bar. Sending 0 locks out the message generation frame and sets chat_active to False until a user initiates a fresh configuration or radio flip.  

Optimized Model Resource Caching: Wraps initialization handlers inside a @st.cache_resource decorator to avoid re-instantiating connection nodes or resetting configuration tunnels during recurring script executions.  


### Local Setup
1. Clone the Repository
git clone https://github.com/Adrita03/multi-mode-chatbot.git  
cd multi-mode-chatbot  
2. Set Up a Virtual Environment & Install Dependencies

python -m venv .venv  
 .venv\Scripts\activate  
pip install -r requirements.txt  
3. Configure Environment Variable
   
Create a .env file in your root folder and supply the respective engine tokens required by init_chat_model:  


Code snippet  

GROQ_API_KEY=your_groq_key_here  
4. Run the App  

streamlit run app.py  
