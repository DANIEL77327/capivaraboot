import os
import re
import unicodedata

import streamlit as st

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

# ============================================================
# 1. CONFIGURACAO
# ============================================================

st.set_page_config(
    page_title="CapivaraBot | Serra da Capivara",
    page_icon="🐾",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# 2. IMAGENS
# ============================================================

IMAGENS = {
    "capa": "https://www.viajenaviagem.com/wp-content/uploads/2013/11/parque-abreinterno.jpg.webp",
    "paisagem": "https://www.maladeaventuras.com/wp-content/uploads/2023/01/parque-serra-da-capivara.jpg",
    "pedra": "https://commons.wikimedia.org/wiki/Special:FilePath/Pedra_Furada_-_Serra_da_Capivara.jpg",
    "pinturas": "https://commons.wikimedia.org/wiki/Special:FilePath/Arte_rupestre_no_Piau%C3%AD.JPG",
    "andorinhas": "https://commons.wikimedia.org/wiki/Special:FilePath/Baix%C3%A3o_das_Andorinhas_%287940206102%29.jpg",
    "caatinga": "https://commons.wikimedia.org/wiki/Special:FilePath/Bioma_caatinga_serra_da_capivara.jpg",
}

# ============================================================
# 3. ESTILO VISUAL
# ============================================================

st.markdown(
    """
    <style>
    :root {
        --terra: #6d2d16;
        --laranja: #e98232;
        --dourado: #f2b968;
        --areia: #fff0dc;
    }

    .stApp {
        background: linear-gradient(145deg, #21120d, #3c1d10, #24140e);
        color: var(--areia);
    }

    .block-container {
        max-width: 1150px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    h1, h2, h3, h4, p, label {
        color: var(--areia) !important;
    }

    h1 {
        font-weight: 900 !important;
        letter-spacing: -1px;
    }

    h2 { color: var(--dourado) !important; }
    h3 { color: #f5c98d !important; }

    .hero {
        padding: 3.5rem 2rem;
        border-radius: 25px;
        border: 1px solid rgba(255, 190, 112, .65);
        background:
            linear-gradient(90deg, rgba(30, 12, 5, .78), rgba(30, 12, 5, .38)),
            url("https://www.viajenaviagem.com/wp-content/uploads/2013/11/parque-abreinterno.jpg.webp");
        background-size: cover;
        background-position: center;
        text-align: center;
        box-shadow: 0 20px 55px rgba(0,0,0,.35);
    }

    .hero h1 {
        font-size: clamp(2.5rem, 7vw, 4.5rem) !important;
        color: #fff0d7 !important;
        text-shadow: 3px 4px 15px #160700;
    }

    .hero p {
        font-size: 1.1rem;
        text-shadow: 2px 2px 8px #1b0800;
    }

    .hero-tag {
        display: inline-block;
        padding: .55rem 1.2rem;
        border: 1px solid var(--laranja);
        border-radius: 30px;
        background: rgba(53, 22, 8, .8);
        color: #ffe2bd;
        font-weight: 700;
    }

    .stButton > button {
        background: linear-gradient(135deg, #ed9a45, #a94a20);
        color: white !important;
        border: 1px solid #ffc47c;
        border-radius: 30px;
        padding: .7rem 1.1rem;
        font-weight: 800;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #ffb65d, #c65b27);
        border-color: #ffe1b5;
    }

    [data-testid="stChatMessage"] {
        background: rgba(111, 55, 29, .72);
        border: 1px solid rgba(235, 157, 88, .5);
        border-radius: 18px;
        padding: 12px;
        margin-bottom: 12px;
    }

    [data-testid="stChatInput"] textarea {
        background: #fff0dc !important;
        color: #35180e !important;
        border-radius: 16px !important;
    }

    [data-testid="stImage"] img {
        border-radius: 17px;
        border: 1px solid rgba(242, 185, 104, .65);
    }

    div[data-testid="stExpander"] {
        background: rgba(91, 43, 22, .75);
        border: 1px solid #a85e36;
        border-radius: 14px;
        margin-bottom: 8px;
    }

    div[data-testid="stExpander"] summary {
        color: #ffe0b7;
        font-weight: 700;
    }

    .ia-info {
        color: #f2b968;
        font-size: .9rem;
    }

    footer { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# 4. BANCO DE PERGUNTAS
# ============================================================

BANCO = [
    ("Turismo", "Como chegar ao Parque Nacional?",
     ["como chegar", "chegar ao parque", "acesso ao parque"],
     "É possível chegar à região por transporte rodoviário ou aéreo, conforme a disponibilidade de conexões. A partir de São Raimundo Nonato, o deslocamento até os acessos do parque pode ser feito por transporte contratado ou veículo próprio."),
    ("Turismo", "Qual é a melhor época para visitar?",
     ["melhor epoca", "quando visitar", "epoca de chuva"],
     "A visita pode acontecer durante todo o ano. O período chuvoso costuma deixar a vegetação mais verde, enquanto a estação seca apresenta outras características da paisagem."),
    ("Turismo", "Qual é o horário de funcionamento?",
     ["horario de funcionamento", "horario de visita", "que horas abre"],
     "Os horários podem variar conforme os circuitos e as condições operacionais. Consulte as informações atualizadas do ICMBio e dos condutores antes da visita."),
    ("Turismo", "É necessário agendar a visita?",
     ["agendar", "agendamento", "reserva", "marcar visita"],
     "É recomendável organizar o passeio antecipadamente e verificar com um condutor cadastrado a disponibilidade, os horários e as condições dos roteiros."),
    ("Turismo", "É necessário pagar ingresso?",
     ["ingresso", "pagar entrada", "preco da entrada", "valor do ingresso"],
     "As informações oficiais indicam entrada gratuita no parque. Serviços de condução, transporte e outras atividades contratadas podem ter custos."),
    ("Turismo", "Quais são os principais atrativos?",
     ["principais atrativos", "pontos turisticos", "o que visitar", "atracoes"],
     "Entre os atrativos conhecidos estão a Pedra Furada, o Boqueirão da Pedra Furada, o Baixão das Andorinhas, os sítios arqueológicos, mirantes e trilhas."),
    ("Turismo", "Onde posso encontrar hospedagem?",
     ["hospedagem", "hotel", "pousada", "onde ficar"],
     "São Raimundo Nonato oferece hotéis, pousadas e outras opções de hospedagem. É recomendável reservar com antecedência."),
    ("História", "O que é a Serra da Capivara?",
     ["o que e a serra", "sobre a serra", "serra da capivara"],
     "A Serra da Capivara fica no sudeste do Piauí e é conhecida por suas paisagens naturais, formações rochosas e importantes sítios arqueológicos."),
    ("História", "Onde fica a Serra da Capivara?",
     ["onde fica", "localizacao", "qual cidade", "em que estado"],
     "O Parque Nacional da Serra da Capivara fica no sudeste do Piauí e abrange áreas de São Raimundo Nonato, Coronel José Dias, João Costa e Canto do Buriti."),
    ("História", "Qual é a importância da Serra da Capivara?",
     ["importancia", "unesco", "patrimonio mundial"],
     "A região possui grande importância histórica e científica por preservar sítios arqueológicos e pinturas rupestres. O Parque Nacional foi inscrito na Lista do Patrimônio Mundial da UNESCO em 1991."),
    ("História", "Quando o parque foi criado?",
     ["quando foi criado", "criacao do parque", "ano de criacao"],
     "O Parque Nacional da Serra da Capivara foi criado em 1979. A arqueóloga Niède Guidon teve papel fundamental nas pesquisas e na valorização do patrimônio da região."),
    ("Arqueologia", "O que são pinturas rupestres?",
     ["pinturas rupestres", "arte rupestre", "desenhos nas pedras"],
     "São desenhos e representações feitos por antigas populações humanas em superfícies rochosas, utilizando pigmentos naturais."),
    ("Arqueologia", "O que é o Boqueirão da Pedra Furada?",
     ["boqueirao da pedra furada", "boqueirao"],
     "É um dos sítios arqueológicos mais conhecidos da região, com pinturas rupestres e registros importantes para pesquisas sobre a presença humana no continente americano."),
    ("Arqueologia", "Posso fotografar as pinturas rupestres?",
     ["fotografar pinturas", "tirar fotos das pinturas", "fotos das pinturas"],
     "A fotografia deve respeitar as orientações do condutor e as regras de conservação. Não toque nas pinturas nem utilize equipamentos que possam causar danos."),
    ("Natureza", "Quais animais vivem na região?",
     ["animais da caatinga", "fauna", "quais animais", "bichos da serra"],
     "A região abriga animais adaptados à Caatinga, como tatu-bola, veado-catingueiro, macaco-prego e diversas espécies de aves."),
    ("Natureza", "Quais plantas existem na Serra da Capivara?",
     ["plantas", "flora", "vegetacao", "mandacaru", "xique xique"],
     "A vegetação é característica da Caatinga. Entre as espécies estão mandacaru, xique-xique, bromélias e arbustos adaptados ao clima semiárido."),
    ("Natureza", "O que é a Caatinga?",
     ["caatinga", "bioma", "clima da regiao"],
     "A Caatinga é um bioma exclusivamente brasileiro, predominante no Nordeste. Sua vegetação apresenta adaptações aos períodos de pouca chuva."),
    ("Visitação", "O que devo levar para visitar o parque?",
     ["o que levar", "levar na visita", "protetor solar"],
     "Leve água, protetor solar, chapéu ou boné, roupas confortáveis e calçados adequados para caminhada. Confira com o condutor o que é necessário para o roteiro."),
    ("Visitação", "As trilhas são difíceis?",
     ["trilhas dificeis", "dificuldade das trilhas", "nivel de dificuldade"],
     "Existem trilhas com diferentes níveis de dificuldade. Escolha o circuito conforme suas condições e siga as orientações do condutor."),
    ("Visitação", "Crianças podem fazer as trilhas?",
     ["criancas", "criancas nas trilhas", "idade para trilha"],
     "Sim, desde que o roteiro seja adequado à idade e às condições da criança e siga as recomendações do condutor."),
    ("Visitação", "Como posso ajudar a preservar o parque?",
     ["preservar o parque", "proteger o parque", "preservacao"],
     "Não deixe lixo, respeite as trilhas, não toque nas pinturas rupestres e não retire pedras, plantas ou outros elementos naturais."),
]


# ============================================================
# 5. FUNCOES
# ============================================================

def normalizar(texto):
    texto = str(texto).lower().strip()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(
        caractere for caractere in texto
        if unicodedata.category(caractere) != "Mn"
    )
    texto = re.sub(r"[^a-z0-9\s]", " ", texto)
    return re.sub(r"\s+", " ", texto).strip()


def responder(pergunta):
    texto = normalizar(pergunta)

    if not texto:
        return "Escreva uma pergunta para começar."

    if texto in {"oi", "ola", "bom dia", "boa tarde", "boa noite", "tudo bem"}:
        return (
            "Olá! Seja bem-vindo ao CapivaraBot! 🐾 "
            "Estou aqui para ajudar você a conhecer a Serra da Capivara. "
            "O que gostaria de descobrir?"
        )

    melhor_resposta = None
    maior_pontuacao = 0

    for categoria, titulo, palavras, resposta in BANCO:
        for termo in palavras:
            termo = normalizar(termo)
            if termo and termo in texto:
                pontuacao = 10 + len(termo.split())
                if pontuacao > maior_pontuacao:
                    maior_pontuacao = pontuacao
                    melhor_resposta = resposta

    if melhor_resposta:
        return melhor_resposta

    return (
        "Ainda não encontrei uma resposta específica para essa pergunta. "
        "Tente reformular ou pergunte sobre turismo, história, arqueologia, "
        "natureza ou visitação."
    )


def resumir_erro_ia(erro):
    """Gera uma mensagem técnica útil sem expor uma chave secreta."""
    mensagem = f"{type(erro).__name__}: {erro}"
    mensagem = re.sub(r"sk-[A-Za-z0-9_-]{10,}", "[CHAVE OCULTADA]", mensagem)
    return mensagem[:700]


def obter_cliente_ia():
    """Obtém a chave dos Secrets do Streamlit ou das variáveis de ambiente."""
    if OpenAI is None:
        st.session_state.erro_ia = (
            "A biblioteca 'openai' não está instalada. "
            "Adicione openai>=1.0.0 ao requirements.txt."
        )
        return None

    chave = None
    try:
        chave = st.secrets.get("OPENAI_API_KEY")
    except Exception:
        chave = None

    if not chave:
        chave = os.getenv("OPENAI_API_KEY")

    if not chave or not str(chave).strip():
        st.session_state.erro_ia = (
            "A chave OPENAI_API_KEY não foi encontrada nos Secrets "
            "do Streamlit."
        )
        return None

    try:
        return OpenAI(api_key=str(chave).strip(), timeout=45.0, max_retries=1)
    except Exception as erro:
        st.session_state.erro_ia = resumir_erro_ia(erro)
        return None


def responder_com_ia():
    """Tenta responder com IA; se falhar, usa o banco e guarda o motivo."""
    st.session_state.erro_ia = ""
    pergunta_atual = st.session_state.mensagens[-1]["content"]
    pergunta_normalizada = normalizar(pergunta_atual)

    # Saudações simples podem ser respondidas diretamente pelo projeto.
    if pergunta_normalizada in {
        "oi", "ola", "bom dia", "boa tarde", "boa noite", "tudo bem"
    }:
        return responder(pergunta_atual), "Banco"

    cliente = obter_cliente_ia()
    if cliente is None:
        return responder(pergunta_atual), "Banco"

    base_conhecimento = "\n\n".join(
        f"Categoria: {categoria}\nPergunta: {titulo}\nResposta: {resposta}"
        for categoria, titulo, palavras, resposta in BANCO
    )

    instrucoes = f"""
Você é o CapivaraBot, um guia virtual educativo e turístico
especializado no Parque Nacional da Serra da Capivara, no Piauí.

Responda em português brasileiro, com clareza, educação e linguagem simples.
Ajude com turismo, história, arqueologia, pinturas rupestres, natureza,
cultura e orientações gerais de visitação.

Não invente preços, horários, telefones, rotas ou regras oficiais.
Quando a informação puder mudar, recomende confirmar com o ICMBio
ou com um condutor cadastrado.
Oriente sempre a preservar as pinturas, trilhas, animais e ambiente natural.

Use este banco de conhecimento como referência:
{base_conhecimento}
"""

    historico = []
    for mensagem in st.session_state.mensagens[-12:]:
        if mensagem.get("role") in ("user", "assistant"):
            historico.append({
                "role": mensagem["role"],
                "content": mensagem.get("content", ""),
            })

    try:
        resposta = cliente.responses.create(
            model="gpt-4.1-mini",
            instructions=instrucoes,
            input=historico,
        )

        texto = (getattr(resposta, "output_text", None) or "").strip()
        if texto:
            return texto, "IA"

        st.session_state.erro_ia = (
            "A API respondeu, mas não retornou texto. "
            "Tente enviar a pergunta novamente."
        )
        return responder(pergunta_atual), "Banco"

    except Exception as erro:
        st.session_state.erro_ia = resumir_erro_ia(erro)
        return responder(pergunta_atual), "Banco"


# ============================================================
# 6. ESTADO DA APLICACAO
# ============================================================

if "pagina" not in st.session_state:
    st.session_state.pagina = "inicio"

if "erro_ia" not in st.session_state:
    st.session_state.erro_ia = ""

if "mensagens" not in st.session_state:
    st.session_state.mensagens = [
        {
            "role": "assistant",
            "content": (
                "Olá! Eu sou o CapivaraBot! 🐾\n\n"
                "Estou pronto para acompanhar você pela história, "
                "natureza e cultura da Serra da Capivara. "
                "O que você gostaria de conhecer?"
            ),
        }
    ]


# ============================================================
# 7. TELA INICIAL
# ============================================================

if st.session_state.pagina == "inicio":
    st.markdown(
        """
        <div class="hero">
            <div class="hero-tag">TURISMO • HISTÓRIA • ARQUEOLOGIA • CULTURA</div>
            <h1>🐾 CapivaraBot</h1>
            <h3>Seu guia virtual pela Serra da Capivara</h3>
            <p>Uma experiência interativa para conhecer a história,
            a arqueologia, a natureza e a riqueza cultural do Piauí.</p>
            <p>🌵 &nbsp; 🪨 &nbsp; 🦅 &nbsp; 🐾</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    if st.button("🐾 COMEÇAR A EXPLORAR", use_container_width=True):
        st.session_state.pagina = "chatbot"
        st.rerun()

    st.divider()
    st.markdown("## Uma terra onde a história está nas rochas")
    st.write(
        "Entre paredões de arenito, pinturas rupestres e paisagens da Caatinga, "
        "a Serra da Capivara guarda um patrimônio histórico, cultural e natural."
    )

    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.image(
            IMAGENS["pedra"],
            use_container_width=True,
            caption="Pedra Furada — um dos símbolos da região.",
        )
    with col2:
        st.image(
            IMAGENS["pinturas"],
            use_container_width=True,
            caption="Pinturas rupestres preservadas nas rochas.",
        )

    st.markdown("## Uma paisagem cheia de vida")
    c1, c2, c3 = st.columns(3, gap="large")
    with c1:
        st.image(IMAGENS["paisagem"], use_container_width=True)
        st.markdown("**Paisagens naturais**")
        st.caption("Formações rochosas e cenários marcantes.")
    with c2:
        st.image(IMAGENS["caatinga"], use_container_width=True)
        st.markdown("**Natureza do sertão**")
        st.caption("A riqueza e as adaptações da Caatinga.")
    with c3:
        st.image(IMAGENS["andorinhas"], use_container_width=True)
        st.markdown("**Baixão das Andorinhas**")
        st.caption("Um dos cenários conhecidos da região.")

    st.divider()
    st.markdown("### CAPIVARABOT | CONHECIMENTO, TECNOLOGIA E PATRIMÔNIO")
    st.caption(
        "Desenvolvido pelo Professor Daniel e pelos alunos "
        "Felype, David, Laiane e Mariana."
    )
    st.caption("Projeto educativo • Piauí • Brasil")


# ============================================================
# 8. TELA DO CHATBOT
# ============================================================

elif st.session_state.pagina == "chatbot":
    topo1, topo2 = st.columns([4, 1])

    with topo1:
        st.title("🐾 CapivaraBot")
        st.caption("Explore a Serra da Capivara com nosso guia virtual.")

    with topo2:
        if st.button("← Início", use_container_width=True):
            st.session_state.pagina = "inicio"
            st.rerun()

    st.divider()
    st.markdown("## Sua jornada começa aqui")
    st.write(
        "Faça uma pergunta no campo abaixo. Você também pode explorar "
        "as perguntas frequentes depois da conversa."
    )

    cliente_disponivel = obter_cliente_ia() is not None

    if cliente_disponivel:
        st.markdown(
            '<p class="ia-info">✦ Chave encontrada. A conexão será testada ao enviar uma pergunta.</p>',
            unsafe_allow_html=True,
        )
    else:
        st.info(
            "A IA ainda não está pronta. O banco de perguntas continua disponível."
        )

    # Exibe o histórico e identifica a origem de cada resposta.
    for mensagem in st.session_state.mensagens:
        with st.chat_message(mensagem["role"]):
            st.markdown(mensagem["content"])

            if mensagem["role"] == "assistant":
                origem = mensagem.get("origem")

                if origem == "IA":
                    st.caption("✦ Resposta gerada pela Inteligência Artificial")
                elif origem == "Banco":
                    st.caption("📚 Resposta do banco de perguntas")

    if st.session_state.get("erro_ia"):
        st.error("A inteligência artificial não conseguiu responder.")
        st.caption("Detalhe técnico: " + st.session_state.erro_ia)

    pergunta = st.chat_input("Ex.: O que são pinturas rupestres?")

    if pergunta:
        st.session_state.mensagens.append({
            "role": "user",
            "content": pergunta,
        })

        with st.spinner("O CapivaraBot está preparando sua resposta..."):
            resposta, origem = responder_com_ia()

        st.session_state.mensagens.append({
            "role": "assistant",
            "content": resposta,
            "origem": origem,
        })

        st.rerun()

    acoes1, acoes2 = st.columns(2)

    with acoes1:
        if st.button("🗑️ Limpar conversa", use_container_width=True):
            st.session_state.erro_ia = ""
            st.session_state.mensagens = [
                {
                    "role": "assistant",
                    "content": "Olá novamente! Qual será sua próxima pergunta?",
                }
            ]
            st.rerun()

    with acoes2:
        if st.button("↩️ Voltar ao início", use_container_width=True):
            st.session_state.pagina = "inicio"
            st.rerun()

    st.divider()
    st.markdown("## Explore por assunto")

    categorias = ["Turismo", "História", "Arqueologia", "Natureza", "Visitação"]

    for categoria in categorias:
        itens = [item for item in BANCO if item[0] == categoria]

        with st.expander(f"📚 {categoria}"):
            for _, titulo, _, resposta in itens:
                st.markdown(f"**{titulo}**")
                st.write(resposta)
                st.divider()

    st.divider()
    st.markdown("### 🐾 CAPIVARABOT")
    st.caption(
        "Conhecimento, tecnologia e valorização do patrimônio piauiense."
    )
    st.caption(
        "Desenvolvido pelo Professor Daniel e pelos alunos "
        "Felype, David, Laiane e Mariana."
    )
    st.caption("Projeto educativo • Piauí • Brasil")
