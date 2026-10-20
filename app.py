import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="CapivaraBot - Serra da Capivara",
    page_icon="🦫",
    layout="wide"
)

# Estilização visual (CSS personalizado para cores e design mais moderno)
st.markdown("""
    <style>
    .main {
        background-color: #FAFAFA;
    }
    .stButton>button {
        background-color: #2E7D32;
        color: white;
        border-radius: 8px;
        font-weight: bold;
        border: none;
        padding: 0.5rem 1rem;
    }
    .stButton>button:hover {
        background-color: #1B5E20;
        color: white;
    }
    .css-1544g2n {
        padding-top: 2rem;
    }
    .chat-box {
        background-color: #E8F5E9;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #2E7D32;
    }
    </style>
""", unsafe_allow_html=True)

# Título e apresentação
st.title("🦫 CapivaraBot")
st.subheader("🌿 Seu guia interativo oficial da Serra da Capivara")

st.markdown(
    "Bem-vindo ao assistente virtual do **Parque Nacional da Serra da Capivara**, "
    "Patrimônio Cultural da Humanidade localizado no sudeste do Piauí. "
    "Explore a nossa rica história, arqueologia e biodiversidade!"
)

# Imagem principal (Pedra Furada)
st.image(
    "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b",
    caption="Explore as belezas e paisagens deslumbrantes da Caatinga.",
    use_container_width=True
)

st.divider()

# Informações turísticas organizadas em Abas (Tabs) para maior dinamismo
st.header("🏞️ Conheça a Região em Detalhes")

aba1, aba2, aba3, aba4, aba5 = st.tabs([
    "📍 Localização", 
    "🪨 Pontos Turísticos", 
    "🎨 Pinturas Rupestres", 
    "🐾 Fauna e Flora", 
    "🎒 Dicas de Visitação"
])

with aba1:
    st.subheader("Onde fica o Parque?")
    st.write(
        "O Parque Nacional da Serra da Capivara está localizado no estado do Piauí, "
        "abrangendo os municípios de **São Raimundo Nonato**, Canto do Buriti, Coronel José Dias e João Costa."
    )

with aba2:
    st.subheader("Principais Atrações")
    st.markdown("- **Pedra Furada:** O cartão-postal mais famoso do parque.")
    st.markdown("- **Baixão da Pedra Furada:** Complexo de sítios arqueológicos com grande concentração de pinturas.")
    st.markdown("- **Museu do Homem Americano:** Localizado em São Raimundo Nonato, abriga achados essenciais.")
    st.markdown("- **Desfiladeiro da Capivara:** Trilhas e cânions espetaculares.")

with aba3:
    st.subheader("A Arte Rupestre")
    st.write(
        "O parque abriga uma das maiores concentrações de sítios arqueológicos pré-históricos "
        "das Américas. As pinturas rupestres retratam cenas de caça, rituais, animais "
        "e o cotidiano dos antigos habitantes da região."
    )

with aba4:
    st.subheader("Biodiversidade da Caatinga")
    st.write(
        "A fauna inclui animais como o tatu-bola, veado-catingueiro, macaco-prego, "
        "onça-parda e diversas aves típicas. A flora é adaptada ao clima semiárido, "
        "com cactos, bromélias e árvores que perdem as folhas na estação seca."
    )

with aba5:
    st.subheader("Orientações para Turistas")
    st.markdown("- 💧 **Hidratação:** Leve sempre bastante água para as trilhas.")
    st.markdown("- 👟 **Calçados:** Use tênis ou botas confortáveis e aderentes.")
    st.markdown("- 🧢 **Proteção:** Não esqueça o protetor solar, óculos escuros e chapéu.")
    st.markdown("- 🧭 **Guias:** A visitação aos sítios exige o acompanhamento de um guia autorizado.")

st.divider()

# Chatbot Inteligente com mais de 30 perguntas e respostas mapeadas
st.header("💬 Converse com o CapivaraBot")
st.write("Digite sua dúvida abaixo (ex: *'Qual o melhor horário para visitar?'*, *'Onde fica a Pedra Furada?'*, *'Quem foi Niède Guidon?'*)")

# Caixa de texto para a pergunta
pergunta = st.text_input("Digite sua pergunta sobre a Serra da Capivara:")

if st.button("Enviar Pergunta 🦫"):
    texto = pergunta.lower().strip()

    if not texto:
        st.warning("⚠️ Por favor, digite uma pergunta antes de enviar.")
    else:
        # Banco de dados com mais de 30 perguntas e variações de palavras-chave
        resposta = None

        if any(w in texto for w in ["onde fica", "localização", "estado", "cidade próxima", "endereço"]):
            resposta = "📍 O Parque fica no sudeste do Piauí, tendo como principais cidades de apoio São Raimundo Nonato, Coronel José Dias e João Costa."
        
        elif any(w in texto for w in ["pedra furada", "cartão postal", "monumento"]):
            resposta = "🪨 A Pedra Furada é o principal cartão-postal do parque, uma imensa formação rochosa arenítica com um grande furo central esculpido pela natureza."

        elif any(w in texto for w in ["niède guidon", "criadora", "fundadora", "arqueóloga"]):
            resposta = "👩‍🔬 Niède Guidon foi a arqueóloga franco-brasileira fundamental para a criação do parque e para a preservação e estudo de seus tesouros históricos."

        elif any(w in texto for w in ["patrimônio", "unesco", "título"]):
            resposta = "🏆 Sim! O Parque Nacional da Serra da Capivara foi declarado Patrimônio Cultural da Humanidade pela UNESCO em 1991."

        elif any(w in texto for w in ["museu do homem americano", "museu", "fumdham"]):
            resposta = "🏛️ O Museu do Homem Americano, gerido pela FUMDHAM em São Raimundo Nonato, exibe fósseis, ossadas e peças arqueológicas incríveis encontradas no parque."

        elif any(w in texto for w in ["pinturas rupestres", "desenhos", "arte rupestre", "o que são"]):
            resposta = "🎨 As pinturas rupestres são registros milenares feitos pelos primeiros grupos humanos nas paredes de rocha, retratando rituais, caçadas e a fauna da época."

        elif any(w in texto for w in ["idade", "anos", "antiguidade", "quanto tempo"]):
            resposta = "⏳ Algumas pesquisas indicam vestígios da presença humana na região que datam de dezenas de milhares de anos atrás."

        elif any(w in texto for w in ["clima", "temperatura", "calor", "seca"]):
            resposta = "☀️ O clima é semiárido, caracterizado por altas temperaturas durante a maior parte do ano e uma estação seca marcante."

        elif any(w in texto for w in ["melhor época", "quando ir", "meses", "época do ano"]):
            resposta = "📅 A melhor época para visitar é durante a estação mais amena ou seca (entre maio e dezembro), quando as chuvas são escassas e o acesso às trilhas fica facilitado."

        elif any(w in texto for w in ["guia", "precisa de guia", "acompanhamento"]):
            resposta = "🧭 Sim, a visitação aos sítios arqueológicos e trilhas do parque obrigatoriamente requer a contratação e o acompanhamento de um guia de turismo credenciado."

        elif any(w in texto for w in ["ingresso", "entrada", "pagar", "valor"]):
            resposta = "🎟️ Há uma taxa de entrada para o parque, e os ingressos podem ser adquiridos nas portarias ou antecipadamente pelos canais oficiais de turismo."

        elif any(w in texto for w in ["aeroporto", "chegar de avião", "voos"]):
            resposta = "✈️ A região conta com o Aeroporto Internacional Serra da Capivara, localizado em São Raimundo Nonato, que recebe voos em períodos específicos."

        elif any(w in texto for w in ["carro", "chegar de carro", "distância de Teresina"]):
            resposta = "🚗 Partindo de Teresina (capital do Piauí), a viagem de carro até São Raimundo Nonato dura cerca de 6 a 7 horas pela rodovia BR-302 / PI-140."

        elif any(w in texto for w in ["hospedagem", "onde ficar", "hotel", "pousada"]):
            resposta = "🏨 As cidades de São Raimundo Nonato e Coronel José Dias oferecem ótimas opções de hotéis, pousadas e restaurantes para os turistas."

        elif any(w in texto for w in ["animais", "fauna", "bichos", "fauna da caatinga"]):
            resposta = "🐾 A fauna da região conta com tatu-bola, veado-catingueiro, macaco-prego, jaguatirica, gaviões e várias outras espécies adaptadas à Caatinga."

        elif any(w in texto for w in ["plantas", "flora", "árvores", "vegetação"]):
            resposta = "🌵 A vegetação é típica da Caatinga, com árvores de médio porte, cactus (como o mandacaru e o xique-xique), bromélias e arbustos resistentes à seca."

        elif any(w in texto for w in ["tatu-bola", "mascote"]):
            resposta = "🦡 O tatu-bola é um dos animais mirabolantes da região e inclusive serviu de inspiração para o mascote da Copa do Mundo de 2014 (o Fuleco)."

        elif any(w in texto for w in ["trilhas", "caminhada", "trekking"]):
            resposta = "🥾 Existem diversas trilhas ecológicas sinalizadas e de diferentes níveis de dificuldade, todas guiadas por profissionais locais."

        elif any(w in texto for w in ["acessibilidade", "cadeirante", "mobilidade"]):
            resposta = "♿ Algumas áreas e passarelas do parque possuem adaptações para facilitar o acesso de pessoas com mobilidade reduzida, embora muitas trilhas exijam caminhada em terreno irregular."

        elif any(w in texto for w in ["segurança", "perigoso", "risco"]):
            resposta = "🛡️ O parque é seguro para os visitantes, desde que sigam as orientações dos guias, utilizem calçados adequados e evitem se afastar das trilhas demarcadas."

        elif any(w in texto for w in ["comida", "gastronomia", "o que comer", "culinária"]):
            resposta = "🍲 Na região de São Raimundo Nonato você poderá saborear pratos típicos nordestinos, como carne de sol, galinha capoeira, paçoca de carne e doces caseiros."

        elif any(w in texto for w in ["souvenirs", "artesanato", "lembranças", "comprar"]):
            resposta = "🧶 O artesanato local produzido por cooperativas da região (incluindo peças de cerâmica inspiradas nas pinturas rupestres) é excelente para levar de lembrança."

        elif any(w in texto for w in ["quantos sítios", "número de sítios", "quantidade de sítios"]):
            resposta = "📊 O Parque Nacional possui catalogados mais de mil sítios arqueológicos, sendo que centenas deles estão abertos à visitação pública."

        elif any(w in texto for w in ["origem do nome", "por que se chama", "capivara"]):
            resposta = "🏷️ O nome 'Serra da Capivara' é uma denominação geográfica tradicional da região, associada a acidentes geográficos locais, embora o parque seja mundialmente famoso por seus vestígios pré-históricos."

        elif any(w in TEXTO_LOWER := [texto] if False else texto, "horário" in texto or "funciona" in texto or "abertura" in texto):
            resposta = "⏰ O parque geralmente fica aberto diariamente para visitação pública em horário diurno, mas os horários específicos de portarias e museus devem ser confirmados com antecedência."

        elif any(w in texto for w in ["chuva", "chuvosa", "inverno"]):
            resposta = "🌧️ A estação chuvosa costuma ocorrer entre os meses de dezembro e abril. Nesse período, a Caatinga floresce e fica totalmente verde!"

        elif any(w in texto for w in ["fotografia", "fotos", "drone", "filmar"]):
            resposta = "📷 Fotografias são permitidas e o cenário é espetacular! O uso de drones, no entanto, requer autorização prévia das autoridades ambientais do parque."

        elif any(w in texto for w in ["escola", "projeto", "educativo", "alunos", "professor daniel"]):
            resposta = "🎓 Este projeto foi desenvolvido de forma educativa pelo professor Daniel junto aos alunos Felype, David, Laiane e Mariana!"

        elif any(w in texto for w in ["olá", "oi", "bom dia", "boa tarde", "boa noite"]):
            resposta = "👋 Olá! Seja muito bem-vindo ao CapivaraBot. Como posso ajudar você a conhecer mais sobre a Serra da Capivara hoje?"

        elif any(w in texto for w in ["obrigado", "valeu", "grato", "agradeço"]):
            resposta = "😊 Por nada! Se precisar de mais informações sobre a Serra da Capivara, é só perguntar. Boa viagem!"

        else:
            resposta = (
                "🤔 Desculpe, ainda não tenho informações específicas sobre isso. "
                "Como sou um assistente exclusivo da **Serra da Capivara**, tente me perguntar "
                "sobre a **Pedra Furada, localização, pinturas rupestres, Niède Guidon, fauna da Caatinga, "
                "dicas de visitação ou hotéis**!"
            )

        # Exibe a resposta formatada dentro de uma caixa estilizada
        st.markdown(f'<div class="chat-box"><b>CapivaraBot:</b><br>{resposta}</div>', unsafe_allow_html=True)

# Rodapé institucional
st.divider()
st.caption(
    "🦫 CapivaraBot | Projeto educativo dedicado ao Parque Nacional da Serra da Capivara, Piauí, "
    "desenvolvido pelo professor Daniel e pelos alunos Felype, David, Laiane e Mariana."
)
