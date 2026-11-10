
import streamlit as st
import unicodedata
import re

# =====================================================
# CONFIGURAÇÃO
# =====================================================

st.set_page_config(
    page_title="CapivaraBot | Serra da Capivara",
    page_icon="🐾",
    layout="wide"
)

# =====================================================
# IMAGENS
# =====================================================

IMAGENS = [
    {
        "url": "https://www.viajenaviagem.com/wp-content/uploads/2013/11/parque-abreinterno.jpg.webp",
        "legenda": "Paisagens e formações rochosas da Serra da Capivara."
    },
    {
        "url": "https://www.maladeaventuras.com/wp-content/uploads/2023/01/parque-serra-da-capivara.jpg",
        "legenda": "Belezas naturais do Parque Nacional da Serra da Capivara."
    }
]

# =====================================================
# ESTILO DO SITE
# =====================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

.stApp {
    background-color: #f7f5ef;
    font-family: 'DM Sans', sans-serif;
}

header[data-testid="stHeader"] {
    background-color: transparent;
}

h1, h2, h3 {
    color: #263d2c;
}

.hero {
    background: linear-gradient(120deg, #263d2c, #526b45);
    padding: 42px;
    border-radius: 20px;
    color: white;
    margin-bottom: 25px;
}

.hero h1 {
    color: white;
    font-family: 'Playfair Display', serif;
    font-size: 44px;
}

.hero p {
    color: #edf2e9;
    font-size: 17px;
    line-height: 1.7;
}

.tag {
    display: inline-block;
    background: #e8eee3;
    color: #344c35;
    padding: 7px 13px;
    border-radius: 30px;
    font-size: 13px;
    font-weight: 700;
    margin-bottom: 12px;
}

.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 29px;
    color: #263d2c;
    margin-top: 25px;
}

.info-card {
    background: white;
    padding: 22px;
    border-radius: 15px;
    border: 1px solid #e4e1d8;
    min-height: 135px;
}

.info-card h3 {
    font-size: 19px;
}

.info-card p {
    color: #555b52;
    line-height: 1.6;
}

div[data-testid="stChatMessage"] {
    background-color: white;
    border: 1px solid #e7e4dc;
    border-radius: 15px;
    padding: 13px;
    margin-bottom: 12px;
}

.stButton > button {
    background-color: #526b45;
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: 600;
}

.stButton > button:hover {
    background-color: #263d2c;
    color: white;
    border: none;
}

div[data-testid="stChatInput"] {
    border-color: #526b45;
}

hr {
    border-color: #deded3;
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# NORMALIZAÇÃO DO TEXTO
# =====================================================

def normalizar(texto):
    texto = texto.lower().strip()

    texto = unicodedata.normalize("NFD", texto)

    texto = "".join(
        c for c in texto
        if unicodedata.category(c) != "Mn"
    )

    texto = re.sub(r"[^a-z0-9\s]", " ", texto)
    texto = re.sub(r"\s+", " ", texto)

    return texto


# =====================================================
# BANCO DE CONHECIMENTO DO CHATBOT
# =====================================================

BANCO_RESPOSTAS = [

    {
        "palavras": [
            "serra da capivara",
            "o que e a serra",
            "sobre o parque"
        ],
        "resposta": (
            "A Serra da Capivara é uma região localizada no sudeste "
            "do Piauí, conhecida por suas paisagens naturais, "
            "formações rochosas e importantes sítios arqueológicos. "
            "O Parque Nacional da Serra da Capivara é um grande "
            "patrimônio histórico e cultural do Brasil."
        )
    },

    {
        "palavras": [
            "onde fica",
            "localizacao",
            "qual cidade",
            "onde esta localizado"
        ],
        "resposta": (
            "O Parque Nacional da Serra da Capivara fica no sudeste "
            "do estado do Piauí. Sua área envolve municípios como "
            "São Raimundo Nonato, Coronel José Dias, João Costa "
            "e Canto do Buriti."
        )
    },

    {
        "palavras": [
            "importancia",
            "por que e importante",
            "patrimonio",
            "unesco"
        ],
        "resposta": (
            "A Serra da Capivara é importante por preservar um "
            "conjunto significativo de sítios arqueológicos e "
            "pinturas rupestres. Em 1991, o parque foi reconhecido "
            "como Patrimônio Mundial pela UNESCO."
        )
    },

    {
        "palavras": [
            "pinturas rupestres",
            "desenhos nas pedras",
            "arte rupestre",
            "pinturas antigas"
        ],
        "resposta": (
            "Pinturas rupestres são registros feitos por grupos "
            "humanos antigos em paredes de rochas. Elas apresentam "
            "figuras de pessoas, animais, cenas de caça, danças "
            "e outras atividades que ajudam a compreender o passado."
        )
    },

    {
        "palavras": [
            "pontos turisticos",
            "lugares para visitar",
            "atracoes",
            "o que visitar",
            "pedra furada"
        ],
        "resposta": (
            "Entre os lugares conhecidos estão a Pedra Furada, "
            "o Baixão das Mulheres, o Museu do Homem Americano "
            "e o Museu da Natureza."
        )
    },

    {
        "palavras": [
            "animais",
            "fauna",
            "bichos",
            "animais da caatinga"
        ],
        "resposta": (
            "A região abriga animais adaptados ao clima da Caatinga, "
            "como tatu-bola, veado-catingueiro, macaco-prego, "
            "aves e outros animais silvestres."
        )
    },

    {
        "palavras": [
            "plantas",
            "flora",
            "vegetacao",
            "mandacaru",
            "xique xique"
        ],
        "resposta": (
            "A vegetação é característica da Caatinga. Entre as "
            "plantas encontradas na região estão o mandacaru, "
            "o xique-xique e diversas espécies de bromélias."
        )
    },

    {
        "palavras": [
            "como visitar",
            "dicas de visita",
            "o que levar",
            "visitar o parque"
        ],
        "resposta": (
            "Para uma visita, é importante usar roupas confortáveis, "
            "calçados adequados para caminhada, levar água, protetor "
            "solar e chapéu ou boné. Consulte as orientações "
            "atualizadas antes de organizar seu passeio."
        )
    },

    {
        "palavras": [
            "comida tipica",
            "culinaria",
            "comidas",
            "gastronomia"
        ],
        "resposta": (
            "A culinária regional apresenta pratos como carne de sol, "
            "galinha caipira, paçoca e preparações com ingredientes "
            "característicos do sertão piauiense."
        )
    },

    {
        "palavras": [
            "museu do homem americano",
            "museu",
            "acervo"
        ],
        "resposta": (
            "O Museu do Homem Americano, localizado em São Raimundo "
            "Nonato, apresenta informações e materiais relacionados "
            "à arqueologia da região e à história da presença humana "
            "nas Américas."
        )
    },

    {
        "palavras": [
            "caatinga",
            "bioma",
            "clima da regiao"
        ],
        "resposta": (
            "A Caatinga é um bioma brasileiro predominante em áreas "
            "do Nordeste. Possui vegetação adaptada a períodos de "
            "pouca chuva, com plantas como cactos e arbustos resistentes."
        )
    },

    {
        "palavras": [
            "preservar",
            "preservacao",
            "conservar",
            "proteger o parque"
        ],
        "resposta": (
            "Você pode ajudar respeitando as trilhas e as orientações "
            "dos guias, não deixando lixo, não retirando elementos "
            "naturais e não tocando nas pinturas rupestres. "
            "Preservar o parque é proteger a história e a natureza."
        )
    }

]


# =====================================================
# SISTEMA DE RESPOSTAS
# =====================================================

def responder(pergunta):

    texto = normalizar(pergunta)

    if not texto:
        return "Digite uma pergunta para que eu possa ajudar!"

    palavras_pergunta = set(texto.split())

    melhor_resposta = None
    maior_pontuacao = 0

    for item in BANCO_RESPOSTAS:

        pontuacao = 0

        for termo in item["palavras"]:

            termo = normalizar(termo)

            if termo in texto:
                pontuacao += len(termo.split()) + 2
            else:
                palavras_termo = set(termo.split())
                pontuacao += len(
                    palavras_pergunta.intersection(palavras_termo)
                )

        if pontuacao > maior_pontuacao:
            maior_pontuacao = pontuacao
            melhor_resposta = item["resposta"]

    if melhor_resposta and maior_pontuacao >= 1:
        return melhor_resposta

    return (
        "Ainda não encontrei uma resposta específica para essa "
        "pergunta. Tente perguntar sobre a localização, as pinturas "
        "rupestres, os pontos turísticos, a fauna, a flora ou "
        "a preservação do parque."
    )


# =====================================================
# HISTÓRICO DO CHAT
# =====================================================

if "mensagens" not in st.session_state:

    st.session_state.mensagens = [
        {
            "role": "assistant",
            "content": (
                "Olá! Eu sou o CapivaraBot! 🐾 "
                "Estou aqui para apresentar a Serra da Capivara, "
                "sua história, cultura e belezas naturais. "
                "Pode escrever sua pergunta no campo abaixo!"
            )
        }
    ]


def enviar_pergunta(pergunta):

    st.session_state.mensagens.append({
        "role": "user",
        "content": pergunta
    })

    resposta = responder(pergunta)

    st.session_state.mensagens.append({
        "role": "assistant",
        "content": resposta
    })


# =====================================================
# CABEÇALHO
# =====================================================

st.markdown("""
<div class="hero">

    <div class="tag">TURISMO • HISTÓRIA • CULTURA</div>

    <h1>🐾 CapivaraBot</h1>

    <p>
        Seu guia virtual pela Serra da Capivara.
        Descubra a história, a natureza e as riquezas culturais
        de um dos maiores patrimônios do Piauí.
    </p>

</div>
""", unsafe_allow_html=True)


# =====================================================
# GALERIA DE IMAGENS
# =====================================================

st.markdown(
    '<div class="section-title">Conheça a Serra da Capivara</div>',
    unsafe_allow_html=True
)

st.write(
    "Explore as paisagens e as formações rochosas do Parque "
    "Nacional da Serra da Capivara."
)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.image(
        IMAGENS[0]["url"],
        use_container_width=True,
        caption=IMAGENS[0]["legenda"]
    )

with col2:
    st.image(
        IMAGENS[1]["url"],
        use_container_width=True,
        caption=IMAGENS[1]["legenda"]
    )

st.caption("Imagens: Viaje na Viagem e Mala de Aventuras.")

st.divider()


# =====================================================
# APRESENTAÇÃO
# =====================================================

st.markdown(
    '<div class="section-title">Um patrimônio do Piauí</div>',
    unsafe_allow_html=True
)

st.write(
    "Localizada no sudeste do Piauí, a Serra da Capivara reúne "
    "paisagens impressionantes, formações rochosas, sítios "
    "arqueológicos e registros de antigas sociedades humanas. "
    "É um lugar que conecta natureza, ciência, memória e cultura."
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="info-card">
        <h3>🪨 História</h3>
        <p>
            Registros arqueológicos e pinturas rupestres que ajudam
            a compreender a vida de grupos humanos antigos.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <h3>🌵 Natureza</h3>
        <p>
            Paisagens da Caatinga, vegetação adaptada ao clima
            e diversidade de animais silvestres.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="info-card">
        <h3>🏛️ Cultura</h3>
        <p>
            Um patrimônio que valoriza a memória, a pesquisa
            e a identidade cultural do Piauí.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.divider()


# =====================================================
# CHATBOT: CAMPO DE PERGUNTAS E RESPOSTAS
# =====================================================

st.markdown(
    '<div class="section-title">💬 Converse com o CapivaraBot</div>',
    unsafe_allow_html=True
)

st.write(
    "Tem curiosidade sobre a Serra da Capivara? "
    "Digite sua pergunta no campo abaixo. O CapivaraBot "
    "vai apresentar a resposta aqui na conversa."
)

# Exibir histórico da conversa
for mensagem in st.session_state.mensagens:

    with st.chat_message(mensagem["role"]):
        st.markdown(mensagem["content"])

# Campo único para inserir perguntas
pergunta = st.chat_input(
    "Digite sua pergunta sobre a Serra da Capivara..."
)

if pergunta:

    enviar_pergunta(pergunta)
    st.rerun()


# Botão para limpar o histórico
if st.button("Limpar conversa"):
    st.session_state.mensagens = [
        {
            "role": "assistant",
            "content": (
                "Olá novamente! Sou o CapivaraBot. "
                "Pode enviar sua pergunta!"
            )
        }
    ]
    st.rerun()


# =====================================================
# RODAPÉ
# =====================================================

st.divider()

st.markdown("""
<div style="
    background-color: #e9ede4;
    padding: 25px;
    border-radius: 15px;
    text-align: center;
">

    <h3 style="color: #263d2c;">🐾 CapivaraBot</h3>

    <p style="color: #465344;">
        Conhecimento, tecnologia e valorização do patrimônio piauiense.
    </p>

    <p style="color: #687365; font-size: 13px;">
        Projeto desenvolvido pelo Professor Daniel e pelos alunos
        Felype, David, Laiane e Mariana.
    </p>

    <p style="color: #687365; font-size: 12px;">
        Projeto educativo de turismo e divulgação cultural.
    </p>

</div>
""", unsafe_allow_html=True)
