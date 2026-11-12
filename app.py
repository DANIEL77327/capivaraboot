import streamlit as st
import unicodedata
import re
import os
from openai import OpenAI

# ============================================================
# 1. CONFIGURACAO
# ============================================================

st.set_page_config(
    page_title="CapivaraBot | Serra da Capivara",
    page_icon="🐾",
    layout="wide",
    initial_sidebar_state="collapsed"
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
    "capivaras": "https://commons.wikimedia.org/wiki/Special:FilePath/Capivaras_na_Serra_da_Capivara.jpg",
    "caatinga": "https://commons.wikimedia.org/wiki/Special:FilePath/Bioma_caatinga_serra_da_capivara.jpg",
    "flora": "https://commons.wikimedia.org/wiki/Special:FilePath/Flora_do_Parque_Nacional_Serra_da_Capivara_%280553%29.jpg"
}

# ============================================================
# 3. ESTILO VISUAL
# ============================================================

st.markdown("""
<style>
:root {
    --terra: #6d2d16;
    --terra-clara: #a64f25;
    --laranja: #e98232;
    --dourado: #f2b968;
    --areia: #f6e6ce;
    --marrom: #29140d;
}
.stApp {
    background: linear-gradient(145deg, #21120d, #3c1d10, #24140e);
    color: #fff0dc;
}
.block-container {
    max-width: 1280px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}
h1, h2, h3, h4, p, label { color: #fff0dc !important; }
h1 { font-weight: 900 !important; letter-spacing: -1.5px; }
h2 { color: #f2b968 !important; }
h3 { color: #f5c98d !important; }
[data-testid="stCaptionContainer"] { color: #d9b997; }

/* CAPA PRINCIPAL */
.st-key-hero {
    min-height: 590px;
    padding: 55px 35px;
    border-radius: 25px;
    border: 1px solid rgba(255, 190, 112, 0.65);
    background:
        linear-gradient(90deg, rgba(40, 13, 4, 0.35),
        rgba(40, 13, 4, 0.75), rgba(40, 13, 4, 0.28)),
        url("https://www.viajenaviagem.com/wp-content/uploads/2013/11/parque-abreinterno.jpg.webp");
    background-size: cover;
    background-position: center;
    box-shadow: 0 20px 55px rgba(0,0,0,0.45);
    text-align: center;
}
.st-key-hero h1 {
    font-size: 4.5rem !important;
    color: #fff0d7 !important;
    text-shadow: 3px 4px 15px #160700;
}
.st-key-hero h2 {
    display: inline-block;
    background: rgba(53, 22, 8, 0.78);
    border: 2px solid #e98232;
    border-radius: 40px;
    padding: 10px 25px;
    color: #ffe2bd !important;
    font-size: 1.4rem !important;
}
.st-key-hero p {
    color: #fff0dc !important;
    font-size: 1.1rem;
    text-shadow: 2px 2px 8px #1b0800;
}

/* BOTOES */
.stButton > button {
    background: linear-gradient(135deg, #ed9a45, #a94a20);
    color: white !important;
    border: 1px solid #ffc47c;
    border-radius: 30px;
    padding: 11px 20px;
    font-weight: 800;
    transition: 0.2s;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #ffb65d, #c65b27);
    border-color: #ffe1b5;
    transform: translateY(-2px);
}

/* ABAS */
.stTabs [data-baseweb="tab-list"] {
    background: #482416;
    border: 1px solid #a75a30;
    border-radius: 17px;
    padding: 8px;
    gap: 5px;
}
.stTabs [data-baseweb="tab"] {
    color: #f8d9b7;
    font-weight: 700;
    border-radius: 12px;
}
.stTabs [aria-selected="true"] {
    background: #bd5b27 !important;
    color: white !important;
}

/* PERGUNTAS */
div[data-testid="stExpander"] {
    background: rgba(91, 43, 22, 0.75);
    border: 1px solid #a85e36;
    border-radius: 14px;
    margin-bottom: 8px;
}
div[data-testid="stExpander"] summary {
    color: #ffe0b7;
    font-weight: 700;
}

/* CARTOES */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(105, 49, 23, 0.45);
    border: 1px solid #a65a30;
    border-radius: 18px;
}

/* CHAT */
[data-testid="stChatMessage"] {
    background: rgba(111, 55, 29, 0.72);
    border: 1px solid rgba(235, 157, 88, 0.5);
    border-radius: 18px;
    padding: 12px;
    margin-bottom: 12px;
}
.stChatInput textarea {
    background: #fff0dc !important;
    color: #35180e !important;
    border-radius: 16px !important;
}

/* IMAGENS */
[data-testid="stImage"] img {
    border-radius: 17px;
    border: 1px solid rgba(242, 185, 104, 0.65);
}
hr { border-color: #a65a30 !important; }
footer { visibility: hidden; }

/* Indicador discreto da IA */
.ia-info {
    color: #f2b968;
    font-size: 0.85rem;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# 4. BANCO DE PERGUNTAS E RESPOSTAS
# ============================================================

BANCO = [
("Turismo", "Como chegar ao Parque Nacional da Serra da Capivara?",
 ["como chegar", "chegar ao parque", "transporte rodoviario", "acesso ao parque"],
 "É possível chegar à região por transporte rodoviário ou aéreo, conforme a disponibilidade de voos e conexões. A partir de São Raimundo Nonato, o deslocamento até os acessos do parque pode ser feito por transporte contratado ou veículo próprio, conforme o roteiro."),
("Turismo", "Qual é a distância entre São Raimundo Nonato e o parque?",
 ["distancia entre", "quantos km", "distancia de sao raimundo"],
 "A distância depende da entrada e do atrativo escolhido. O parque possui diferentes acessos e circuitos, por isso é importante verificar o percurso antes de sair."),
("Turismo", "Qual é a melhor época para visitar o parque?",
 ["melhor epoca", "quando visitar", "epoca de chuva", "estacao seca"],
 "A visita pode acontecer durante todo o ano. O período de chuvas costuma deixar a vegetação mais verde, enquanto a estação seca apresenta paisagens diferentes. A escolha depende da preferência do visitante."),
("Turismo", "Qual é o horário de funcionamento do parque?",
 ["horario de funcionamento", "horario de visita", "abre", "fecha"],
 "Os horários de visitação podem variar conforme os circuitos e as condições operacionais. Consulte as informações atualizadas do ICMBio e dos condutores antes de programar o passeio."),
("Turismo", "É necessário agendar a visita?",
 ["agendar", "agendamento", "reserva", "marcar visita"],
 "É recomendável organizar o passeio antecipadamente e entrar em contato com um condutor cadastrado para verificar disponibilidade, horários e condições dos roteiros."),
("Turismo", "É necessário pagar ingresso para entrar no parque?",
 ["ingresso", "pagar entrada", "preco da entrada", "valor do ingresso"],
 "As informações oficiais de visitação do ICMBio indicam entrada gratuita. Entretanto, serviços de condução, transporte e outras atividades contratadas podem ter custos."),
("Turismo", "É obrigatório contratar um guia ou condutor?",
 ["guia", "condutor", "guia turistico", "obrigatorio contratar"],
 "A visitação deve seguir as regras oficiais do parque, que preveem acompanhamento por condutor cadastrado. Consulte o ICMBio para confirmar as condições aplicáveis ao roteiro escolhido."),
("Turismo", "Quanto tempo dura um passeio no parque?",
 ["duracao do passeio", "quanto tempo dura", "tempo de passeio"],
 "Depende do circuito escolhido. Existem passeios de algumas horas e roteiros que podem ocupar um dia inteiro."),
("Turismo", "Posso visitar o parque em apenas um dia?",
 ["visitar em um dia", "um dia no parque", "passeio de um dia"],
 "Sim. É possível conhecer alguns atrativos em um dia, mas para explorar diferentes circuitos e sítios arqueológicos é recomendável reservar mais tempo."),
("Turismo", "O parque funciona em feriados e finais de semana?",
 ["feriados", "final de semana", "fim de semana", "sabado", "domingo"],
 "A visitação depende do calendário e das condições operacionais. Confirme antecipadamente com o ICMBio ou com os responsáveis pela condução turística."),
("Turismo", "É possível visitar o parque por conta própria?",
 ["por conta propria", "sem guia", "visitar sozinho"],
 "A visita deve respeitar as regras de acompanhamento e os roteiros autorizados. Entre em contato com um condutor cadastrado antes de iniciar o passeio."),
("Turismo", "Onde posso encontrar hospedagem?",
 ["hospedagem", "hotel", "pousada", "onde ficar"],
 "São Raimundo Nonato oferece opções de hotéis, pousadas e outras hospedagens. Também existem alternativas em municípios próximos. É recomendável reservar antecipadamente."),
("Turismo", "Existem restaurantes próximos ao parque?",
 ["restaurantes", "restaurante", "onde comer", "alimentacao"],
 "São Raimundo Nonato possui restaurantes, lanchonetes e estabelecimentos que oferecem refeições regionais e outras opções gastronômicas."),
("Turismo", "Onde posso contratar um condutor turístico?",
 ["contratar condutor", "condutor turistico", "guia cadastrado"],
 "Você pode buscar informações junto à associação ou aos serviços de condutores cadastrados, agências de turismo locais e canais oficiais de atendimento do parque."),
("Turismo", "Existe transporte turístico para chegar aos atrativos?",
 ["transporte turistico", "transporte para atrativos", "empresas de transporte"],
 "Existem prestadores de serviços que oferecem transporte e passeios na região. Consulte as empresas locais para verificar disponibilidade, valores e condições."),
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
 ["por do sol", "contemplar o sol", "final da tarde"],
 "Alguns roteiros permitem contemplar a paisagem no final da tarde. É necessário verificar com o condutor os locais autorizados e os horários de retorno."),
("Turismo", "Quais são as comidas típicas da região?",
 ["comida tipica", "culinaria", "gastronomia", "pratos regionais"],
 "A culinária regional apresenta pratos tradicionais como carne de sol, galinha caipira e paçoca, além de preparações que valorizam ingredientes e costumes do sertão piauiense."),
("Turismo", "Existe algum museu para visitar na região?",
 ["museus", "museu na regiao", "museu para visitar"],
 "Sim. O Museu do Homem Americano e o Museu da Natureza são importantes atrações culturais e científicas da região."),
("Turismo", "O que posso conhecer no Museu do Homem Americano?",
 ["museu do homem americano", "museu do homem", "acervo arqueologico"],
 "O museu apresenta informações sobre a presença humana na região, pesquisas arqueológicas, vestígios encontrados e a história das antigas populações."),
("Turismo", "O que posso conhecer no Museu da Natureza?",
 ["museu da natureza", "historia da natureza", "evolucao da vida"],
 "O museu apresenta a história da natureza e as transformações ambientais do planeta, com exposições sobre a evolução da vida e os acontecimentos que marcaram a região."),
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
("Natureza", "Como o visitante pode contribuir com o turismo sustentável?",
 ["turismo sustentavel", "contribuir com turismo", "turismo responsavel"],
 "Contratando serviços locais, valorizando a cultura regional, respeitando as comunidades, evitando desperdícios e preservando o meio ambiente."),
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
("Visitação", "Posso levar animais de estimação para o parque?",
 ["animais de estimacao", "cachorro", "gato", "pet"],
 "A entrada de animais domésticos está sujeita às regras da unidade de conservação. Consulte previamente o ICMBio antes de levar seu animal."),
("Visitação", "É permitido fumar dentro do parque?",
 ["fumar", "cigarro", "permitido fumar"],
 "O visitante deve respeitar as restrições ambientais e as orientações da administração, especialmente devido ao risco de incêndios na vegetação da Caatinga."),
("Visitação", "Posso retirar pedras ou pedaços de rochas como lembrança?",
 ["retirar pedras", "levar pedras", "pedras como lembranca", "retirar rochas"],
 "Não. É proibido retirar materiais arqueológicos, pedras, fósseis, plantas ou qualquer elemento natural do parque."),
("Visitação", "O que fazer se encontrar um animal silvestre durante a visita?",
 ["encontrar um animal", "animal silvestre durante", "animal na trilha"],
 "Mantenha distância, não tente alimentar ou tocar no animal e avise o condutor responsável."),
("Visitação", "Como posso ajudar a preservar o parque?",
 ["preservar o parque", "proteger o parque", "como ajudar na preservacao"],
 "Não deixe lixo, respeite as trilhas, não retire elementos naturais e siga as orientações dos condutores. Pequenas atitudes ajudam a conservar esse patrimônio para as próximas gerações.")
]

# ============================================================
# 5. FUNCOES DO CHATBOT E DA INTELIGENCIA ARTIFICIAL
# ============================================================

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


def responder(pergunta):
    texto = normalizar(pergunta)

    if not texto:
        return "Escreva uma pergunta para começar."

    if texto in ["oi", "ola", "bom dia", "boa tarde", "boa noite"]:
        return (
            "Olá! Seja bem-vindo ao CapivaraBot! 🐾 "
            "Estou aqui para ajudar você a conhecer a Serra da Capivara. "
            "O que gostaria de descobrir?"
        )

    melhor_resposta = None
    maior_pontuacao = 0

    for categoria, titulo, palavras, resposta in BANCO:
        pontuacao = 0
        for termo in palavras:
            termo_normalizado = normalizar(termo)
            if termo_normalizado in texto:
                pontuacao = max(
                    pontuacao,
                    10 + len(termo_normalizado.split())
                )

        if pontuacao > maior_pontuacao:
            maior_pontuacao = pontuacao
            melhor_resposta = resposta

    if melhor_resposta:
        return melhor_resposta

    return (
        "Ainda não encontrei uma resposta adequada para essa pergunta. "
        "Experimente reformular ou escolha uma das categorias para "
        "explorar os assuntos disponíveis."
    )


def obter_cliente_ia():
    """Lê a chave com segurança dos Secrets ou variável de ambiente."""
    chave = None

    try:
        chave = st.secrets.get("OPENAI_API_KEY")
    except Exception:
        chave = None

    if not chave:
        chave = os.getenv("OPENAI_API_KEY")

    if not chave:
        return None

    return OpenAI(api_key=chave)


def responder_com_ia():
    """
    Usa a conversa atual, incluindo a pergunta recém-adicionada,
    e o banco do projeto como referência.
    """
    cliente = obter_cliente_ia()

    if cliente is None:
        pergunta = st.session_state.mensagens[-1]["content"]
        return responder(pergunta), False

    base_conhecimento = "\n\n".join(
        [
            f"Categoria: {categoria}\n"
            f"Pergunta: {titulo}\n"
            f"Resposta de referência: {resposta}"
            for categoria, titulo, palavras, resposta in BANCO
        ]
    )

    instrucoes = f"""
Você é o CapivaraBot, um guia virtual educativo e turístico
especializado no Parque Nacional da Serra da Capivara, no Piauí.

PERSONALIDADE:
- Seja acolhedor, educado, claro e interessante.
- Responda em português brasileiro.
- Use linguagem simples, natural e correta.
- Seja objetivo, mas explique quando necessário.
- Use emojis com moderação.

OBJETIVO:
Ajudar visitantes e estudantes a conhecer a Serra da Capivara,
sua história, arqueologia, pinturas rupestres, natureza,
turismo, cultura e orientações de visitação.

REGRAS DE CONFIABILIDADE:
- Use o banco de conhecimento abaixo como referência do projeto.
- Não invente preços, horários, telefones, regras, rotas ou dados oficiais.
- Se não souber algo, diga claramente que não tem certeza.
- Informações operacionais podem mudar. Oriente a confirmar com o
  ICMBio ou com um condutor cadastrado.
- Não apresente uma suposição como informação oficial.
- Se a pergunta não tiver relação com a Serra da Capivara, responda
  brevemente e convide a pessoa a conhecer o tema do projeto.

PRESERVAÇÃO:
- Oriente a respeitar as trilhas e as áreas autorizadas.
- Nunca recomende tocar nas pinturas rupestres.
- Nunca recomende retirar pedras, fósseis, plantas ou outros elementos.
- Oriente a observar animais à distância, sem alimentar ou perseguir.

BANCO DE CONHECIMENTO DO PROJETO:
{base_conhecimento}
"""

    # O histórico já contém a pergunta atual.
    
    historico = []

    for mensagem in st.session_state.mensagens[-12:]:
        if mensagem["role"] in ("user", "assistant"):
            historico.append({
                "role": mensagem["role"],
                "content": mensagem["content"]
            })



    try:
        resposta = cliente.responses.create(
            model="gpt-5.5",
            instructions=instrucoes,
            input=historico
        )

        texto = resposta.output_text.strip()

        if texto:
            return texto, True

        return "Não consegui formular uma resposta agora. Tente novamente.", True

   st.exception(erro)
        return "Erro ao conectar com a inteligência artificial.", False



        )

# ============================================================
# 6. ESTADO DO SITE
# ============================================================

if "pagina" not in st.session_state:
    st.session_state.pagina = "inicio"

if "mensagens" not in st.session_state:
    st.session_state.mensagens = [
        {
            "role": "assistant",
            "content": (
                "Olá! Eu sou o CapivaraBot! 🐾\n\n"
                "Estou pronto para acompanhar você nessa viagem "
                "pela história, natureza e cultura da Serra da Capivara."
            )
        }
    ]

# ============================================================
# 7. TELA INICIAL
# ============================================================

if st.session_state.pagina == "inicio":

    with st.container(key="hero"):
        st.write("")
        st.write("")
        st.markdown("🏛️  TURISMO   •   HISTÓRIA   •   ARQUEOLOGIA   •   CULTURA")
        st.write("")
        st.write("")
        st.title("🐾 CapivaraBot")
        st.subheader("Seu guia virtual pela Serra da Capivara")
        st.write(
            "Uma experiência interativa para conhecer a história, "
            "a arqueologia, a natureza e a riqueza cultural do Piauí."
        )
        st.write("")
        st.markdown("🦎   🌵   🐾   🪨   🦅")
        st.write("")
        st.write("")

        if st.button(
            "⌄  COMEÇAR A EXPLORAR",
            use_container_width=True,
            type="primary"
        ):
            st.session_state.pagina = "chatbot"
            st.rerun()

        st.write("")
        st.write("")

    st.write("")
    st.write("")
    st.markdown("## Uma terra onde a história está nas rochas")
    st.write(
        "Entre paredões de arenito, pinturas rupestres e paisagens "
        "da Caatinga, a Serra da Capivara guarda registros de antigas "
        "populações e uma biodiversidade marcante."
    )
    st.write("")

    galeria1, galeria2 = st.columns([1.3, 1], gap="large")
    with galeria1:
        st.image(
            IMAGENS["pedra"],
            use_container_width=True,
            caption="Pedra Furada — um dos símbolos da região."
        )
    with galeria2:
        st.image(
            IMAGENS["pinturas"],
            use_container_width=True,
            caption="Pinturas rupestres preservadas nas rochas."
        )

    st.write("")
    st.markdown("## Uma paisagem cheia de vida")
    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        st.image(IMAGENS["capivaras"], use_container_width=True,
                 caption="Fauna da Serra da Capivara")
        st.markdown("**Vida selvagem**")
        st.caption("Animais que fazem parte da riqueza natural da região.")

    with col2:
        st.image(IMAGENS["caatinga"], use_container_width=True,
                 caption="Paisagem da Caatinga")
        st.markdown("**Natureza do sertão**")
        st.caption("Um bioma de formas, cores e adaptações.")

    with col3:
        st.image(IMAGENS["andorinhas"], use_container_width=True,
                 caption="Baixão das Andorinhas")
        st.markdown("**Paisagens impressionantes**")
        st.caption("Vales, paredões e cenários naturais.")

    st.write("")
    st.divider()
    st.markdown("## Escolha o que deseja descobrir")
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("### 🧭")
        st.markdown("**Turismo**")
        st.caption("Atrativos e roteiros.")
    with c2:
        st.markdown("### 📜")
        st.markdown("**História**")
        st.caption("Memória e patrimônio.")
    with c3:
        st.markdown("### 🎨")
        st.markdown("**Arqueologia**")
        st.caption("Pinturas e sítios.")
    with c4:
        st.markdown("### 🌵")
        st.markdown("**Natureza**")
        st.caption("Fauna e flora.")

    st.write("")
    if st.button("🐾 ACESSAR O GUIA VIRTUAL", use_container_width=True):
        st.session_state.pagina = "chatbot"
        st.rerun()

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
        "Escolha uma categoria para explorar informações "
        "ou converse diretamente com o CapivaraBot."
    )

    abas = st.tabs([
        "💬 Atendimento",
        "🧭 Turismo",
        "📜 História",
        "🎨 Arqueologia",
        "🌵 Natureza",
        "🥾 Visitação",
        "🖼️ Galeria"
    ])

    # ATENDIMENTO
    with abas[0]:
        st.subheader("Converse com o CapivaraBot")
        st.write(
            "Digite sua dúvida no campo abaixo. "
            "Nosso guia virtual vai ajudar você."
        )

        cliente_disponivel = obter_cliente_ia() is not None
        if cliente_disponivel:
            st.markdown(
                '<p class="ia-info">✦ Assistente com inteligência artificial ativada</p>',
                unsafe_allow_html=True
            )
        else:
            st.info(
                "A IA ainda não foi configurada. O banco de respostas "
                "continua funcionando normalmente."
            )

        for mensagem in st.session_state.mensagens:
            with st.chat_message(mensagem["role"]):
                st.markdown(mensagem["content"])

        pergunta = st.chat_input("Ex.: Como chegar ao Parque Nacional?")

        if pergunta:
            st.session_state.mensagens.append({
                "role": "user",
                "content": pergunta
            })

            with st.spinner("O CapivaraBot está preparando sua resposta..."):
                resposta, usou_ia = responder_com_ia()

            st.session_state.mensagens.append({
                "role": "assistant",
                "content": resposta
            })
            st.rerun()

        if st.button("🗑️ Limpar conversa"):
            st.session_state.mensagens = [
                {
                    "role": "assistant",
                    "content": "Olá novamente! Qual será sua próxima pergunta?"
                }
            ]
            st.rerun()

    # FUNCAO PARA AS ABAS DE CONTEUDO
    def mostrar_categoria(nome):
        itens = [item for item in BANCO if item[0] == nome]
        st.write("Selecione uma pergunta para conhecer a resposta.")
        for categoria, titulo, palavras, resposta in itens:
            with st.expander(titulo):
                st.write(resposta)

    # TURISMO
    with abas[1]:
        st.subheader("🧭 Descubra os caminhos da Serra")
        st.image(
            IMAGENS["paisagem"],
            use_container_width=True,
            caption="Paisagens do Parque Nacional da Serra da Capivara."
        )
        mostrar_categoria("Turismo")

    # HISTORIA
    with abas[2]:
        st.subheader("📜 Um patrimônio que conta histórias")
        st.image(
            IMAGENS["pedra"],
            use_container_width=True,
            caption="Formações rochosas da Serra da Capivara."
        )
        st.write(
            "A região reúne importantes registros arqueológicos "
            "e paisagens que ajudam a compreender a história "
            "e a ocupação humana do território."
        )
        mostrar_categoria("História")

    # ARQUEOLOGIA
    with abas[3]:
        st.subheader("🎨 A arte que atravessou o tempo")
        st.image(
            IMAGENS["pinturas"],
            use_container_width=True,
            caption="Registros de arte rupestre da região."
        )
        st.write(
            "As pinturas rupestres são registros visuais que "
            "revelam aspectos das atividades, representações "
            "e expressões de antigas populações humanas."
        )
        mostrar_categoria("Arqueologia")

    # NATUREZA
    with abas[4]:
        st.subheader("🌵 A vida na Caatinga")
        natureza1, natureza2 = st.columns(2, gap="large")
        with natureza1:
            st.image(
                IMAGENS["capivaras"],
                use_container_width=True,
                caption="Fauna da região."
            )
        with natureza2:
            st.image(
                IMAGENS["flora"],
                use_container_width=True,
                caption="Vegetação da Caatinga."
            )
        mostrar_categoria("Natureza")

    # VISITACAO
    with abas[5]:
        st.subheader("🥾 Prepare sua visita")
        st.image(
            IMAGENS["andorinhas"],
            use_container_width=True,
            caption="Paisagens do Baixão das Andorinhas."
        )
        st.write(
            "Organize seu roteiro, consulte as orientações "
            "de visitação e escolha atividades adequadas "
            "às suas condições e ao tempo disponível."
        )
        mostrar_categoria("Visitação")

    # GALERIA
    with abas[6]:
        st.subheader("🖼️ Galeria da Serra da Capivara")
        st.write(
            "Uma seleção de imagens para conhecer um pouco "
            "mais das paisagens, da arqueologia e da natureza."
        )

        imagens_galeria = [
            ("Paisagem da Serra", IMAGENS["capa"]),
            ("Parque Nacional", IMAGENS["paisagem"]),
            ("Pedra Furada", IMAGENS["pedra"]),
            ("Pinturas rupestres", IMAGENS["pinturas"]),
            ("Baixão das Andorinhas", IMAGENS["andorinhas"]),
            ("Fauna da região", IMAGENS["capivaras"]),
            ("Caatinga", IMAGENS["caatinga"]),
            ("Flora", IMAGENS["flora"])
        ]

        for inicio in range(0, len(imagens_galeria), 2):
            esquerda, direita = st.columns(2, gap="large")
            with esquerda:
                titulo, url = imagens_galeria[inicio]
                st.image(url, use_container_width=True, caption=titulo)

            if inicio + 1 < len(imagens_galeria):
                with direita:
                    titulo, url = imagens_galeria[inicio + 1]
                    st.image(url, use_container_width=True, caption=titulo)

    # RODAPE
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
