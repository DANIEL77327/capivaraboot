
import streamlit as st

st.set_page_config(
    page_title="CapivaraBot",
    page_icon="🦕"
)

st.title("🦕 CapivaraBot")
st.subheader("Assistente da Serra da Capivara")
st.write("Olá! Pergunte sobre turismo, pinturas rupestres e a Serra da Capivara.")

def responder(pergunta):
    pergunta = pergunta.lower()

    if "oi" in pergunta or "olá" in pergunta:
        return "Olá! 😊 Seja bem-vindo ao CapivaraBot!"

    elif "serra" in pergunta:
        return "A Serra da Capivara fica no sudeste do Piauí e possui importantes sítios arqueológicos."

    elif "pinturas" in pergunta:
        return "As pinturas rupestres são registros feitos nas rochas por povos antigos."

    elif "turismo" in pergunta:
        return "A região oferece trilhas, sítios arqueológicos e paisagens incríveis."

    elif "onde fica" in pergunta:
        return "O Parque Nacional da Serra da Capivara fica no estado do Piauí, no Brasil."

    else:
        return "Ainda não sei responder a isso. Tente perguntar sobre a Serra da Capivara!"

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

for mensagem in st.session_state.mensagens:
    with st.chat_message(mensagem["role"]):
        st.write(mensagem["content"])

pergunta = st.chat_input("Digite sua pergunta...")

if pergunta:
    st.session_state.mensagens.append(
        {"role": "user", "content": pergunta}
    )

    with st.chat_message("user"):
        st.write(pergunta)

    resposta = responder(pergunta)

    st.session_state.mensagens.append(
        {"role": "assistant", "content": resposta}
    )

    with st.chat_message("assistant"):
        st.write(resposta)

