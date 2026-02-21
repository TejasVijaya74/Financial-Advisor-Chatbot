import streamlit as st
from app.services.gemini_service import generate_response
from app.services.memory_service import MemoryService
from app.prompts.financial_prompt import SYSTEM_PROMPT

st.title("Financial Advisor Chatbot")

if "memory" not in st.session_state:
    st.session_state.memory = MemoryService()

user_input = st.chat_input("Ask your financial question...")

if user_input:
    memory = st.session_state.memory
    memory.add_user_message(user_input)

    context = memory.get_context()

    prompt = SYSTEM_PROMPT + "\n" + context

    response = generate_response(prompt)

    memory.add_bot_message(response)

    st.chat_message("user").write(user_input)
    st.chat_message("assistant").write(response)