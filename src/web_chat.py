import streamlit as st
from openai import OpenAI

st.title("Meu ChatGPT Local (Privado & Offline)")
st.caption("Rodando com Qwen via LM Studio & OpenAI SDK")

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Olá! Como posso te ajudar hoje?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("Digite sua mensagem..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    response = client.chat.completions.create(
        model="qwen-local-model",
        messages=st.session_state.messages
    )
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)