
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
# 2. IDENTIDADE DO PROJETO
# ============================================================

NOME_PROJETO = "CapivaraBot"
SUBTITULO = "Seu guia virtual pela Serra da Capivara"

DESCRICAO = (
    "Uma experiência interativa para conhecer a história, "
    "a arqueologia, a natureza e a riqueza cultural do Piauí."
)

# ============================================================
# 3. IMAGENS
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
# 4. BANCO DE CONHECIMENTO
# ============================================================

BANCO_RESPOSTAS = [

    # --------------------------------------------------------
    # INFORMAÇÕES GERAIS
    # --------------------------------------------------------

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
            "o que visitar"
        ],
        "resposta": (
            "Entre os principais atrativos estão a Pedra Furada, "
            "o Boqueirão da Pedra Furada, o Baixão das Andorinhas, "
            "os circuitos de sítios arqueológicos, os mirantes "
            "e as trilhas."
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
            "vegetacao do piaui"
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
            "condutores e verificar as regras atualizadas de visitação."
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
            "criado o parque",
            "niede guidon"
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
    },

    # --------------------------------------------------------
    # 59 NOVAS PERGUNTAS SOBRE VISITAÇÃO
    # --------------------------------------------------------

    {
        "palavras": [
            "como chegar ao parque",
            "como chegar na serra",
            "como chegar a serra da capivara"
        ],
        "resposta": (
            "É possível chegar à região por transporte rodoviário "
            "ou aéreo, conforme a disponibilidade de voos e conexões. "
            "A partir de São Raimundo Nonato, o deslocamento até os "
            "acessos do parque pode ser feito por transporte contratado "
            "ou veículo próprio, conforme o roteiro."
        )
    },

    {
        "palavras": [
            "qual a distancia entre sao raimundo nonato e o parque",
            "distancia de sao raimundo nonato",
            "distancia ate o parque"
        ],
        "resposta": (
            "A distância depende da entrada e do atrativo escolhido. "
            "O parque possui diferentes acessos e circuitos, por isso "
            "é importante verificar o percurso antes de sair."
        )
    },

    {
        "palavras": [
            "qual a melhor epoca para visitar",
            "melhor epoca para conhecer o parque",
            "quando visitar a serra da capivara"
        ],
        "resposta": (
            "A visita pode acontecer durante todo o ano. O período "
            "de chuvas costuma deixar a vegetação mais verde, enquanto "
            "a estação seca apresenta paisagens diferentes. A escolha "
            "depende da preferência do visitante."
        )
    },

    {
        "palavras": [
            "qual o horario de funcionamento do parque",
            "horario de funcionamento",
            "que horas o parque abre",
            "que horas o parque fecha"
        ],
        "resposta": (
            "Os horários de visitação podem variar conforme os "
            "circuitos e as condições operacionais. Consulte as "
            "informações atualizadas do ICMBio e dos condutores "
            "antes de programar o passeio."
        )
    },

    {
        "palavras": [
            "e necessario agendar a visita",
            "precisa agendar o passeio",
            "como agendar a visita"
        ],
        "resposta": (
            "É recomendável organizar o passeio antecipadamente "
            "e entrar em contato com um condutor cadastrado para "
            "verificar disponibilidade, horários e condições dos roteiros."
        )
    },

    {
        "palavras": [
            "e necessario pagar ingresso",
            "quanto custa a entrada",
            "qual o valor do ingresso",
            "o parque e gratuito"
        ],
        "resposta": (
            "As informações oficiais de visitação do ICMBio indicam "
            "entrada gratuita. Entretanto, serviços de condução, "
            "transporte e outras atividades contratadas podem ter custos."
        )
    },

    {
        "palavras": [
            "e obrigatorio contratar um guia",
            "precisa de guia turistico",
            "precisa contratar condutor",
            "e obrigatorio um condutor"
        ],
        "resposta": (
            "A visitação deve seguir as regras oficiais do parque, "
            "que preveem acompanhamento por condutor cadastrado. "
            "Consulte o ICMBio para confirmar as condições aplicáveis "
            "ao roteiro escolhido."
        )
    },

    {
        "palavras": [
            "quanto tempo dura um passeio",
            "duracao do passeio",
            "quanto tempo leva a visita"
        ],
        "resposta": (
            "Depende do circuito escolhido. Existem passeios de "
            "algumas horas e roteiros que podem ocupar um dia inteiro."
        )
    },

    {
        "palavras": [
            "posso visitar o parque em um dia",
            "da para conhecer em um dia",
            "visitar em apenas um dia"
        ],
        "resposta": (
            "Sim. É possível conhecer alguns atrativos em um dia, "
            "mas para explorar diferentes circuitos e sítios "
            "arqueológicos é recomendável reservar mais tempo."
        )
    },

    {
        "palavras": [
            "o parque funciona em feriados",
            "funciona aos finais de semana",
            "abre nos finais de semana",
            "abre nos feriados"
        ],
        "resposta": (
            "A visitação depende do calendário e das condições "
            "operacionais. Confirme antecipadamente com o ICMBio "
            "ou com os responsáveis pela condução turística."
        )
    },

    {
        "palavras": [
            "posso visitar por conta propria",
            "posso ir sozinho ao parque",
            "visitar sem guia",
            "visita independente"
        ],
        "resposta": (
            "A visita deve respeitar as regras de acompanhamento "
            "e os roteiros autorizados. Entre em contato com um "
            "condutor cadastrado antes de iniciar o passeio."
        )
    },

    {
        "palavras": [
            "o que devo levar",
            "o que levar para visitar",
            "itens para levar ao parque",
            "o que levar na caminhada"
        ],
        "resposta": (
            "Leve água suficiente, protetor solar, chapéu ou boné, "
            "roupas confortáveis, calçados adequados para caminhada "
            "e lanches, conforme a duração do roteiro."
        )
    },

    {
        "palavras": [
            "quais os principais atrativos",
            "principais pontos turisticos",
            "atracoes do parque",
            "lugares mais famosos"
        ],
        "resposta": (
            "Entre os principais atrativos estão a Pedra Furada, "
            "o Boqueirão da Pedra Furada, o Baixão das Andorinhas, "
            "os circuitos de sítios arqueológicos, os mirantes e as trilhas."
        )
    },

    {
        "palavras": [
            "o que e a pedra furada",
            "explique a pedra furada",
            "formacao da pedra furada"
        ],
        "resposta": (
            "É uma impressionante formação rochosa natural com "
            "uma abertura que se tornou um dos símbolos mais "
            "conhecidos da Serra da Capivara."
        )
    },

    {
        "palavras": [
            "o que e o boqueirao da pedra furada",
            "boqueirao da pedra furada",
            "sitio arqueologico pedra furada"
        ],
        "resposta": (
            "É um dos sítios arqueológicos mais importantes e "
            "conhecidos da região, com pinturas rupestres e registros "
            "fundamentais para os estudos sobre a presença humana "
            "no continente americano."
        )
    },

    {
        "palavras": [
            "o que sao pinturas rupestres",
            "significado das pinturas rupestres",
            "como eram feitas as pinturas rupestres"
        ],
        "resposta": (
            "São desenhos e representações produzidos por antigas "
            "populações humanas em superfícies rochosas, utilizando "
            "pigmentos naturais."
        )
    },

    {
        "palavras": [
            "quantos sitios arqueologicos existem",
            "quantidade de sitios arqueologicos",
            "numero de sitios do parque"
        ],
        "resposta": (
            "O parque possui mais de mil sítios arqueológicos "
            "cadastrados, sendo centenas deles com registros "
            "de pinturas rupestres."
        )
    },

    {
        "palavras": [
            "e possivel fotografar as pinturas",
            "pode tirar fotos das pinturas rupestres",
            "fotografar os registros rupestres"
        ],
        "resposta": (
            "Em geral, é possível fotografar os registros respeitando "
            "as orientações do condutor e as regras de conservação. "
            "Não se deve tocar nas pinturas nem utilizar equipamentos "
            "ou iluminação que possam causar danos."
        )
    },

    {
        "palavras": [
            "o que e o baixao das andorinhas",
            "baixao das andorinhas",
            "andorinhas no parque"
        ],
        "resposta": (
            "É um atrativo natural conhecido por suas formações "
            "rochosas e pela observação de aves, especialmente no "
            "final da tarde, quando andorinhas e outros pássaros "
            "podem ser vistos voando na região."
        )
    },

    {
        "palavras": [
            "existem mirantes",
            "tem mirantes no parque",
            "onde observar a paisagem"
        ],
        "resposta": (
            "Sim. O parque possui pontos de observação que permitem "
            "contemplar as paisagens da Caatinga, os vales e as "
            "formações rochosas."
        )
    },

    {
        "palavras": [
            "todos os atrativos podem ser visitados no mesmo dia",
            "da para visitar todos os atrativos",
            "conhecer todos os circuitos em um dia"
        ],
        "resposta": (
            "Não necessariamente. Os atrativos estão distribuídos "
            "em diferentes áreas e circuitos. O ideal é organizar "
            "um roteiro com o condutor, considerando distância, "
            "duração e dificuldade das caminhadas."
        )
    },

    {
        "palavras": [
            "o parque possui trilhas",
            "existem trilhas para caminhada",
            "trilhas da serra da capivara"
        ],
        "resposta": (
            "Sim. Existem trilhas com diferentes distâncias e "
            "níveis de dificuldade, que permitem conhecer sítios "
            "arqueológicos e paisagens naturais."
        )
    },

    {
        "palavras": [
            "as trilhas sao dificeis",
            "nivel de dificuldade das trilhas",
            "as caminhadas exigem muito esforco"
        ],
        "resposta": (
            "Algumas são leves e outras exigem maior esforço físico. "
            "É importante escolher o circuito de acordo com as "
            "condições físicas e as orientações do condutor."
        )
    },

    {
        "palavras": [
            "criancas podem fazer as trilhas",
            "pode levar criancas",
            "visita com criancas"
        ],
        "resposta": (
            "Sim, desde que o roteiro seja adequado à idade, "
            "às condições da criança e às recomendações de segurança."
        )
    },

    {
        "palavras": [
            "pessoas idosas podem visitar",
            "idosos podem fazer os passeios",
            "visita para idosos"
        ],
        "resposta": (
            "Sim. É possível selecionar roteiros com caminhadas "
            "mais curtas e acessíveis, conforme as condições "
            "de cada visitante."
        )
    },

    {
        "palavras": [
            "e possivel fazer passeio de bicicleta",
            "pode andar de bicicleta no parque",
            "passeio de bicicleta"
        ],
        "resposta": (
            "A possibilidade depende das regras e dos roteiros "
            "autorizados. Consulte a administração do parque e "
            "os prestadores de serviços locais antes de planejar "
            "essa atividade."
        )
    },

    {
        "palavras": [
            "posso fazer piquenique",
            "e permitido piquenique",
            "pode comer dentro do parque"
        ],
        "resposta": (
            "A alimentação deve respeitar as áreas permitidas e "
            "as orientações de visitação. Nunca deixe restos de "
            "alimentos ou embalagens no ambiente natural."
        )
    },

    {
        "palavras": [
            "e possivel observar animais silvestres",
            "posso ver animais no parque",
            "observacao de animais"
        ],
        "resposta": (
            "Sim. O parque abriga diversas espécies da fauna da "
            "Caatinga. A observação deve acontecer à distância, "
            "sem alimentar, perseguir ou tentar tocar nos animais."
        )
    },

    {
        "palavras": [
            "qual o melhor horario para fotografar",
            "melhor horario para tirar fotos",
            "horario para fotografar as paisagens"
        ],
        "resposta": (
            "O início da manhã e o final da tarde costumam oferecer "
            "iluminação interessante para fotografias. Respeite "
            "sempre os horários autorizados de visitação."
        )
    },

    {
        "palavras": [
            "existem passeios para ver o por do sol",
            "pode ver o por do sol",
            "passeio no final da tarde"
        ],
        "resposta": (
            "Alguns roteiros permitem contemplar a paisagem no "
            "final da tarde. É necessário verificar com o condutor "
            "os locais autorizados e os horários de retorno."
        )
    },

    {
        "palavras": [
            "preciso ter preparo fisico",
            "e necessario preparo fisico",
            "precisa estar em boa forma para visitar"
        ],
        "resposta": (
            "Não para todos os passeios. Existem opções com diferentes "
            "níveis de esforço, mas é importante informar ao condutor "
            "suas limitações para escolher o roteiro adequado."
        )
    },

    {
        "palavras": [
            "onde encontrar hospedagem",
            "onde ficar hospedado",
            "hoteis perto do parque",
            "pousadas em sao raimundo nonato"
        ],
        "resposta": (
            "São Raimundo Nonato oferece opções de hotéis, pousadas "
            "e outras hospedagens. Também existem alternativas em "
            "municípios próximos. É recomendável reservar antecipadamente."
        )
    },

    {
        "palavras": [
            "existem restaurantes proximos",
            "onde comer perto do parque",
            "restaurantes em sao raimundo nonato"
        ],
        "resposta": (
            "São Raimundo Nonato possui restaurantes, lanchonetes "
            "e estabelecimentos que oferecem refeições regionais "
            "e outras opções gastronômicas."
        )
    },

    {
        "palavras": [
            "onde contratar um condutor turistico",
            "como contratar um condutor",
            "onde encontrar guia cadastrado",
            "associacao de condutores"
        ],
        "resposta": (
            "Você pode buscar informações junto à associação ou "
            "aos serviços de condutores cadastrados, agências de "
            "turismo locais e canais oficiais de atendimento do parque."
        )
    },

    {
        "palavras": [
            "existe transporte turistico",
            "transporte para os atrativos",
            "como chegar aos atrativos",
            "transporte dentro do parque"
        ],
        "resposta": (
            "Existem prestadores de serviços que oferecem transporte "
            "e passeios na região. Consulte as empresas locais para "
            "verificar disponibilidade, valores e condições."
        )
    },

    {
        "palavras": [
            "o parque possui banheiros",
            "tem banheiro no parque",
            "pontos de apoio",
            "locais para descanso"
        ],
        "resposta": (
            "A infraestrutura varia conforme o circuito e o atrativo. "
            "Antes de sair, confirme com o condutor onde existem "
            "banheiros, pontos de apoio e locais para descanso."
        )
    },

    {
        "palavras": [
            "existe sinal de celular",
            "tem internet no parque",
            "funciona celular dentro do parque",
            "tem sinal de telefone"
        ],
        "resposta": (
            "O sinal pode ser limitado ou inexistente em determinados "
            "trechos. É recomendável combinar previamente o roteiro, "
            "os horários e os pontos de encontro."
        )
    },

    {
        "palavras": [
            "existe atendimento de emergencia",
            "o que fazer em uma emergencia",
            "atendimento medico no parque"
        ],
        "resposta": (
            "O visitante deve seguir as orientações do condutor e "
            "informar previamente qualquer necessidade especial. "
            "Em emergências, deve-se acionar os serviços públicos "
            "competentes."
        )
    },

    {
        "palavras": [
            "existe algum museu na regiao",
            "quais museus visitar",
            "museus perto do parque"
        ],
        "resposta": (
            "Sim. O Museu do Homem Americano e o Museu da Natureza "
            "são importantes atrações culturais e científicas da região."
        )
    },

    {
        "palavras": [
            "o que conhecer no museu do homem americano",
            "o que tem no museu do homem americano",
            "museu do homem americano exposicao"
        ],
        "resposta": (
            "O museu apresenta informações sobre a presença humana "
            "na região, pesquisas arqueológicas, vestígios encontrados "
            "e a história das antigas populações."
        )
    },

    {
        "palavras": [
            "o que conhecer no museu da natureza",
            "o que tem no museu da natureza",
            "museu da natureza exposicao"
        ],
        "resposta": (
            "O museu apresenta a história da natureza e as "
            "transformações ambientais do planeta, com exposições "
            "sobre a evolução da vida e os acontecimentos que "
            "marcaram a região."
        )
    },

    {
        "palavras": [
            "o parque possui acessibilidade",
            "pessoas com mobilidade reduzida",
            "atrativos acessiveis",
            "acessibilidade no parque"
        ],
        "resposta": (
            "Existem sítios arqueológicos com estruturas adaptadas "
            "para pessoas com mobilidade reduzida. É importante "
            "consultar previamente quais atrativos oferecem "
            "acessibilidade e quais são as condições de visitação."
        )
    },

    {
        "palavras": [
            "o que fazer em caso de chuva",
            "passeio durante a chuva",
            "pode visitar quando chove"
        ],
        "resposta": (
            "Siga imediatamente as orientações do condutor. "
            "Dependendo das condições climáticas, algumas trilhas "
            "e áreas podem ter a visitação suspensa por segurança."
        )
    },

    {
        "palavras": [
            "posso levar animais de estimacao",
            "pode levar cachorro",
            "entrada de animais domesticos",
            "posso levar meu pet"
        ],
        "resposta": (
            "A entrada de animais domésticos está sujeita às regras "
            "da unidade de conservação. Consulte previamente o "
            "ICMBio antes de levar seu animal."
        )
    },

    {
        "palavras": [
            "e permitido fumar",
            "pode fumar dentro do parque",
            "proibido fumar"
        ],
        "resposta": (
            "O visitante deve respeitar as restrições ambientais e "
            "as orientações da administração, especialmente devido "
            "ao risco de incêndios na vegetação da Caatinga."
        )
    },

    {
        "palavras": [
            "posso retirar pedras",
            "pode levar pedras como lembranca",
            "retirar rochas do parque",
            "levar fosseis"
        ],
        "resposta": (
            "Não. É proibido retirar materiais arqueológicos, pedras, "
            "fósseis, plantas ou qualquer elemento natural do parque."
        )
    },

    {
        "palavras": [
            "o que fazer ao encontrar um animal",
            "encontrei um animal silvestre",
            "como agir perto de animais"
        ],
        "resposta": (
            "Mantenha distância, não tente alimentar ou tocar no "
            "animal e avise o condutor responsável."
        )
    },

    {
        "palavras": [
            "como ajudar na preservacao das pinturas",
            "como proteger as pinturas rupestres",
            "conservar pinturas rupestres"
        ],
        "resposta": (
            "Não toque nas pinturas, não escreva nas rochas, "
            "não utilize produtos químicos e respeite as áreas "
            "delimitadas para visitação."
        )
    },

    {
        "palavras": [
            "o que acontece se danificar um sitio",
            "danificar pinturas rupestres",
            "danos ao patrimonio arqueologico"
        ],
        "resposta": (
            "Danificar o patrimônio arqueológico é uma infração e "
            "pode gerar responsabilização conforme a legislação "
            "brasileira. As pinturas e os sítios são bens que "
            "precisam ser protegidos."
        )
    },

    {
        "palavras": [
            "como contribuir com turismo sustentavel",
            "como praticar turismo sustentavel",
            "ajudar o turismo local"
        ],
        "resposta": (
            "Você pode contribuir contratando serviços locais, "
            "valorizando a cultura regional, respeitando as "
            "comunidades, evitando desperdícios e preservando "
            "o meio ambiente."
        )
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

    return texto.strip()


# ============================================================
# 6. SISTEMA INTELIGENTE DE RESPOSTAS
# ============================================================

def responder(pergunta):

    texto = normalizar(pergunta)

    if not texto:
        return "Por favor, escreva uma pergunta."

    cumprimentos = [
        "oi",
        "ola",
        "bom dia",
        "boa tarde",
        "boa noite",
        "tudo bem",
        "e ai"
    ]

    if texto in cumprimentos:
        return (
            "Olá! Seja bem-vindo ao CapivaraBot! 🐾\n\n"
            "Estou pronto para ajudar você a conhecer a Serra "
            "da Capivara. O que gostaria de saber?"
        )

    palavras_pergunta = set(texto.split())

    melhor_resposta = None
    maior_pontuacao = 0

    for item in BANCO_RESPOSTAS:

        pontuacao_item = 0

        for termo_original in item["palavras"]:

            termo = normalizar(termo_original)

            # Correspondência de expressão completa
            if termo in texto:
                pontuacao = 100 + len(termo.split())

            else:
                palavras_termo = set(termo.split())

                if len(palavras_termo) < 2:
                    continue

                correspondencias = palavras_pergunta.intersection(
                    palavras_termo
                )

                proporcao = (
                    len(correspondencias) / len(palavras_termo)
                )

                if proporcao >= 0.60:
                    pontuacao = proporcao * 10
                else:
                    pontuacao = 0

            pontuacao_item = max(
                pontuacao_item,
                pontuacao
            )

        if pontuacao_item > maior_pontuacao:
            maior_pontuacao = pontuacao_item
            melhor_resposta = item["resposta"]

    if melhor_resposta and maior_pontuacao >= 6:
        return melhor_resposta

    return (
        "Ainda não encontrei uma resposta específica para essa pergunta.\n\n"
        "Você pode reformulá-la ou perguntar sobre localização, "
        "horários, ingressos, transporte, trilhas, hospedagem, "
        "museus, pinturas rupestres, fauna, flora ou preservação "
        "do Parque Nacional da Serra da Capivara."
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
                "Estou aqui para ajudar você a descobrir a Serra "
                "da Capivara. Escreva sua pergunta no campo abaixo "
                "e vamos explorar esse patrimônio juntos!"
            )
        }
    ]


# ============================================================
# 8. CABEÇALHO
# ============================================================

st.write("")

st.caption("TURISMO • HISTÓRIA • ARQUEOLOGIA • CULTURA")

st.title("🐾 CapivaraBot")

st.subheader(SUBTITULO)

st.write(DESCRICAO)

st.divider()


# ============================================================
# 9. APRESENTAÇÃO DO PARQUE
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
# 10. INFORMAÇÕES PRINCIPAIS
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
# 11. CHATBOT
# ============================================================

st.header("Converse com o CapivaraBot")

st.write(
    "Quer saber mais sobre a Serra da Capivara? "
    "Digite sua pergunta abaixo. O chatbot apresentará "
    "a resposta nesta conversa."
)

with st.container(border=True):

    st.subheader("💬 Atendimento virtual")

    for mensagem in st.session_state.mensagens:

        with st.chat_message(mensagem["role"]):

            st.markdown(mensagem["content"])


# Campo único para perguntas

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
# 12. LIMPAR CONVERSA
# ============================================================

if st.button("Limpar histórico da conversa"):

    st.session_state.mensagens = [
        {
            "role": "assistant",
            "content": (
                "Olá novamente! Sou o CapivaraBot. 🐾\n\n"
                "Qual será sua próxima pergunta?"
            )
        }
    ]

    st.rerun()


st.divider()


# ============================================================
# 13. RODAPÉ
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

# ============================================================
# FIM DO CAPIVARABOT
# ============================================================
