
import streamlit as st
import unicodedata
import re
import random

# ============================================================
# CAPIVARABOT — SEM IA E SEM API PAGA
# ============================================================

st.set_page_config(
    page_title="CapivaraBot | Serra da Capivara",
    page_icon="🐾",
    layout="centered"
)

# ============================================================
# IMAGENS
# ============================================================

IMAGEM_CAPA = (
    "https://www.viajenaviagem.com/wp-content/uploads/"
    "2013/11/parque-abreinterno.jpg.webp"
)

IMAGEM_PARQUE = (
    "https://www.maladeaventuras.com/wp-content/uploads/"
    "2023/01/parque-serra-da-capivara.jpg"
)

# ============================================================
# VISUAL
# ============================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

.stApp {
    background: linear-gradient(180deg, #f8f3eb, #eee1cf);
    color: #382a22;
}

.block-container {
    max-width: 850px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1, h2, h3 {
    font-family: 'Playfair Display', serif !important;
    color: #432b20;
}

.hero {
    background: linear-gradient(
        120deg,
        rgba(54,35,25,.91),
        rgba(112,69,47,.72)
    ),
    url('""" + IMAGEM_CAPA + """');

    background-size: cover;
    background-position: center;
    padding: 2.5rem 1.5rem;
    border-radius: 22px;
    color: white;
    margin-bottom: 25px;
}

.hero h1 {
    color: white !important;
    font-size: 2.4rem;
}

.hero p {
    color: #fff5e8;
    font-size: 1.05rem;
}

.card {
    background: rgba(255,255,255,.85);
    border: 1px solid #e5d2bc;
    border-radius: 17px;
    padding: 18px;
    margin: 12px 0;
}

div.stButton > button {
    border-radius: 12px;
    border: 1px solid #c6a17c;
    background: #fffaf3;
    color: #563a29;
    font-weight: 600;
    min-height: 42px;
}

div.stButton > button:hover {
    background: #efe0cc;
    border-color: #95643e;
}

[data-testid="stChatMessage"] {
    background: rgba(255,255,255,.75);
    border-radius: 15px;
    padding: 10px;
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# BASE DE CONHECIMENTO
# ============================================================

BANCO = [
    {
        "pergunta": "Onde fica a Serra da Capivara?",
        "palavras": ["onde fica", "localizacao", "localizada", "fica"],
        "resposta": """
A Serra da Capivara está localizada no sudeste do estado do Piauí, no Brasil.

O Parque Nacional abrange áreas de municípios como São Raimundo Nonato,
Coronel José Dias, João Costa e Brejo do Piauí.

A região é conhecida por suas paisagens naturais, formações rochosas
e importantes sítios arqueológicos.
"""
    },
    {
        "pergunta": "Por que a Serra da Capivara é importante?",
        "palavras": ["importancia", "importante", "historia", "historica"],
        "resposta": """
A Serra da Capivara possui grande importância histórica, arqueológica
e ambiental.

O parque reúne milhares de registros arqueológicos, incluindo pinturas
e gravuras rupestres que ajudam pesquisadores a estudar antigas
populações humanas.

Também protege a biodiversidade e as paisagens da Caatinga.
"""
    },
    {
        "pergunta": "O que são pinturas rupestres?",
        "palavras": ["pinturas rupestres", "pintura rupestre", "arte rupestre"],
        "resposta": """
As pinturas rupestres são desenhos produzidos por grupos humanos
do passado em paredes e abrigos rochosos.

Na Serra da Capivara, existem representações de pessoas, animais
e cenas que ajudam a compreender aspectos da vida e da cultura
de antigas populações.
"""
    },
    {
        "pergunta": "Quem foi Niède Guidon?",
        "palavras": ["niede", "guidon", "pesquisadora"],
        "resposta": """
Niède Guidon foi uma arqueóloga brasileira conhecida por seu trabalho
de pesquisa e preservação da Serra da Capivara.

Suas pesquisas contribuíram para ampliar o conhecimento sobre os
vestígios arqueológicos da região e fortalecer a proteção do parque.
"""
    },
    {
        "pergunta": "O que é a Pedra Furada?",
        "palavras": ["pedra furada", "formacao rochosa"],
        "resposta": """
A Pedra Furada é uma das formações rochosas mais conhecidas
da Serra da Capivara.

Seu grande arco natural tornou-se um dos símbolos do parque
e é um dos cenários mais conhecidos da região.
"""
    },
    {
        "pergunta": "Quais animais vivem na região?",
        "palavras": ["animais", "fauna", "bichos", "mocó", "tatu"],
        "resposta": """
A região abriga animais adaptados ao ambiente da Caatinga.

Entre eles estão mocós, tatus, seriemas, répteis e diferentes
espécies de aves.

A diversidade da fauna faz parte da riqueza ambiental do parque.
"""
    },
    {
        "pergunta": "O que é a Caatinga?",
        "palavras": ["caatinga", "bioma", "vegetacao", "plantas"],
        "resposta": """
A Caatinga é um bioma exclusivamente brasileiro.

Possui vegetação adaptada às condições de seca, com plantas
que desenvolveram características para sobreviver à pouca
disponibilidade de água.

Ela é uma parte fundamental do ambiente da Serra da Capivara.
"""
    },
    {
        "pergunta": "Por que preservar o parque?",
        "palavras": ["preservar", "preservacao", "conservar", "proteger"],
        "resposta": """
Preservar a Serra da Capivara é proteger a história, a cultura
e a natureza.

A conservação ajuda a proteger as pinturas rupestres, os sítios
arqueológicos, os animais, as plantas e as paisagens naturais.

Todos podem colaborar respeitando as regras de visitação.
"""
    },
    {
        "pergunta": "Como visitar a Serra da Capivara?",
        "palavras": ["visitar", "visita", "turismo", "passeio", "guia"],
        "resposta": """
A visitação deve ser planejada com antecedência.

O parque possui trilhas e circuitos diferentes. Muitos passeios
exigem acompanhamento de condutores credenciados.

Antes de viajar, consulte as informações oficiais sobre horários,
acesso, condições das trilhas e regras de visitação.
"""
    },
    {
        "pergunta": "O parque é Patrimônio Mundial?",
        "palavras": ["unesco", "patrimonio mundial", "patrimonio humanidade"],
        "resposta": """
Sim! O Parque Nacional Serra da Capivara foi reconhecido como
Patrimônio Mundial pela UNESCO em 1991.

Esse reconhecimento destaca sua importância arqueológica
e cultural para a humanidade.
"""
    },
    {
        "pergunta": "Como foram feitas as pinturas rupestres?",
        "palavras": ["como foram feitas", "pigmentos", "tintas", "pintadas"],
        "resposta": """
As pinturas rupestres foram produzidas com pigmentos naturais
e técnicas utilizadas por grupos humanos antigos.

Os registros mostram diferentes formas de expressão e são
estudados por pesquisadores para compreender as sociedades
do passado.
"""
    },
    {
        "pergunta": "O que estudantes podem aprender no parque?",
        "palavras": ["estudantes", "escola", "educacao", "aprender", "aula"],
        "resposta": """
Os estudantes podem aprender sobre três grandes áreas:

🏺 História e arqueologia: pinturas rupestres e antigas populações.

🌵 Meio ambiente: Caatinga, fauna, flora e preservação.

🪨 Geografia e geologia: formações rochosas e paisagens naturais.

A visita pode transformar o conhecimento escolar em uma
experiência de aprendizagem.
"""
    },
    {
        "pergunta": "Quais cuidados o visitante deve ter?",
        "palavras": ["cuidados", "regras", "lixo", "seguranca", "trilha"],
        "resposta": """
Durante a visita, é importante:

- Respeitar as trilhas e sinalizações.
- Seguir as orientações do condutor.
- Não tocar nas pinturas rupestres.
- Não retirar pedras, plantas ou outros materiais.
- Não deixar lixo no parque.

Esses cuidados ajudam a conservar o patrimônio natural e cultural.
"""
    },
    {
        "pergunta": "Quais curiosidades existem sobre o parque?",
        "palavras": ["curiosidade", "curiosidades", "fatos interessantes"],
        "resposta": """
Aqui estão algumas curiosidades:

1. O parque reúne centenas de sítios arqueológicos.
2. Existem registros de diferentes estilos de pinturas e gravuras.
3. A região possui cânions, paredões e formações rochosas.
4. A Caatinga é parte essencial da paisagem.
5. O parque é reconhecido internacionalmente por sua importância cultural.
"""
    },
    {
        "pergunta": "O que são sítios arqueológicos?",
        "palavras": ["sitios arqueologicos", "sitio arqueologico", "vestigios"],
        "resposta": """
Sítios arqueológicos são lugares onde existem vestígios de
atividades humanas do passado.

Esses vestígios podem incluir ferramentas, pinturas, gravuras
e outros materiais que ajudam a estudar antigas sociedades.
"""
    },
    {
        "pergunta": "Como montar um roteiro educativo de um dia?",
        "palavras": ["roteiro", "um dia", "programacao"],
        "resposta": """
Uma sugestão de roteiro educativo, conforme a disponibilidade
dos circuitos e as regras de visitação:

🌞 MANHÃ
- Conhecer um circuito arqueológico acompanhado por condutor.
- Observar pinturas rupestres.
- Conversar sobre a importância das pesquisas arqueológicas.

🌵 TARDE
- Conhecer uma paisagem natural autorizada.
- Observar características da Caatinga.
- Conversar sobre biodiversidade e preservação.

O roteiro deve ser confirmado previamente com os responsáveis
pela visitação do parque.
"""
    }
]

# ============================================================
# NORMALIZAÇÃO E BUSCA
# ============================================================

def normalizar(texto):
    texto = unicodedata.normalize("NFKD", texto.lower())
    texto = "".join(
        caractere for caractere in texto
        if not unicodedata.combining(caractere)
    )
    texto = re.sub(r"[^a-z0-9\s]", " ", texto)
    return re.sub(r"\s+", " ", texto).strip()


def responder(pergunta):
    texto = normalizar(pergunta)

    if not texto:
        return "Digite uma pergunta para começarmos! 🐾"

    saudacoes = {
        "oi": "Olá! 🐾 Como posso ajudar você a conhecer a Serra da Capivara?",
        "ola": "Olá! Sou o CapivaraBot! Vamos explorar a história e a natureza da Serra da Capivara?",
        "bom dia": "Bom dia! ☀️ O que você gostaria de descobrir sobre a Serra da Capivara?",
        "boa tarde": "Boa tarde! 🐾 Estou pronto para ajudar. Qual é sua pergunta?",
        "boa noite": "Boa noite! 🌙 Vamos conversar sobre a Serra da Capivara?",
        "obrigado": "Por nada! 🐾 Estou aqui para ajudar!",
        "obrigada": "Por nada! 🐾 Estou aqui para ajudar!"
    }

    if texto in saudacoes:
        return saudacoes[texto]

    melhor_resposta = None
    maior_pontuacao = 0

    for item in BANCO:
        pontuacao = 0

        for palavra in item["palavras"]:
            termo = normalizar(palavra)

            if termo in texto:
                pontuacao += 3 if " " in termo else 1

        palavras_titulo = set(normalizar(item["pergunta"]).split())
        palavras_digitadas = set(texto.split())

        pontuacao += len(palavras_titulo & palavras_digitadas)

        if pontuacao > maior_pontuacao:
            maior_pontuacao = pontuacao
            melhor_resposta = item["resposta"]

    if melhor_resposta and maior_pontuacao >= 2:
        return melhor_resposta

    return """
Ainda não encontrei uma resposta específica para essa pergunta
na minha base de conhecimentos. 🐾

Mas posso ajudar você com:

- História da Serra da Capivara.
- Pinturas rupestres.
- Pedra Furada.
- Niède Guidon.
- Arqueologia.
- Caatinga e animais.
- Turismo e preservação.

Experimente reformular sua pergunta usando um desses assuntos!
"""

# ============================================================
# ESTADO DO SITE
# ============================================================

if "pagina" not in st.session_state:
    st.session_state.pagina = "inicio"

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

# ============================================================
# CABEÇALHO
# ============================================================

st.markdown("""
<div class="hero">
    <h1>🐾 CapivaraBot</h1>
    <p>Explore a Serra da Capivara com nosso guia virtual.</p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# PÁGINA INICIAL
# ============================================================

if st.session_state.pagina == "inicio":

    st.markdown("## Sua jornada começa aqui")

    st.write(
        "Descubra um dos patrimônios arqueológicos e naturais "
        "mais importantes do Brasil."
    )

    st.image(
        IMAGEM_PARQUE,
        use_container_width=True
    )

    st.markdown("""
    <div class="card">
        <h3>🏺 História, cultura e natureza</h3>
        <p>
        Converse com o CapivaraBot e descubra informações
        sobre pinturas rupestres, arqueologia, biodiversidade
        e preservação da Serra da Capivara.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### O que você pode explorar?")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**🏺 Arqueologia**")
        st.caption("Conheça os registros das antigas populações.")

    with col2:
        st.markdown("**🌵 Natureza**")
        st.caption("Descubra a Caatinga e sua biodiversidade.")

    if st.button(
        "Começar a explorar →",
        use_container_width=True,
        type="primary"
    ):
        st.session_state.pagina = "chat"
        st.rerun()

# ============================================================
# CHATBOT
# ============================================================

else:

    col1, col2 = st.columns([4, 1])

    with col1:
        st.markdown("## Converse com o CapivaraBot")
        st.caption("Faça uma pergunta e descubra novos conhecimentos.")

    with col2:
        if st.button("Início"):
            st.session_state.pagina = "inicio"
            st.rerun()

    st.info(
        "📚 Modo educativo: respostas disponíveis na base "
        "de conhecimentos do CapivaraBot. Sem API e sem créditos pagos."
    )

    if not st.session_state.mensagens:
        with st.chat_message("assistant", avatar="🐾"):
            st.write(
                "Olá! Eu sou o CapivaraBot! 🐾\n\n"
                "Estou pronto para acompanhar você pela história, "
                "natureza e cultura da Serra da Capivara. "
                "O que você gostaria de conhecer?"
            )

    for mensagem in st.session_state.mensagens:

        avatar = "🧑‍🎓" if mensagem["role"] == "user" else "🐾"

        with st.chat_message(
            mensagem["role"],
            avatar=avatar
        ):
            st.markdown(mensagem["content"])

            if mensagem["role"] == "assistant":
                st.caption("📚 Resposta da base de conhecimentos")

    pergunta = st.chat_input(
        "Digite sua pergunta sobre a Serra da Capivara..."
    )

    if pergunta:

        resposta = responder(pergunta)

        st.session_state.mensagens.append({
            "role": "user",
            "content": pergunta
        })

        st.session_state.mensagens.append({
            "role": "assistant",
            "content": resposta
        })

        st.rerun()

    # ========================================================
    # PERGUNTAS SUGERIDAS
    # ========================================================

    with st.expander("✨ Perguntas para começar"):

        exemplos = [
            "Onde fica a Serra da Capivara?",
            "Por que o parque é importante?",
            "O que são pinturas rupestres?",
            "Quem foi Niède Guidon?",
            "Quais animais vivem na região?",
            "Como montar um roteiro educativo de um dia?"
        ]

        for i, exemplo in enumerate(exemplos):

            if st.button(
                exemplo,
                key=f"pergunta_{i}",
                use_container_width=True
            ):

                resposta = responder(exemplo)

                st.session_state.mensagens.append({
                    "role": "user",
                    "content": exemplo
                })

                st.session_state.mensagens.append({
                    "role": "assistant",
                    "content": resposta
                })

                st.rerun()

    if st.session_state.mensagens:

        if st.button("🗑️ Limpar conversa"):
            st.session_state.mensagens = []
            st.rerun()

# ============================================================
# RODAPÉ
# ============================================================

st.divider()

st.markdown(
    "<center>🐾 CapivaraBot | Projeto educativo sobre "
    "a Serra da Capivara — Piauí</center>",
    unsafe_allow_html=True
)
