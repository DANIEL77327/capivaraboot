
import streamlit as st
import unicodedata
import re

# ============================================================
# 1. CONFIGURAÇÃO DO SITE
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

NOME_PROJETO = "CapivaraBot"

DESCRICAO = (
    "Uma experiência interativa para conhecer a história, "
    "a arqueologia, a natureza e a riqueza cultural do Piauí."
)

COR_TERRA = "#A66B45"
COR_VERDE = "#526B4D"
COR_AREIA = "#D9C5A0"

# ============================================================
# 3. IMAGENS
# ============================================================

IMAGENS = [
    {
        "url": "https://www.viajenaviagem.com/wp-content/uploads/2013/11/parque-abreinterno.jpg.webp",
        "legenda": "Paisagens e formações rochosas da Serra da Capivara."
    },
    {
        "url": "https://www.maladeaventuras.com/wp-content/uploads/2023/01/parque-serra-da-capivara.jpg",
        "legenda": "A beleza natural do Parque Nacional da Serra da Capivara."
    }
]

# ============================================================
# 4. BANCO DE PERGUNTAS E RESPOSTAS
# ============================================================

BANCO_RESPOSTAS = [

    {
        "pergunta": "Como chegar ao Parque Nacional da Serra da Capivara?",
        "palavras": ["como chegar", "chegar ao parque", "transporte", "acesso ao parque"],
        "resposta": "É possível chegar à região por transporte rodoviário ou aéreo, conforme a disponibilidade de voos e conexões. A partir de São Raimundo Nonato, o deslocamento até os acessos do parque pode ser feito por transporte contratado ou veículo próprio, conforme o roteiro."
    },

    {
        "pergunta": "Qual é a distância entre São Raimundo Nonato e o parque?",
        "palavras": ["distancia", "sao raimundo nonato", "quantos km", "perto da cidade"],
        "resposta": "A distância depende da entrada e do atrativo escolhido. O parque possui diferentes acessos e circuitos, por isso é importante verificar o percurso antes de sair."
    },

    {
        "pergunta": "Qual é a melhor época para visitar o parque?",
        "palavras": ["melhor epoca", "quando visitar", "epoca de chuva", "estacao seca"],
        "resposta": "A visita pode acontecer durante todo o ano. O período de chuvas costuma deixar a vegetação mais verde, enquanto a estação seca apresenta paisagens diferentes. A escolha depende da preferência do visitante."
    },

    {
        "pergunta": "Qual é o horário de funcionamento do parque?",
        "palavras": ["horario", "funcionamento", "abre", "fecha", "horario de visita"],
        "resposta": "Os horários de visitação podem variar conforme os circuitos e as condições operacionais. Consulte as informações atualizadas do ICMBio e dos condutores antes de programar o passeio."
    },

    {
        "pergunta": "É necessário agendar a visita?",
        "palavras": ["agendar", "agendamento", "reserva", "marcar visita"],
        "resposta": "É recomendável organizar o passeio antecipadamente e entrar em contato com um condutor cadastrado para verificar disponibilidade, horários e condições dos roteiros."
    },

    {
        "pergunta": "É necessário pagar ingresso para entrar no parque?",
        "palavras": ["ingresso", "pagar", "preco", "valor da entrada", "entrada gratuita"],
        "resposta": "As informações oficiais de visitação do ICMBio indicam entrada gratuita. Entretanto, serviços de condução, transporte e outras atividades contratadas podem ter custos."
    },

    {
        "pergunta": "É obrigatório contratar um guia ou condutor?",
        "palavras": ["guia", "condutor", "guia turistico", "obrigatorio contratar"],
        "resposta": "A visitação deve seguir as regras oficiais do parque, que preveem acompanhamento por condutor cadastrado. Consulte o ICMBio para confirmar as condições aplicáveis ao roteiro escolhido."
    },

    {
        "pergunta": "Quanto tempo dura um passeio no parque?",
        "palavras": ["duracao", "quanto tempo", "tempo de passeio", "horas de passeio"],
        "resposta": "Depende do circuito escolhido. Existem passeios de algumas horas e roteiros que podem ocupar um dia inteiro."
    },

    {
        "pergunta": "Posso visitar o parque em apenas um dia?",
        "palavras": ["um dia", "visitar em um dia", "passeio de um dia"],
        "resposta": "Sim. É possível conhecer alguns atrativos em um dia, mas para explorar diferentes circuitos e sítios arqueológicos é recomendável reservar mais tempo."
    },

    {
        "pergunta": "O parque funciona em feriados e finais de semana?",
        "palavras": ["feriado", "final de semana", "fim de semana", "sabado", "domingo"],
        "resposta": "A visitação depende do calendário e das condições operacionais. Confirme antecipadamente com o ICMBio ou com os responsáveis pela condução turística."
    },

    {
        "pergunta": "É possível visitar o parque por conta própria?",
        "palavras": ["por conta propria", "sozinho", "sem guia", "visitar sozinho"],
        "resposta": "A visita deve respeitar as regras de acompanhamento e os roteiros autorizados. Entre em contato com um condutor cadastrado antes de iniciar o passeio."
    },

    {
        "pergunta": "O que devo levar para visitar o parque?",
        "palavras": ["o que levar", "levar na visita", "protetor solar", "roupas", "agua"],
        "resposta": "Leve água suficiente, protetor solar, chapéu ou boné, roupas confortáveis, calçados adequados para caminhada e lanches, conforme a duração do roteiro."
    },

    {
        "pergunta": "Quais são os principais atrativos do parque?",
        "palavras": ["principais atrativos", "pontos turisticos", "atracoes", "o que visitar", "lugares para visitar"],
        "resposta": "Entre os principais atrativos estão a Pedra Furada, o Boqueirão da Pedra Furada, o Baixão das Andorinhas, os circuitos de sítios arqueológicos, os mirantes e as trilhas."
    },

    {
        "pergunta": "O que é a Pedra Furada?",
        "palavras": ["pedra furada", "formacao rochosa", "cartao postal"],
        "resposta": "É uma impressionante formação rochosa natural com uma abertura que se tornou um dos símbolos mais conhecidos da Serra da Capivara."
    },

    {
        "pergunta": "O que é o Boqueirão da Pedra Furada?",
        "palavras": ["boqueirao", "boqueirao da pedra furada"],
        "resposta": "É um dos sítios arqueológicos mais importantes e conhecidos da região, com pinturas rupestres e registros fundamentais para os estudos sobre a presença humana no continente americano."
    },

    {
        "pergunta": "O que são pinturas rupestres?",
        "palavras": ["pinturas rupestres", "arte rupestre", "desenhos nas pedras", "pinturas antigas"],
        "resposta": "São desenhos e representações produzidos por antigas populações humanas em superfícies rochosas, utilizando pigmentos naturais."
    },

    {
        "pergunta": "Quantos sítios arqueológicos existem no parque?",
        "palavras": ["quantos sitios", "sitios arqueologicos", "quantidade de sitios", "mais de mil"],
        "resposta": "O parque possui mais de mil sítios arqueológicos cadastrados, sendo centenas deles com registros de pinturas rupestres."
    },

    {
        "pergunta": "É possível fotografar as pinturas rupestres?",
        "palavras": ["fotografar pinturas", "tirar fotos", "fotos das pinturas"],
        "resposta": "Em geral, é possível fotografar os registros respeitando as orientações do condutor e as regras de conservação. Não se deve tocar nas pinturas nem utilizar equipamentos ou iluminação que possam causar danos."
    },

    {
        "pergunta": "O que é o Baixão das Andorinhas?",
        "palavras": ["baixao das andorinhas", "andorinhas", "observar aves"],
        "resposta": "É um atrativo natural conhecido por suas formações rochosas e pela observação de aves, especialmente no final da tarde, quando andorinhas e outros pássaros podem ser vistos voando na região."
    },

    {
        "pergunta": "Existem mirantes no parque?",
        "palavras": ["mirantes", "mirante", "vista panoramica"],
        "resposta": "Sim. O parque possui pontos de observação que permitem contemplar as paisagens da Caatinga, os vales e as formações rochosas."
    },

    {
        "pergunta": "Todos os atrativos podem ser visitados no mesmo dia?",
        "palavras": ["todos os atrativos", "mesmo dia", "visitar tudo"],
        "resposta": "Não necessariamente. Os atrativos estão distribuídos em diferentes áreas e circuitos. O ideal é organizar um roteiro com o condutor, considerando distância, duração e dificuldade das caminhadas."
    },

    {
        "pergunta": "O parque possui trilhas para caminhadas?",
        "palavras": ["trilhas", "caminhadas", "trilha no parque"],
        "resposta": "Sim. Existem trilhas com diferentes distâncias e níveis de dificuldade, que permitem conhecer sítios arqueológicos e paisagens naturais."
    },

    {
        "pergunta": "As trilhas são difíceis?",
        "palavras": ["trilhas dificeis", "dificuldade", "nivel de dificuldade"],
        "resposta": "Algumas são leves e outras exigem maior esforço físico. É importante escolher o circuito de acordo com as condições físicas e as orientações do condutor."
    },

    {
        "pergunta": "Crianças podem fazer as trilhas?",
        "palavras": ["criancas", "criancas nas trilhas", "idade para trilha"],
        "resposta": "Sim, desde que o roteiro seja adequado à idade, às condições da criança e às recomendações de segurança."
    },

    {
        "pergunta": "Pessoas idosas podem visitar o parque?",
        "palavras": ["idosos", "pessoas idosas", "terceira idade"],
        "resposta": "Sim. É possível selecionar roteiros com caminhadas mais curtas e acessíveis, conforme as condições de cada visitante."
    },

    {
        "pergunta": "É possível fazer passeios de bicicleta?",
        "palavras": ["bicicleta", "passeio de bicicleta", "ciclismo"],
        "resposta": "A possibilidade depende das regras e dos roteiros autorizados. Consulte a administração do parque e os prestadores de serviços locais antes de planejar essa atividade."
    },

    {
        "pergunta": "Posso fazer piquenique no parque?",
        "palavras": ["piquenique", "lanche", "comer no parque"],
        "resposta": "A alimentação deve respeitar as áreas permitidas e as orientações de visitação. Nunca deixe restos de alimentos ou embalagens no ambiente natural."
    },

    {
        "pergunta": "É possível observar animais silvestres?",
        "palavras": ["animais silvestres", "observar animais", "fauna", "bichos"],
        "resposta": "Sim. O parque abriga diversas espécies da fauna da Caatinga. A observação deve acontecer à distância, sem alimentar, perseguir ou tentar tocar nos animais."
    },

    {
        "pergunta": "Qual é o melhor horário para fotografar as paisagens?",
        "palavras": ["melhor horario fotografar", "fotografar paisagens", "fotos da paisagem"],
        "resposta": "O início da manhã e o final da tarde costumam oferecer iluminação interessante para fotografias. Respeite sempre os horários autorizados de visitação."
    },

    {
        "pergunta": "Existem passeios para contemplar o pôr do sol?",
        "palavras": ["por do sol", "passeio no final da tarde", "contemplar o sol"],
        "resposta": "Alguns roteiros permitem contemplar a paisagem no final da tarde. É necessário verificar com o condutor os locais autorizados e os horários de retorno."
    },

    {
        "pergunta": "É necessário ter preparo físico para conhecer o parque?",
        "palavras": ["preparo fisico", "condicionamento", "esforco fisico"],
        "resposta": "Não para todos os passeios. Existem opções com diferentes níveis de esforço, mas é importante informar ao condutor suas limitações para escolher o roteiro adequado."
    },

    {
        "pergunta": "Onde posso encontrar hospedagem para visitar o parque?",
        "palavras": ["hospedagem", "hotel", "pousada", "onde ficar"],
        "resposta": "São Raimundo Nonato oferece opções de hotéis, pousadas e outras hospedagens. Também existem alternativas em municípios próximos. É recomendável reservar antecipadamente."
    },

    {
        "pergunta": "Existem restaurantes próximos ao parque?",
        "palavras": ["restaurantes", "restaurante", "onde comer", "alimentacao"],
        "resposta": "São Raimundo Nonato possui restaurantes, lanchonetes e estabelecimentos que oferecem refeições regionais e outras opções gastronômicas."
    },

    {
        "pergunta": "Onde posso contratar um condutor turístico?",
        "palavras": ["contratar condutor", "contratar guia", "condutor turistico", "guia cadastrado"],
        "resposta": "Você pode buscar informações junto à associação ou aos serviços de condutores cadastrados, agências de turismo locais e canais oficiais de atendimento do parque."
    },

    {
        "pergunta": "Existe transporte turístico para chegar aos atrativos?",
        "palavras": ["transporte turistico", "transporte para atrativos", "passeios na regiao"],
        "resposta": "Existem prestadores de serviços que oferecem transporte e passeios na região. Consulte as empresas locais para verificar disponibilidade, valores e condições."
    },

    {
        "pergunta": "O parque possui banheiros e pontos de apoio?",
        "palavras": ["banheiros", "pontos de apoio", "estrutura", "infraestrutura"],
        "resposta": "A infraestrutura varia conforme o circuito e o atrativo. Antes de sair, confirme com o condutor onde existem banheiros, pontos de apoio e locais para descanso."
    },

    {
        "pergunta": "Existe sinal de celular e internet dentro do parque?",
        "palavras": ["sinal de celular", "internet", "wifi", "rede de celular"],
        "resposta": "O sinal pode ser limitado ou inexistente em determinados trechos. É recomendável combinar previamente o roteiro, os horários e os pontos de encontro."
    },

    {
        "pergunta": "Existe atendimento de emergência dentro do parque?",
        "palavras": ["emergencia", "atendimento medico", "socorro", "acidente"],
        "resposta": "O visitante deve seguir as orientações do condutor e informar previamente qualquer necessidade especial. Em emergências, deve-se acionar os serviços públicos competentes."
    },

    {
        "pergunta": "Existe algum museu para visitar na região?",
        "palavras": ["museus", "museu na regiao", "museu para visitar"],
        "resposta": "Sim. O Museu do Homem Americano e o Museu da Natureza são importantes atrações culturais e científicas da região."
    },

    {
        "pergunta": "O que posso conhecer no Museu do Homem Americano?",
        "palavras": ["museu do homem americano", "museu do homem", "acervo arqueologico"],
        "resposta": "O museu apresenta informações sobre a presença humana na região, pesquisas arqueológicas, vestígios encontrados e a história das antigas populações."
    },

    {
        "pergunta": "O que posso conhecer no Museu da Natureza?",
        "palavras": ["museu da natureza", "historia da natureza", "evolucao da vida"],
        "resposta": "O museu apresenta a história da natureza e as transformações ambientais do planeta, com exposições sobre a evolução da vida e os acontecimentos que marcaram a região."
    },

    {
        "pergunta": "Existem atrativos com acessibilidade?",
        "palavras": ["acessibilidade", "cadeirante", "mobilidade reduzida", "acessivel"],
        "resposta": "Sim. Existem sítios arqueológicos com estruturas adaptadas para pessoas com mobilidade reduzida. É importante consultar previamente quais atrativos oferecem acessibilidade e quais são as condições de visitação."
    },

    {
        "pergunta": "O que devo fazer em caso de chuva durante o passeio?",
        "palavras": ["chuva", "chovendo", "tempo chuvoso", "chuva durante passeio"],
        "resposta": "Siga imediatamente as orientações do condutor. Dependendo das condições climáticas, algumas trilhas e áreas podem ter a visitação suspensa por segurança."
    },

    {
        "pergunta": "Posso levar animais de estimação para o parque?",
        "palavras": ["animais de estimacao", "cachorro", "gato", "pet"],
        "resposta": "A entrada de animais domésticos está sujeita às regras da unidade de conservação. Consulte previamente o ICMBio antes de levar seu animal."
    },

    {
        "pergunta": "É permitido fumar dentro do parque?",
        "palavras": ["fumar", "cigarro", "permitido fumar"],
        "resposta": "O visitante deve respeitar as restrições ambientais e as orientações da administração, especialmente devido ao risco de incêndios na vegetação da Caatinga."
    },

    {
        "pergunta": "Posso retirar pedras ou pedaços de rochas como lembrança?",
        "palavras": ["retirar pedras", "levar pedras", "pedras como lembranca", "retirar rochas"],
        "resposta": "Não. É proibido retirar materiais arqueológicos, pedras, fósseis, plantas ou qualquer elemento natural do parque."
    },

    {
        "pergunta": "O que fazer se encontrar um animal silvestre durante a visita?",
        "palavras": ["encontrar animal", "animal silvestre", "animal durante visita"],
        "resposta": "Mantenha distância, não tente alimentar ou tocar no animal e avise o condutor responsável."
    },

    {
        "pergunta": "Como posso ajudar na preservação das pinturas rupestres?",
        "palavras": ["preservar pinturas", "proteger pinturas", "conservar pinturas"],
        "resposta": "Não toque nas pinturas, não escreva nas rochas, não utilize produtos químicos e respeite as áreas delimitadas para visitação."
    },

    {
        "pergunta": "O que acontece se um visitante danificar um sítio arqueológico?",
        "palavras": ["danificar sitio", "danificar pinturas", "destruir patrimonio", "danos arqueologicos"],
        "resposta": "Danificar o patrimônio arqueológico é uma infração e pode gerar responsabilização conforme a legislação brasileira. As pinturas e os sítios são bens que precisam ser protegidos."
    },

    {
        "pergunta": "Como o visitante pode contribuir com o turismo sustentável?",
        "palavras": ["turismo sustentavel", "contribuir", "ajudar comunidades", "turismo responsavel"],
        "resposta": "Contratando serviços locais, valorizando a cultura regional, respeitando as comunidades, evitando desperdícios e preservando o meio ambiente."
    },

    {
        "pergunta": "Onde fica a Serra da Capivara?",
        "palavras": ["onde fica", "localizacao", "qual cidade", "em que estado"],
        "resposta": "O Parque Nacional da Serra da Capivara está localizado no sudeste do estado do Piauí. Sua área abrange partes dos municípios de São Raimundo Nonato, Coronel José Dias, João Costa e Canto do Buriti."
    },

    {
        "pergunta": "Qual é a importância da Serra da Capivara?",
        "palavras": ["importancia", "unesco", "patrimonio mundial", "reconhecimento"],
        "resposta": "A Serra da Capivara possui grande importância histórica e científica por preservar sítios arqueológicos e pinturas rupestres. Em 1991, o Parque Nacional foi inscrito na Lista do Patrimônio Mundial da UNESCO."
    },

    {
        "pergunta": "Quais animais vivem na Serra da Capivara?",
        "palavras": ["animais da caatinga", "fauna", "quais animais", "bichos da serra"],
        "resposta": "A região abriga animais adaptados ao ambiente da Caatinga, como tatu-bola, veado-catingueiro, macaco-prego e diversas espécies de aves. A preservação desses animais é importante para o equilíbrio ambiental."
    },

    {
        "pergunta": "Quais plantas existem na Serra da Capivara?",
        "palavras": ["plantas", "flora", "vegetacao", "mandacaru", "xique xique"],
        "resposta": "A vegetação da região é característica da Caatinga. Entre as espécies encontradas estão mandacaru, xique-xique, bromélias e diferentes arbustos adaptados ao clima semiárido."
    },

    {
        "pergunta": "O que é a Caatinga?",
        "palavras": ["caatinga", "bioma", "clima da regiao"],
        "resposta": "A Caatinga é um bioma exclusivamente brasileiro, predominante em áreas do Nordeste. Sua vegetação apresenta adaptações aos períodos de pouca chuva, com plantas resistentes ao clima semiárido."
    },

    {
        "pergunta": "Qual é a história da criação do parque?",
        "palavras": ["historia do parque", "quem descobriu", "criado o parque", "criacao do parque"],
        "resposta": "O Parque Nacional da Serra da Capivara foi criado em 1979. A arqueóloga Niède Guidon teve papel fundamental nas pesquisas, na defesa e na valorização do patrimônio arqueológico da região."
    },

    {
        "pergunta": "Qual é o tamanho do parque?",
        "palavras": ["tamanho", "extensao", "area do parque", "hectares"],
        "resposta": "O Parque Nacional da Serra da Capivara possui aproximadamente 130 mil hectares de área protegida. Seu território reúne paisagens, sítios arqueológicos e diferentes ambientes naturais."
    },

    {
        "pergunta": "Quais são as comidas típicas da região?",
        "palavras": ["comida tipica", "culinaria", "gastronomia", "o que comer", "pratos regionais"],
        "resposta": "A culinária regional apresenta pratos tradicionais como carne de sol, galinha caipira e paçoca, além de preparações que valorizam ingredientes e costumes do sertão piauiense."
    }
]

# ============================================================
# 5. NORMALIZAÇÃO DAS PERGUNTAS
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


# ============================================================
# 6. SISTEMA DE RESPOSTAS
# ============================================================

def responder(pergunta):

    texto = normalizar(pergunta)

    if not texto:
        return "Digite uma pergunta para começar nossa conversa."

    cumprimentos = [
        "oi",
        "ola",
        "bom dia",
        "boa tarde",
        "boa noite",
        "tudo bem"
    ]

    if texto in cumprimentos:
        return (
            "Olá! Seja bem-vindo ao CapivaraBot! 🐾\n\n"
            "Estou pronto para apresentar a Serra da Capivara. "
            "Pode perguntar sobre turismo, história, pinturas "
            "rupestres, animais, natureza e muito mais!"
        )

    melhor_resposta = None
    maior_pontuacao = 0

    palavras_pergunta = set(texto.split())

    for item in BANCO_RESPOSTAS:

        pontuacao = 0

        for termo in item["palavras"]:

            termo_normalizado = normalizar(termo)

            if termo_normalizado in texto:
                pontuacao += 10 + len(termo_normalizado.split())

            else:
                palavras_termo = set(termo_normalizado.split())

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
        "Tente reformular ou perguntar sobre os atrativos turísticos, "
        "as pinturas rupestres, a fauna, a flora, a hospedagem, "
        "a visitação ou a história da Serra da Capivara."
    )


# ============================================================
# 7. HISTÓRICO DA CONVERSA
# ============================================================

if "mensagens" not in st.session_state:

    st.session_state.mensagens = [
        {
            "role": "assistant",
            "content": (
                "Olá! Eu sou o CapivaraBot. 🐾\n\n"
                "Seu guia virtual pela Serra da Capivara. "
                "Escreva sua pergunta e descubra as riquezas "
                "históricas, naturais e culturais do Piauí!"
            )
        }
    ]


# ============================================================
# 8. ABERTURA DO SITE
# ============================================================

st.write("")
st.write("")

coluna_esquerda, coluna_centro, coluna_direita = st.columns(
    [1, 4, 1]
)

with coluna_centro:

    st.title("🐾 CapivaraBot")

    st.subheader(
        "Seu guia virtual pela Serra da Capivara"
    )

    st.write(DESCRICAO)

    st.write("")

    st.caption(
        "🪨 ARQUEOLOGIA   •   🌵 NATUREZA   •   "
        "🐾 BIODIVERSIDADE   •   🏛️ CULTURA"
    )

st.write("")
st.divider()


# ============================================================
# 9. APRESENTAÇÃO DO PATRIMÔNIO
# ============================================================

st.write("")
st.header("Uma história desenhada nas rochas")

st.write(
    "No sudeste do Piauí, entre paredões de pedra, cânions "
    "e paisagens da Caatinga, encontra-se um dos mais "
    "importantes patrimônios arqueológicos do Brasil."
)

st.write(
    "A Serra da Capivara reúne registros de antigas populações "
    "humanas, pinturas rupestres, espécies da fauna e flora "
    "e paisagens naturais que encantam visitantes."
)

st.write("")

imagem1, imagem2 = st.columns(2, gap="large")

with imagem1:

    st.image(
        IMAGENS[0]["url"],
        use_container_width=True,
        caption=IMAGENS[0]["legenda"]
    )

with imagem2:

    st.image(
        IMAGENS[1]["url"],
        use_container_width=True,
        caption=IMAGENS[1]["legenda"]
    )

st.write("")
st.divider()


# ============================================================
# 10. IDENTIDADE CULTURAL E NATURAL
# ============================================================

st.header("Os detalhes que tornam esse lugar único")

col1, col2, col3 = st.columns(3, gap="large")

with col1:

    with st.container(border=True):

        st.subheader("🪨 Arte rupestre")

        st.write(
            "As pinturas nas paredes rochosas revelam "
            "representações de figuras humanas, animais, "
            "danças, caçadas e atividades de antigas populações."
        )

        st.caption("Memória registrada nas rochas.")

with col2:

    with st.container(border=True):

        st.subheader("🌵 Vegetação da Caatinga")

        st.write(
            "Mandacarus, xique-xiques, bromélias e outras "
            "espécies adaptadas ao clima semiárido compõem "
            "a paisagem da região."
        )

        st.caption("A resistência e a beleza do sertão.")

with col3:

    with st.container(border=True):

        st.subheader("🦊 Animais silvestres")

        st.write(
            "A região abriga espécies como tatu-bola, "
            "veado-catingueiro, macaco-prego e diversas aves "
            "que fazem parte da biodiversidade local."
        )

        st.caption("Vida e biodiversidade na Caatinga.")

st.write("")
st.divider()


# ============================================================
# 11. EXPERIÊNCIA DE CONHECIMENTO
# ============================================================

st.header("Conheça, descubra e preserve")

st.write(
    "A Serra da Capivara não é apenas um destino turístico. "
    "É um espaço de conhecimento, pesquisa, preservação "
    "ambiental e valorização da história humana."
)

coluna1, coluna2 = st.columns(2, gap="large")

with coluna1:

    with st.container(border=True):

        st.subheader("🎨 Um patrimônio arqueológico")

        st.write(
            "As pinturas rupestres representam uma importante "
            "fonte de conhecimento sobre as antigas populações "
            "humanas. Cada registro contribui para a compreensão "
            "da história e das formas de expressão do passado."
        )

with coluna2:

    with st.container(border=True):

        st.subheader("🐾 Um ambiente que precisa de proteção")

        st.write(
            "A preservação da fauna, da flora e dos sítios "
            "arqueológicos depende de atitudes responsáveis. "
            "Conhecer também significa respeitar e proteger."
        )

st.write("")
st.divider()


# ============================================================
# 12. CHATBOT
# ============================================================

st.write("")
st.header("Converse com o CapivaraBot")

st.write(
    "Tem curiosidade sobre a Serra da Capivara? "
    "Digite sua pergunta no campo abaixo. Nosso guia virtual "
    "vai apresentar as informações disponíveis."
)

st.write("")

with st.container(border=True):

    st.subheader("🐾 Atendimento virtual")

    st.caption(
        "Faça sua pergunta e explore o patrimônio piauiense."
    )

    for mensagem in st.session_state.mensagens:

        with st.chat_message(mensagem["role"]):

            st.markdown(mensagem["content"])


# Campo único para inserir perguntas

pergunta = st.chat_input(
    "Digite sua pergunta sobre a Serra da Capivara..."
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


# ============================================================
# 13. LIMPAR CONVERSA
# ============================================================

st.write("")

if st.button(
    "🗑️ Limpar histórico da conversa",
    use_container_width=False
):

    st.session_state.mensagens = [
        {
            "role": "assistant",
            "content": (
                "Olá novamente! 🐾\n\n"
                "Estou pronto para responder às suas perguntas "
                "sobre a Serra da Capivara."
            )
        }
    ]

    st.rerun()


# ============================================================
# 14. RODAPÉ INSTITUCIONAL
# ============================================================

st.write("")
st.divider()
st.write("")

rodape1, rodape2, rodape3 = st.columns([1, 3, 1])

with rodape2:

    st.title("🐾 CapivaraBot")

    st.caption(
        "CONHECIMENTO • TECNOLOGIA • PATRIMÔNIO"
    )

    st.write(
        "Conhecimento, inovação e valorização do "
        "patrimônio piauiense."
    )

    st.caption(
        "Projeto desenvolvido pelo Professor Daniel "
        "e pelos alunos Felype, David, Laiane e Mariana."
    )

    st.caption(
        "Projeto educativo de turismo e divulgação cultural."
    )

    st.caption("Piauí • Brasil")


# ============================================================
# FIM DO PROJETO
# ============================================================
