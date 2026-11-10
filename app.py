
import streamlit as st
import unicodedata
import re

# ============================================================
# 1. CONFIGURAÇÃO GERAL
# ============================================================

st.set_page_config(
    page_title="CapivaraBot | Guia Turístico",
    page_icon="🐾",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# 2. IMAGENS DO PROJETO
# ============================================================

IMAGENS = [
    {
        "url": "https://www.viajenaviagem.com/wp-content/uploads/2013/11/parque-abreinterno.jpg.webp",
        "legenda": "Formações rochosas e paisagens da Serra da Capivara."
    },
    {
        "url": "https://www.maladeaventuras.com/wp-content/uploads/2023/01/parque-serra-da-capivara.jpg",
        "legenda": "A beleza natural do Parque Nacional da Serra da Capivara."
    }
]

# ============================================================
# 3. IDENTIDADE DO CHATBOT
# ============================================================

NOME_PROJETO = "CapivaraBot"
SUBTITULO = "Seu guia virtual pela Serra da Capivara"

DESCRICAO = (
    "Uma experiência interativa para conhecer a história, "
    "a arqueologia, a natureza e a riqueza cultural do Piauí."
)

# ============================================================
# 4. BANCO DE CONHECIMENTO
# ============================================================

BANCO_RESPOSTAS = [
    {
        "palavras": [
            "o que e a serra da capivara",
            "serra da capivara",
            "sobre o parque",
            "fale sobre a serra"
        ],
        "resposta": (
            "A Serra da Capivara é uma região localizada no sudeste "
            "do Piauí. É conhecida por suas paisagens naturais, "
            "formações rochosas e importantes sítios arqueológicos. "
            "O Parque Nacional da Serra da Capivara preserva um "
            "patrimônio histórico, cultural e ambiental de grande "
            "importância para o Brasil."
        )
    },
    {
        "palavras": [
            "onde fica",
            "localizacao",
            "qual cidade",
            "onde esta localizado",
            "em que estado fica"
        ],
        "resposta": (
            "O Parque Nacional da Serra da Capivara está localizado "
            "no sudeste do estado do Piauí. Sua área abrange partes "
            "dos municípios de São Raimundo Nonato, Coronel José Dias, "
            "João Costa e Canto do Buriti."
        )
    },
    {
        "palavras": [
            "importancia",
            "por que e importante",
            "patrimonio mundial",
            "unesco",
            "reconhecimento"
        ],
        "resposta": (
            "A Serra da Capivara possui grande importância histórica "
            "e científica por preservar sítios arqueológicos e "
            "pinturas rupestres. Em 1991, o Parque Nacional foi "
            "inscrito na Lista do Patrimônio Mundial da UNESCO."
        )
    },
    {
        "palavras": [
            "pinturas rupestres",
            "arte rupestre",
            "desenhos nas pedras",
            "pinturas antigas",
            "quem fez as pinturas"
        ],
        "resposta": (
            "As pinturas rupestres são registros visuais produzidos "
            "por grupos humanos antigos em superfícies rochosas. "
            "Elas representam figuras humanas, animais, cenas de "
            "caça, danças e outras atividades. Esses registros "
            "ajudam os pesquisadores a estudar as sociedades do passado."
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
            "Entre os principais atrativos estão a Pedra Furada, "
            "o Baixão das Mulheres, o Museu do Homem Americano "
            "e o Museu da Natureza. Esses lugares permitem conhecer "
            "a paisagem, a arqueologia e a história natural da região."
        )
    },
    {
        "palavras": [
            "pedra furada",
            "formacao rochosa",
            "cartao postal"
        ],
        "resposta": (
            "A Pedra Furada é uma das formações rochosas mais "
            "conhecidas da Serra da Capivara. Sua abertura natural "
            "na rocha tornou o local um dos símbolos mais conhecidos "
            "do parque."
        )
    },
    {
        "palavras": [
            "museu do homem americano",
            "museu do homem",
            "acervo arqueologico"
        ],
        "resposta": (
            "O Museu do Homem Americano fica em São Raimundo Nonato "
            "e apresenta materiais e informações relacionados às "
            "pesquisas arqueológicas realizadas na região, ajudando "
            "a compreender a presença humana nas Américas."
        )
    },
    {
        "palavras": [
            "museu da natureza",
            "historia natural",
            "fossil"
        ],
        "resposta": (
            "O Museu da Natureza apresenta aspectos da história "
            "natural da região, abordando transformações ambientais, "
            "animais antigos, fósseis e a evolução da paisagem."
        )
    },
    {
        "palavras": [
            "animais",
            "fauna",
            "bichos",
            "animais da caatinga",
            "quais especies"
        ],
        "resposta": (
            "A região abriga animais adaptados ao ambiente da "
            "Caatinga, como tatu-bola, veado-catingueiro, macaco-prego "
            "e diversas espécies de aves. A preservação desses "
            "animais é importante para o equilíbrio ambiental."
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
            "A vegetação da região é característica da Caatinga. "
            "Entre as espécies encontradas estão mandacaru, "
            "xique-xique, bromélias e diferentes arbustos adaptados "
            "ao clima semiárido."
        )
    },
    {
        "palavras": [
            "caatinga",
            "bioma",
            "clima da regiao",
            "vegetacao do piauí"
        ],
        "resposta": (
            "A Caatinga é um bioma exclusivamente brasileiro, "
            "predominante em áreas do Nordeste. Sua vegetação "
            "apresenta adaptações aos períodos de pouca chuva, "
            "com plantas resistentes ao clima semiárido."
        )
    },
    {
        "palavras": [
            "como visitar",
            "dicas de visita",
            "o que levar",
            "visitar o parque",
            "preparar a visita"
        ],
        "resposta": (
            "Para visitar o parque, recomenda-se usar roupas "
            "confortáveis, calçados adequados para caminhada, "
            "levar água, protetor solar e chapéu ou boné. "
            "Também é importante respeitar as orientações dos "
            "guias e verificar as regras atualizadas de visitação."
        )
    },
    {
        "palavras": [
            "preservar",
            "preservacao",
            "conservar",
            "proteger o parque",
            "como ajudar"
        ],
        "resposta": (
            "A preservação começa com atitudes responsáveis: "
            "não deixar lixo, respeitar as trilhas, não retirar "
            "elementos naturais e nunca tocar nas pinturas rupestres. "
            "Proteger o parque é conservar a história e a natureza "
            "para as próximas gerações."
        )
    },
    {
        "palavras": [
            "comida tipica",
            "culinaria",
            "gastronomia",
            "o que comer",
            "pratos regionais"
        ],
        "resposta": (
            "A culinária regional apresenta pratos tradicionais "
            "como carne de sol, galinha caipira e paçoca, além "
            "de preparações que valorizam ingredientes e costumes "
            "do sertão piauiense."
        )
    },
    {
        "palavras": [
            "quem descobriu",
            "descoberta do parque",
            "historia do parque",
            "criado o parque"
        ],
        "resposta": (
            "O Parque Nacional da Serra da Capivara foi criado "
            "em 1979. A arqueóloga Niède Guidon teve papel "
            "fundamental nas pesquisas, na defesa e na valorização "
            "do patrimônio arqueológico da região."
        )
    },
    {
        "palavras": [
            "tamanho do parque",
            "extensao",
            "area do parque",
            "quantos hectares"
        ],
        "resposta": (
            "O Parque Nacional da Serra da Capivara possui "
            "aproximadamente 130 mil hectares de área protegida. "
            "Seu território reúne paisagens, sítios arqueológicos "
            "e diferentes ambientes naturais."
        )
    },
    {
        "palavras": [
            "quantos sitios",
            "sitios arqueologicos",
            "quantidade de sitios",
            "mais de mil sitios"
        ],
        "resposta": (
            "A região possui mais de mil sítios arqueológicos "
            "identificados, com registros que incluem pinturas "
            "rupestres e outros vestígios da presença humana."
        )
    }
]

# ============================================================
# 5. TRATAMENTO E IDENTIFICAÇÃO DAS PERGUNTAS
# ============================================================

def normalizar(texto):
    texto = texto.lower().strip()

    texto = unicodedata.normalize("NFD", texto)

    texto = "".join(
        caractere
        for caractere in texto
        if unicodedata.category(caractere) != "Mn"
    )

    texto = re.sub(r"[^a-z0-9\s]", " ", texto)
    texto = re.sub(r"\s+", " ", texto)

    return texto


def responder(pergunta):

    texto = normalizar(pergunta)

    if not texto:
        return "Por favor, escreva uma pergunta."

    # Reconhece cumprimentos
    cumprimentos = [
        "oi", "ola", "bom dia", "boa tarde",
        "boa noite", "tudo bem", "e ai"
    ]

    if texto in cumprimentos:
        return (
            "Olá! Seja bem-vindo ao CapivaraBot. "
            "Estou pronto para apresentar a Serra da Capivara. "
            "O que você gostaria de saber?"
        )

    palavras_pergunta = set(texto.split())

    melhor_resposta = None
    maior_pontuacao = 0

    for item in BANCO_RESPOSTAS:

        pontuacao = 0

        for termo in item["palavras"]:

            termo = normalizar(termo)

            if termo in texto:
                pontuacao += 5 + len(termo.split())
            else:
                palavras_termo = set(termo.split())
                correspondencias = palavras_pergunta.intersection(
                    palavras_termo
                )
                pontuacao += len(correspondencias)

        if pontuacao > maior_pontuacao:
            maior_pontuacao = pontuacao
            melhor_resposta = item["resposta"]

    if melhor_resposta and maior_pontuacao >= 2:
        return melhor_resposta

    return (
        "Ainda não encontrei uma resposta adequada para essa pergunta. "
        "Você pode reformulá-la ou perguntar sobre a história, "
        "as pinturas rupestres, os pontos turísticos, os animais, "
        "a vegetação ou a preservação da Serra da Capivara."
    )

# ============================================================
# 6. HISTÓRICO DA CONVERSA
# ============================================================

if "mensagens" not in st.session_state:
    st.session_state.mensagens = [
        {
            "role": "assistant",
            "content": (
                "Olá! Eu sou o CapivaraBot. 🐾\n\n"
                "Estou aqui para ajudar você a descobrir a Serra "
                "da Capivara. Escreva sua pergunta no campo abaixo "
                "e vamos explorar esse patrimônio juntos!"
            )
        }
    ]

# ============================================================
# 7. CABEÇALHO INSTITUCIONAL
# ============================================================

st.write("")
st.caption("TURISMO • HISTÓRIA • ARQUEOLOGIA • CULTURA")

st.title("🐾 CapivaraBot")

st.subheader("Seu guia virtual pela Serra da Capivara")

st.write(DESCRICAO)

st.divider()

# ============================================================
# 8. APRESENTAÇÃO VISUAL
# ============================================================

st.header("Conheça um dos maiores patrimônios do Piauí")

st.write(
    "Localizado no sudeste do Piauí, o Parque Nacional da "
    "Serra da Capivara reúne paisagens impressionantes, "
    "formações rochosas, sítios arqueológicos e registros "
    "que ajudam a contar a história das antigas populações humanas."
)

imagem1, imagem2 = st.columns(2, gap="large")

with imagem1:
    try:
        st.image(
            IMAGENS[0]["url"],
            use_container_width=True,
            caption=IMAGENS[0]["legenda"]
        )
    except Exception:
        st.warning("A primeira imagem não pôde ser carregada.")

with imagem2:
    try:
        st.image(
            IMAGENS[1]["url"],
            use_container_width=True,
            caption=IMAGENS[1]["legenda"]
        )
    except Exception:
        st.warning("A segunda imagem não pôde ser carregada.")

st.divider()

# ============================================================
# 9. INFORMAÇÕES PRINCIPAIS
# ============================================================

st.header("Um lugar de história, natureza e cultura")

coluna1, coluna2, coluna3 = st.columns(3, gap="medium")

with coluna1:
    with st.container(border=True):
        st.subheader("🪨 Arqueologia")
        st.write(
            "Sítios arqueológicos e pinturas rupestres "
            "que preservam registros de antigas sociedades."
        )

with coluna2:
    with st.container(border=True):
        st.subheader("🌵 Natureza")
        st.write(
            "A biodiversidade da Caatinga, suas plantas, "
            "animais e formações naturais."
        )

with coluna3:
    with st.container(border=True):
        st.subheader("🏛️ Patrimônio")
        st.write(
            "Um espaço de importância histórica, científica "
            "e cultural reconhecido mundialmente."
        )

st.divider()

# ============================================================
# 10. CHATBOT
# ============================================================

st.header("Converse com o CapivaraBot")

st.write(
    "Quer saber mais sobre a Serra da Capivara? "
    "Digite sua pergunta abaixo. O chatbot apresentará "
    "a resposta nesta conversa."
)

# Apresentação do histórico
with st.container(border=True):

    st.subheader("💬 Atendimento virtual")

    for mensagem in st.session_state.mensagens:

        with st.chat_message(mensagem["role"]):
            st.markdown(mensagem["content"])

# Campo único de perguntas
pergunta = st.chat_input(
    "Ex.: Onde fica a Serra da Capivara?"
)

if pergunta:

    st.session_state.mensagens.append(
        {
            "role": "user",
            "content": pergunta
        }
    )

    resposta = responder(pergunta)

    st.session_state.mensagens.append(
        {
            "role": "assistant",
            "content": resposta
        }
    )

    st.rerun()

# Limpar conversa
if st.button("Limpar histórico da conversa"):

    st.session_state.mensagens = [
        {
            "role": "assistant",
            "content": (
                "Olá novamente! Sou o CapivaraBot. "
                "Qual será sua próxima pergunta?"
            )
        }
    ]

    st.rerun()

st.divider()

# ============================================================
# 11. RODAPÉ
# ============================================================

st.caption("CAPIVARABOT | PROJETO DE TURISMO E TECNOLOGIA")

st.write(
    "Conhecimento, inovação e valorização do patrimônio piauiense."
)

st.write(
    "Desenvolvido pelo Professor Daniel e pelos alunos "
    "Felype, David, Laiane e Mariana."
)

st.caption("Projeto educativo • Piauí • Brasil")
