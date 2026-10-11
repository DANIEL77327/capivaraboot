
import streamlit as st

st.set_page_config(
    page_title="CapivaraBot",
    page_icon="🦫",
    layout="wide"
)

# Título e apresentação
st.title("🦫 CapivaraBot")
st.subheader("🌿 Seu guia virtual da Serra da Capivara")

st.write(
    "Bem-vindo! Descubra a natureza, a história "
    "e os pontos turísticos da Serra da Capivara, no Piauí."
)

# Imagem principal
st.image(
    "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b",
    caption="Explore as belezas da natureza."
)

st.divider()

# Informações turísticas
st.header("🏞️ Conheça a região")

opcao = st.selectbox(
    "Escolha um assunto:",
    [
        "Selecione",
        "Localização",
        "Pontos turísticos",
        "Pinturas rupestres",
        "Animais da Caatinga",
        "Dicas de visitação"
    ]
)

if opcao == "Localização":
    st.write(
        "O Parque Nacional da Serra da Capivara fica "
        "no sudeste do Piauí, próximo a São Raimundo Nonato."
    )

elif opcao == "Pontos turísticos":
    st.write("Alguns atrativos conhecidos da região são:")
    st.write("- Pedra Furada")
    st.write("- Sítios arqueológicos")
    st.write("- Trilhas e paisagens da Caatinga")
    st.write("- Museu do Homem Americano")

elif opcao == "Pinturas rupestres":
    st.write(
        "São desenhos e registros feitos por povos antigos "
        "sobre superfícies rochosas. Eles ajudam a conhecer "
        "aspectos da vida humana no passado."
    )

elif opcao == "Animais da Caatinga":
    st.write(
        "A região possui uma rica biodiversidade, "
        "com aves, répteis e mamíferos adaptados ao "
        "clima semiárido."
    )

elif opcao == "Dicas de visitação":
    st.write("🎒 Recomendações para sua visita:")
    st.write("- Leve água e proteção solar.")
    st.write("- Use roupas leves e calçados adequados.")
    st.write("- Respeite a natureza e as pinturas rupestres.")
    st.write("- Consulte as regras de visitação antes da viagem.")

st.divider()

# Chatbot
st.header("💬 Converse com o CapivaraBot")

pergunta = st.text_input(
    "Digite sua pergunta sobre a Serra da Capivara:"
)

if st.button("Enviar pergunta"):
    texto = pergunta.lower()

    if "onde" in texto or "localização" in texto:
        st.info(
            "A Serra da Capivara fica no sudeste do Piauí, "
            "na região de São Raimundo Nonato."
        )

    elif "pintura" in texto:
        st.info(
            "As pinturas rupestres são registros antigos "
            "feitos em superfícies rochosas."
        )

    elif "animal" in texto or "caatinga" in texto:
        st.info(
            "A Caatinga abriga aves, répteis e mamíferos "
            "adaptados ao clima semiárido."
        )

    elif "turístico" in texto or "visitar" in texto:
        st.info(
            "Você pode conhecer sítios arqueológicos, "
            "pinturas rupestres e paisagens naturais."
        )

    elif pergunta.strip() == "":
        st.warning("Digite uma pergunta antes de enviar.")

    else:
        st.info(
            "Ainda não sei responder a essa pergunta. "
            "Experimente perguntar sobre localização, "
            "pinturas rupestres, animais ou turismo."
        )

# Rodapé
st.divider()

st.caption(
    "🦫 CapivaraBot | Projeto educativo sobre a Serra da Capivara, Piauí, "
    "desenvolvido pelo professor Daniel e pelos alunos "
    "Felype, David, Laiane e Mariana."
)
