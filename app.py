
import streamlit as st
import unicodedata
import re

# ============================================================
# 1. CONFIGURAÇÃO
# ============================================================

st.set_page_config(
    page_title="CapivaraBot | Serra da Capivara",
    page_icon="🐾",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# 2. IDENTIDADE VISUAL
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
# 3. BANCO DE CONHECIMENTO
# ============================================================

BANCO = [

    # TURISMO
    ("Turismo", "Como chegar ao Parque Nacional da Serra da Capivara?",
     ["como chegar", "chegar ao parque", "transporte rodoviario", "acesso ao parque"],
     "É possível chegar à região por transporte rodoviário ou aéreo, conforme a disponibilidade de voos e conexões. A partir de São Raimundo Nonato, o deslocamento até os acessos do parque pode ser feito por transporte contratado ou veículo próprio, conforme o roteiro."),

    ("Turismo", "Qual é a distância entre São Raimundo Nonato e o parque?",
     ["distancia entre", "quantos km", "distancia de sao raimundo", "perto da cidade"],
     "A distância depende da entrada e do atrativo escolhido. O parque possui diferentes acessos e circuitos, por isso é importante verificar o percurso antes de sair."),

    ("Turismo", "Onde posso encontrar hospedagem para visitar o parque?",
     ["hospedagem", "hotel", "pousada", "onde ficar"],
     "São Raimundo Nonato oferece opções de hotéis, pousadas e outras hospedagens. Também existem alternativas em municípios próximos. É recomendável reservar antecipadamente."),

    ("Turismo", "Existem restaurantes próximos ao parque?",
     ["restaurantes", "restaurante", "onde comer", "alimentacao"],
     "São Raimundo Nonato possui restaurantes, lanchonetes e estabelecimentos que oferecem refeições regionais e outras opções gastronômicas."),

    ("Turismo", "Quais são as comidas típicas da região?",
     ["comida tipica", "culinaria", "gastronomia", "pratos regionais"],
     "A culinária regional apresenta pratos tradicionais como carne de sol, galinha caipira e paçoca, além de preparações que valorizam ingredientes e costumes do sertão piauiense."),

    ("Turismo", "Quais são os principais atrativos do parque?",
     ["principais atrativos", "pontos turisticos", "atracoes", "o que visitar"],
     "Entre os principais atrativos estão a Pedra Furada, o Boqueirão da Pedra Furada, o Baixão das Andorinhas, os circuitos de sítios arqueológicos, os mirantes e as trilhas."),

    ("Turismo", "O que é a Pedra Furada?",
     ["pedra furada", "formacao rochosa", "cartao postal"],
     "É uma impressionante formação rochosa natural com uma abertura que se tornou um dos símbolos mais conhecidos da Serra da Capivara."),

    ("Turismo", "O que é o Baixão das Andorinhas?",
     ["baixao das andorinhas", "andorinhas"],
     "É um atrativo natural conhecido por suas formações rochosas e pela observação de aves, especialmente no final da tarde, quando andorinhas e outros pássaros podem ser vistos voando na região."),

    ("Turismo", "Existem mirantes no parque?",
     ["mirantes", "mirante", "vista panoramica"],
     "Sim. O parque possui pontos de observação que permitem contemplar as paisagens da Caatinga, os vales e as formações rochosas."),

    ("Turismo", "Existem passeios para contemplar o pôr do sol?",
     ["por do sol", "contemplar o sol", "passeio no final da tarde"],
     "Alguns roteiros permitem contemplar a paisagem no final da tarde. É necessário verificar com o condutor os locais autorizados e os horários de retorno."),

    ("Turismo", "Onde posso contratar um condutor turístico?",
     ["contratar condutor", "condutor turistico", "guia cadastrado"],
     "Você pode buscar informações junto à associação ou aos serviços de condutores cadastrados, agências de turismo locais e canais oficiais de atendimento do parque."),

    ("Turismo", "Existe transporte turístico para chegar aos atrativos?",
     ["transporte turistico", "transporte para atrativos", "empresas de transporte"],
     "Existem prestadores de serviços que oferecem transporte e passeios na região. Consulte as empresas locais para verificar disponibilidade, valores e condições."),

    ("Turismo", "Existe algum museu para visitar na região?",
     ["museus", "museu na regiao", "museu para visitar"],
     "Sim. O Museu do Homem Americano e o Museu da Natureza são importantes atrações culturais e científicas da região."),

    ("Turismo", "O que posso conhecer no Museu do Homem Americano?",
     ["museu do homem americano", "museu do homem", "acervo arqueologico"],
     "O museu apresenta informações sobre a presença humana na região, pesquisas arqueológicas, vestígios encontrados e a história das antigas populações."),

    ("Turismo", "O que posso conhecer no Museu da Natureza?",
     ["museu da natureza", "historia da natureza", "evolucao da vida"],
     "O museu apresenta a história da natureza e as transformações ambientais do planeta, com exposições sobre a evolução da vida e os acontecimentos que marcaram a região."),

    # HISTÓRIA
    ("História", "O que é a Serra da Capivara?",
     ["o que e a serra", "sobre a serra", "serra da capivara"],
     "A Serra da Capivara é uma região localizada no sudeste do Piauí. É conhecida por suas paisagens naturais, formações rochosas e importantes sítios arqueológicos. O Parque Nacional preserva um patrimônio histórico, cultural e ambiental de grande importância para o Brasil."),

    ("História", "Onde fica a Serra da Capivara?",
     ["onde fica", "localizacao", "qual cidade", "em que estado"],
     "O Parque Nacional da Serra da Capivara está localizado no sudeste do estado do Piauí. Sua área abrange partes dos municípios de São Raimundo Nonato, Coronel José Dias, João Costa e Canto do Buriti."),

    ("História", "Qual é a importância da Serra da Capivara?",
     ["importancia", "unesco", "patrimonio mundial", "reconhecimento"],
     "A Serra da Capivara possui grande importância histórica e científica por preservar sítios arqueológicos e pinturas rupestres. Em 1991, o Parque Nacional foi inscrito na Lista do Patrimônio Mundial da UNESCO."),

    ("História", "Qual é a história da criação do parque?",
     ["historia da criacao", "quem descobriu", "criado o parque", "criacao do parque"],
     "O Parque Nacional da Serra da Capivara foi criado em 1979. A arqueóloga Niède Guidon teve papel fundamental nas pesquisas, na defesa e na valorização do patrimônio arqueológico da região."),

    ("História", "Qual é o tamanho do parque?",
     ["tamanho do parque", "extensao", "area do parque", "hectares"],
     "O Parque Nacional da Serra da Capivara possui aproximadamente 130 mil hectares de área protegida. Seu território reúne paisagens, sítios arqueológicos e diferentes ambientes naturais."),

    # ARQUEOLOGIA
    ("Arqueologia", "O que são pinturas rupestres?",
     ["pinturas rupestres", "arte rupestre", "desenhos nas pedras", "pinturas antigas"],
     "São desenhos e representações produzidos por antigas populações humanas em superfícies rochosas, utilizando pigmentos naturais."),

    ("Arqueologia", "O que é o Boqueirão da Pedra Furada?",
     ["boqueirao da pedra furada", "boqueirao"],
     "É um dos sítios arqueológicos mais importantes e conhecidos da região, com pinturas rupestres e registros fundamentais para os estudos sobre a presença humana no continente americano."),

    ("Arqueologia", "Quantos sítios arqueológicos existem no parque?",
     ["quantos sitios", "sitios arqueologicos", "quantidade de sitios", "mais de mil sitios"],
     "O parque possui mais de mil sítios arqueológicos cadastrados, sendo centenas deles com registros de pinturas rupestres."),

    ("Arqueologia", "É possível fotografar as pinturas rupestres?",
     ["fotografar pinturas", "tirar fotos das pinturas", "fotos das pinturas"],
     "Em geral, é possível fotografar os registros respeitando as orientações do condutor e as regras de conservação. Não se deve tocar nas pinturas nem utilizar equipamentos ou iluminação que possam causar danos."),

    ("Arqueologia", "Como posso ajudar na preservação das pinturas rupestres?",
     ["preservar pinturas", "proteger pinturas", "conservar pinturas"],
     "Não toque nas pinturas, não escreva nas rochas, não utilize produtos químicos e respeite as áreas delimitadas para visitação."),

    ("Arqueologia", "O que acontece se um visitante danificar um sítio arqueológico?",
     ["danificar sitio", "danificar pinturas", "destruir patrimonio", "danos arqueologicos"],
     "Danificar o patrimônio arqueológico é uma infração e pode gerar responsabilização conforme a legislação brasileira. As pinturas e os sítios são bens que precisam ser protegidos."),

    # NATUREZA
    ("Natureza", "Quais animais vivem na Serra da Capivara?",
     ["animais da caatinga", "fauna", "quais animais", "bichos da serra"],
     "A região abriga animais adaptados ao ambiente da Caatinga, como tatu-bola, veado-catingueiro, macaco-prego e diversas espécies de aves. A preservação desses animais é importante para o equilíbrio ambiental."),

    ("Natureza", "Quais plantas existem na Serra da Capivara?",
     ["plantas", "flora", "vegetacao", "mandacaru", "xique xique"],
     "A vegetação da região é característica da Caatinga. Entre as espécies encontradas estão mandacaru, xique-xique, bromélias e diferentes arbustos adaptados ao clima semiárido."),

    ("Natureza", "O que é a Caatinga?",
     ["caatinga", "bioma", "clima da regiao"],
     "A Caatinga é um bioma exclusivamente brasileiro, predominante em áreas do Nordeste. Sua vegetação apresenta adaptações aos períodos de pouca chuva, com plantas resistentes ao clima semiárido."),

    ("Natureza", "É possível observar animais silvestres?",
     ["animais silvestres", "observar animais", "observar bichos"],
     "Sim. O parque abriga diversas espécies da fauna da Caatinga. A observação deve acontecer à distância, sem alimentar, perseguir ou tentar tocar nos animais."),

    ("Natureza", "O que fazer se encontrar um animal silvestre?",
     ["encontrar animal", "animal durante visita", "animal silvestre durante"],
     "Mantenha distância, não tente alimentar ou tocar no animal e avise o condutor responsável."),

    ("Natureza", "Posso levar animais de estimação para o parque?",
     ["animais de estimacao", "cachorro", "gato", "pet"],
     "A entrada de animais domésticos está sujeita às regras da unidade de conservação. Consulte previamente o ICMBio antes de levar seu animal."),

    ("Natureza", "Como o visitante pode contribuir com o turismo sustentável?",
     ["turismo sustentavel", "contribuir com turismo", "turismo responsavel"],
     "Contratando serviços locais, valorizando a cultura regional, respeitando as comunidades, evitando desperdícios e preservando o meio ambiente."),

    # VISITAÇÃO
    ("Visitação", "Qual é a melhor época para visitar o parque?",
     ["melhor epoca", "quando visitar", "epoca de chuva", "estacao seca"],
     "A visita pode acontecer durante todo o ano. O período de chuvas costuma deixar a vegetação mais verde, enquanto a estação seca apresenta paisagens diferentes. A escolha depende da preferência do visitante."),

    ("Visitação", "Qual é o horário de funcionamento do parque?",
     ["horario de funcionamento", "horario", "abre", "fecha"],
     "Os horários de visitação podem variar conforme os circuitos e as condições operacionais. Consulte as informações atualizadas do ICMBio e dos condutores antes de programar o passeio."),

    ("Visitação", "É necessário agendar a visita?",
     ["agendar", "agendamento", "reserva", "marcar visita"],
     "É recomendável organizar o passeio antecipadamente e entrar em contato com um condutor cadastrado para verificar disponibilidade, horários e condições dos roteiros."),

    ("Visitação", "É necessário pagar ingresso para entrar no parque?",
     ["ingresso", "pagar entrada", "preco da entrada", "valor do ingresso"],
     "As informações oficiais de visitação do ICMBio indicam entrada gratuita. Entretanto, serviços de condução, transporte e outras atividades contratadas podem ter custos."),

    ("Visitação", "É obrigatório contratar um guia ou condutor?",
     ["guia", "condutor", "guia turistico", "obrigatorio contratar"],
     "A visitação deve seguir as regras oficiais do parque, que preveem acompanhamento por condutor cadastrado. Consulte o ICMBio para confirmar as condições aplicáveis ao roteiro escolhido."),

    ("Visitação", "Quanto tempo dura um passeio no parque?",
     ["duracao do passeio", "quanto tempo dura", "tempo de passeio"],
     "Depende do circuito escolhido. Existem passeios de algumas horas e roteiros que podem ocupar um dia inteiro."),

    ("Visitação", "Posso visitar o parque em apenas um dia?",
     ["visitar em um dia", "um dia no parque", "passeio de um dia"],
     "Sim. É possível conhecer alguns atrativos em um dia, mas para explorar diferentes circuitos e sítios arqueológicos é recomendável reservar mais tempo."),

    ("Visitação", "O parque funciona em feriados e finais de semana?",
     ["feriados", "final de semana", "fim de semana", "sabado", "domingo"],
     "A visitação depende do calendário e das condições operacionais. Confirme antecipadamente com o ICMBio ou com os responsáveis pela condução turística."),

    ("Visitação", "É possível visitar o parque por conta própria?",
     ["por conta propria", "sem guia", "visitar sozinho"],
     "A visita deve respeitar as regras de acompanhamento e os roteiros autorizados. Entre em contato com um condutor cadastrado antes de iniciar o passeio."),

    ("Visitação", "O que devo levar para visitar o parque?",
     ["o que levar", "levar na visita", "protetor solar", "roupas para visitar"],
     "Leve água suficiente, protetor solar, chapéu ou boné, roupas confortáveis, calçados adequados para caminhada e lanches, conforme a duração do roteiro."),

    ("Visitação", "Todos os atrativos podem ser visitados no mesmo dia?",
     ["todos os atrativos", "visitar tudo", "mesmo dia"],
     "Não necessariamente. Os atrativos estão distribuídos em diferentes áreas e circuitos. O ideal é organizar um roteiro com o condutor, considerando distância, duração e dificuldade das caminhadas."),

    ("Visitação", "O parque possui trilhas para caminhadas?",
     ["trilhas", "caminhadas", "trilha no parque"],
     "Sim. Existem trilhas com diferentes distâncias e níveis de dificuldade, que permitem conhecer sítios arqueológicos e paisagens naturais."),

    ("Visitação", "As trilhas são difíceis?",
     ["trilhas dificeis", "dificuldade das trilhas", "nivel de dificuldade"],
     "Algumas são leves e outras exigem maior esforço físico. É importante escolher o circuito de acordo com as condições físicas e as orientações do condutor."),

    ("Visitação", "Crianças podem fazer as trilhas?",
     ["criancas", "criancas nas trilhas", "idade para trilha"],
     "Sim, desde que o roteiro seja adequado à idade, às condições da criança e às recomendações de segurança."),

    ("Visitação", "Pessoas idosas podem visitar o parque?",
     ["idosos", "pessoas idosas", "terceira idade"],
     "Sim. É possível selecionar roteiros com caminhadas mais curtas e acessíveis, conforme as condições de cada visitante."),

    ("Visitação", "É possível fazer passeios de bicicleta?",
     ["bicicleta", "passeio de bicicleta", "ciclismo"],
     "A possibilidade depende das regras e dos roteiros autorizados. Consulte a administração do parque e os prestadores de serviços locais antes de planejar essa atividade."),

    ("Visitação", "Posso fazer piquenique no parque?",
     ["piquenique", "lanche no parque", "comer no parque"],
     "A alimentação deve respeitar as áreas permitidas e as orientações de visitação. Nunca deixe restos de alimentos ou embalagens no ambiente natural."),

    ("Visitação", "Qual é o melhor horário para fotografar as paisagens?",
     ["melhor horario fotografar", "fotografar paisagens", "fotos da paisagem"],
     "O início da manhã e o final da tarde costumam oferecer iluminação interessante para fotografias. Respeite sempre os horários autorizados de visitação."),

    ("Visitação", "É necessário ter preparo físico para conhecer o parque?",
     ["preparo fisico", "condicionamento", "esforco fisico"],
     "Não para todos os passeios. Existem opções com diferentes níveis de esforço, mas é importante informar ao condutor suas limitações para escolher o roteiro adequado."),

    ("Visitação", "O parque possui banheiros e pontos de apoio?",
     ["banheiros", "pontos de apoio", "infraestrutura do parque"],
     "A infraestrutura varia conforme o circuito e o atrativo. Antes de sair, confirme com o condutor onde existem banheiros, pontos de apoio e locais para descanso."),

    ("Visitação", "Existe sinal de celular e internet dentro do parque?",
     ["sinal de celular", "internet", "wifi", "rede de celular"],
     "O sinal pode ser limitado ou inexistente em determinados trechos. É recomendável combinar previamente o roteiro, os horários e os pontos de encontro."),

    ("Visitação", "Existe atendimento de emergência dentro do parque?",
     ["emergencia", "atendimento medico", "socorro", "acidente"],
     "O visitante deve seguir as orientações do condutor e informar previamente qualquer necessidade especial. Em emergências, deve-se acionar os serviços públicos competentes."),

    ("Visitação", "Existem atrativos com acessibilidade?",
     ["acessibilidade", "cadeirante", "mobilidade reduzida", "acessivel"],
     "Existem sítios arqueológicos com estruturas adaptadas para pessoas com mobilidade reduzida. É importante consultar previamente quais atrativos oferecem acessibilidade e quais são as condições de visitação."),

    ("Visitação", "O que devo fazer em caso de chuva durante o passeio?",
     ["chuva durante", "chovendo", "tempo chuvoso", "chuva no passeio"],
     "Siga imediatamente as orientações do condutor. Dependendo das condições climáticas, algumas trilhas e áreas podem ter a visitação suspensa por segurança."),

    ("Visitação", "É permitido fumar dentro do parque?",
     ["fumar", "cigarro", "permitido fumar"],
     "O visitante deve respeitar as restrições ambientais e as orientações da administração, especialmente devido ao risco de incêndios na vegetação da Caatinga."),

    ("Visitação", "Posso retirar pedras ou pedaços de rochas como lembrança?",
     ["retirar pedras", "levar pedras", "pedras como lembranca", "retirar rochas"],
     "Não. É proibido retirar materiais arqueológicos, pedras, fósseis, plantas ou qualquer elemento natural do parque.")
]


# ============================================================
# 4. TRATAMENTO DAS PERGUNTAS
# ============================================================

def normalizar(texto):
    texto = texto.lower().strip()
    texto = unicodedata.normalize("NFD", texto)

    texto = "".join(
        caractere for caractere in texto
        if unicodedata.category(caractere) != "Mn"
    )

    texto = re.sub(r"[^a-z0-9\s]", " ", texto)
    texto = re.sub(r"\s+", " ", texto)

    return texto


def responder(pergunta):
    texto = normalizar(pergunta)

    if not texto:
        return "Digite uma pergunta para começar."

    if texto in ["oi", "ola", "bom dia", "boa tarde", "boa noite"]:
        return (
            "Olá! Seja bem-vindo ao CapivaraBot! 🐾 "
            "Estou pronto para ajudar você a descobrir as riquezas "
            "da Serra da Capivara."
        )

    melhor = None
    maior = 0

    for categoria, pergunta_base, palavras, resposta in BANCO:
        pontos = 0

        for termo in palavras:
            termo = normalizar(termo)

            if termo in texto:
                pontos = max(pontos, 10 + len(termo.split()))

        if pontos > maior:
            maior = pontos
            melhor = resposta

    if melhor and maior >= 10:
        return melhor

    return (
        "Ainda não encontrei uma resposta para essa pergunta. "
        "Tente utilizar outras palavras ou escolha uma das abas "
        "para conhecer os assuntos disponíveis."
    )


# ============================================================
# 5. NAVEGAÇÃO ENTRE AS DUAS TELAS
# ============================================================

if "pagina" not in st.session_state:
    st.session_state.pagina = "inicio"

if "mensagens" not in st.session_state:
    st.session_state.mensagens = [
        {
            "role": "assistant",
            "content": (
                "Olá! Eu sou o CapivaraBot! 🐾\n\n"
                "Pode perguntar sobre turismo, história, arqueologia, "
                "natureza e visitação da Serra da Capivara."
            )
        }
    ]


# ============================================================
# 6. TELA INICIAL
# ============================================================

if st.session_state.pagina == "inicio":

    st.write("")
    st.write("")

    st.image(IMAGEM_CAPA, use_container_width=True)

    st.write("")

    _, centro, _ = st.columns([1, 4, 1])

    with centro:
        st.title("🐾 CapivaraBot")

        st.subheader("Seu guia virtual pela Serra da Capivara")

        st.write(
            "Uma experiência interativa para conhecer a história, "
            "a arqueologia, a natureza e a riqueza cultural do Piauí."
        )

        st.write("")
        st.markdown(
            "🏛️ **TURISMO**  •  🪨 **HISTÓRIA**  •  "
            "🎨 **ARQUEOLOGIA**  •  🌵 **NATUREZA**"
        )

        st.write("")
        st.write(
            "Descubra os registros deixados nas rochas, "
            "conheça os animais da Caatinga e explore um "
            "dos maiores patrimônios culturais do Brasil."
        )

        st.write("")

        if st.button(
            "🐾 COMEÇAR EXPERIÊNCIA",
            use_container_width=True,
            type="primary"
        ):
            st.session_state.pagina = "chatbot"
            st.rerun()

    st.write("")
    st.divider()

    st.subheader("Uma paisagem que guarda histórias")

    st.write(
        "A Serra da Capivara reúne formações rochosas, "
        "pinturas rupestres, biodiversidade e paisagens "
        "que representam a riqueza natural e cultural do Piauí."
    )

    st.image(
        IMAGEM_PARQUE,
        use_container_width=True,
        caption="Parque Nacional da Serra da Capivara — Piauí"
    )

    st.write("")
    st.caption(
        "CAPIVARABOT • CONHECIMENTO • TECNOLOGIA • PATRIMÔNIO"
    )


# ============================================================
# 7. TELA DO CHATBOT
# ============================================================

elif st.session_state.pagina == "chatbot":

    topo1, topo2 = st.columns([4, 1])

    with topo1:
        st.title("🐾 CapivaraBot")
        st.caption("Seu guia virtual pela Serra da Capivara")

    with topo2:
        if st.button("← Início", use_container_width=True):
            st.session_state.pagina = "inicio"
            st.rerun()

    st.divider()

    st.write(
        "Explore os assuntos abaixo ou converse diretamente "
        "com nosso assistente virtual."
    )

    # --------------------------------------------------------
    # ABAS
    # --------------------------------------------------------

    abas = st.tabs([
        "💬 Atendimento",
        "🧭 Turismo",
        "📜 História",
        "🎨 Arqueologia",
        "🌵 Natureza",
        "🥾 Visitação"
    ])

    # --------------------------------------------------------
    # ABA 1 - ATENDIMENTO
    # --------------------------------------------------------

    with abas[0]:

        st.subheader("Converse com nosso guia virtual")

        st.write(
            "Digite sua pergunta e receba informações "
            "sobre a Serra da Capivara."
        )

        for mensagem in st.session_state.mensagens:
            with st.chat_message(mensagem["role"]):
                st.markdown(mensagem["content"])

        pergunta = st.chat_input(
            "O que você gostaria de saber?"
        )

        if pergunta:
            st.session_state.mensagens.append(
                {"role": "user", "content": pergunta}
            )

            resposta = responder(pergunta)

            st.session_state.mensagens.append(
                {"role": "assistant", "content": resposta}
            )

            st.rerun()

        if st.button("Limpar conversa"):
            st.session_state.mensagens = [
                {
                    "role": "assistant",
                    "content": "Olá novamente! Qual será sua próxima pergunta?"
                }
            ]
            st.rerun()

    # --------------------------------------------------------
    # FUNÇÃO PARA MOSTRAR PERGUNTAS DE CADA CATEGORIA
    # --------------------------------------------------------

    def mostrar_categoria(nome):
        st.subheader(nome)

        st.write(
            "Selecione uma pergunta para consultar "
            "a resposta correspondente."
        )

        itens = [item for item in BANCO if item[0] == nome]

        for indice, item in enumerate(itens):
            categoria, pergunta, palavras, resposta = item

            with st.expander(pergunta):
                st.write(resposta)

    # --------------------------------------------------------
    # ABA 2 - TURISMO
    # --------------------------------------------------------

    with abas[1]:
        st.image(IMAGEM_PARQUE, use_container_width=True)
        mostrar_categoria("Turismo")

    # --------------------------------------------------------
    # ABA 3 - HISTÓRIA
    # --------------------------------------------------------

    with abas[2]:
        st.subheader("A memória da Serra da Capivara")
        st.write(
            "Conheça a importância histórica e cultural "
            "desse patrimônio piauiense."
        )
        mostrar_categoria("História")

    # --------------------------------------------------------
    # ABA 4 - ARQUEOLOGIA
    # --------------------------------------------------------

    with abas[3]:
        st.subheader("Registros de antigas populações")
        st.write(
            "As pinturas rupestres são registros importantes "
            "para o estudo das sociedades humanas do passado."
        )
        mostrar_categoria("Arqueologia")

    # --------------------------------------------------------
    # ABA 5 - NATUREZA
    # --------------------------------------------------------

    with abas[4]:
        st.image(IMAGEM_PARQUE, use_container_width=True)
        st.subheader("A biodiversidade da Caatinga")
        st.write(
            "Descubra as espécies de plantas e animais "
            "que fazem parte desse ambiente."
        )
        mostrar_categoria("Natureza")

    # --------------------------------------------------------
    # ABA 6 - VISITAÇÃO
    # --------------------------------------------------------

    with abas[5]:
        st.subheader("Planeje sua visita")
        st.write(
            "Consulte orientações gerais para organizar "
            "um passeio responsável e seguro."
        )
        mostrar_categoria("Visitação")

    # --------------------------------------------------------
    # RODAPÉ DO CHATBOT
    # --------------------------------------------------------

    st.divider()

    st.caption(
        "CAPIVARABOT | GUIA TURÍSTICO VIRTUAL"
    )

    st.caption(
        "Desenvolvido pelo Professor Daniel e pelos alunos "
        "Felype, David, Laiane e Mariana."
    )

    st.caption("Projeto educativo • Piauí • Brasil")
