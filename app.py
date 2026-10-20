import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="CapivaraBot - Serra da Capivara",
    page_icon="🦫",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilização visual avançada (Design Dark/Preto, Neon Accents, Card Layout)
st.markdown("""
    <style>
    /* Fundo Escuro Principal */
    .stApp {
        background-color: #0B0F17;
        color: #E2E8F0;
    }
    
    /* Cabeçalho / Título CapivaraBot em Destaque */
    .hero-title {
        font-size: 3.5rem !important;
        font-weight: 900 !important;
        background: linear-gradient(135deg, #10B981 0%, #3B82F6 50%, #A855F7 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        letter-spacing: -1px;
        margin-bottom: 0.2rem;
        text-shadow: 0px 10px 30px rgba(16, 185, 129, 0.3);
    }
    
    .hero-subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: #94A3B8;
        margin-bottom: 2rem;
        font-weight: 400;
    }

    .badge-tag {
        background: rgba(16, 185, 129, 0.15);
        color: #34D399;
        border: 1px solid rgba(52, 211, 153, 0.3);
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
    }

    /* Estilização dos Botões */
    .stButton>button {
        background: linear-gradient(135deg, #059669 0%, #10B981 100%);
        color: #FFFFFF !important;
        border-radius: 12px;
        font-weight: 700;
        border: none;
        padding: 0.6rem 1.2rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(16, 185, 129, 0.2);
        width: 100%;
    }
    
    .stButton>button:hover {
        background: linear-gradient(135deg, #10B981 0%, #34D399 100%);
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(52, 211, 153, 0.4);
    }

    /* Cartões de Informação e Métricas */
    .info-card {
        background: #161E2E;
        border: 1px solid #243046;
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
        margin-bottom: 15px;
    }

    /* Imagem em Destaque */
    .img-container {
        border-radius: 20px;
        overflow: hidden;
        border: 2px solid #243046;
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.7);
    }

    /* Bolhas do Chatbot */
    .chat-user {
        background: #1E293B;
        border: 1px solid #334155;
        color: #F1F5F9;
        padding: 14px 18px;
        border-radius: 18px 18px 2px 18px;
        margin-bottom: 12px;
        margin-left: 20%;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }

    .chat-bot {
        background: linear-gradient(135deg, #064E3B 0%, #022C22 100%);
        border: 1px solid #059669;
        color: #ECFDF5;
        padding: 16px 20px;
        border-radius: 18px 18px 18px 2px;
        margin-bottom: 15px;
        margin-right: 10%;
        box-shadow: 0 4px 20px rgba(5, 150, 105, 0.25);
    }

    .chat-bot-header {
        font-weight: 800;
        color: #34D399;
        margin-bottom: 6px;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    /* Caixas de Texto */
    .stTextInput input {
        background-color: #1E293B !important;
        color: #F8FAFC !important;
        border: 1px solid #334155 !important;
        border-radius: 12px !important;
        padding: 12px !important;
    }
    
    .stTextInput input:focus {
        border-color: #10B981 !important;
        box-shadow: 0 0 10px rgba(16, 185, 129, 0.5) !important;
    }

    /* Divisor */
    hr {
        border-color: #1E293B !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- CABEÇALHO HERO ---
st.markdown("<h1 class='hero-title'>🦫 CAPIVARABOT</h1>", unsafe_allow_html=True)
st.markdown(
    "<p class='hero-subtitle'>"
    "<span class='badge-tag'>PATRIMÔNIO UNESCO</span> &nbsp; "
    "🌿 Seu Guia Interativo Oficial da <b>Serra da Capivara</b>"
    "</p>", 
    unsafe_allow_html=True
)

# --- DESTAQUE: IMAGEM DA PEDRA FURADA E MÉTRICAS ---
col_img, col_info = st.columns([1.2, 1], gap="large")

with col_img:
    st.markdown("<div class='img-container'>", unsafe_allow_html=True)
    # Imagem real e de alta qualidade do Monumento da Pedra Furada
    st.image(
        "https://storage.stwonline.com.br/180graus/media/image_bank/2023/2/pedra-furada-sao-raimundo-nonato-foto-thiago-amaral_6212355228442260045.jpeg",
        caption="🪨 Monumento da Pedra Furada - Parque Nacional da Serra da Capivara, Piauí",
        use_container_width=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

with col_info:
    st.markdown("""
        <div class='info-card'>
            <h3 style='color: #34D399; margin-top:0;'>✨ Destaques do Parque</h3>
            <p style='color: #CBD5E1;'>
                O <b>Parque Nacional da Serra da Capivara</b> é o maior santuário de arte rupestre das Américas. 
                Um espetáculo natural e arqueológico encravado no coração do semiárido piauiense.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Métricas interativas rápidas
    m1, m2, m3 = st.columns(3)
    m1.metric("📍 Estado", "Piauí")
    m2.metric("📊 Sítios", "+1.000")
    m3.metric("🏆 UNESCO", "1991")

st.divider()

# --- SEÇÃO INTERATIVA: TABS COM DETALHES DA REGIÃO ---
st.markdown("<h2 style='color: #F8FAFC; text-align: center;'>🏞️ Explore o Parque em Detalhes</h2>", unsafe_allow_html=True)

aba1, aba2, aba3, aba4, aba5 = st.tabs([
    "📍 Localização", 
    "🪨 Pontos Turísticos", 
    "🎨 Pinturas Rupestres", 
    "🐾 Fauna e Flora", 
    "🎒 Dicas de Visitação"
])

with aba1:
    st.markdown("""
    <div class='info-card'>
        <h4 style='color: #34D399;'>Onde fica localizado?</h4>
        <p>O Parque está situado no sudeste do estado do Piauí, abrangendo os municípios de <b>São Raimundo Nonato</b>, <b>Coronel José Dias</b>, <b>Canto do Buriti</b> e <b>João Costa</b>.</p>
        <p>🚗 <b>Acesso:</b> Aproximadamente 530 km de Teresina via BR-302 / PI-140.</p>
    </div>
    """, unsafe_allow_html=True)

with aba2:
    st.markdown("""
    <div class='info-card'>
        <h4 style='color: #34D399;'>Principais Atrações Imperdíveis</h4>
        <ul>
            <li><b>Pedra Furada:</b> Formação rochosa de arenito e maior símbolo do parque.</li>
            <li><b>Baixão das Mulheres e Pedra Furada:</b> Cânions e paredões ricos em painéis rupestres.</li>
            <li><b>Museu do Homem Americano:</b> Acervo tecnológico e arqueológico em São Raimundo Nonato.</li>
            <li><b>Museu da Natureza:</b> Estrutura arquitetônica moderna em Coronel José Dias.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with aba3:
    st.markdown("""
    <div class='info-card'>
        <h4 style='color: #34D399;'>A Maior Galeria Pré-Histórica ao Ar Livre</h4>
        <p>São registros gravados nas rochas há dezenas de milhares de anos. Retratam o cotidiano, danças, rituais de caça e animais extintos da megafauna pré-histórica.</p>
    </div>
    """, unsafe_allow_html=True)

with aba4:
    st.markdown("""
    <div class='info-card'>
        <h4 style='color: #34D399;'>Biodiversidade Guardiã da Caatinga</h4>
        <p>🐾 <b>Fauna:</b> Tatu-bola, veado-catingueiro, macaco-prego, onça-parda e gaviões.</p>
        <p>🌵 <b>Flora:</b> Mandacaru, xique-xique, bromélias e vegetação adaptada à seca.</p>
    </div>
    """, unsafe_allow_html=True)

with aba5:
    st.markdown("""
    <div class='info-card'>
        <h4 style='color: #34D399;'>Guia Rápido do Visitante</h4>
        <p>🧭 <b>Guia Obrigatório:</b> A entrada nos sítios exige condutor ambiental credenciado.</p>
        <p>💧 <b>Essenciais:</b> Água abundante, protetor solar, chapéu e tênis próprio para caminhada.</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- SEÇÃO DO CHATBOT ---
st.markdown("<h2 style='color: #F8FAFC; text-align: center;'>💬 Converse com o CapivaraBot</h2>", unsafe_allow_html=True)

# Botões de perguntas rápidas (Atalhos Interativos)
st.write("💡 **Perguntas frequentes (clique para sugestão):**")
c1, c2, c3, c4 = st.columns(4)

sugestao = ""
if c1.button("🪨 O que é a Pedra Furada?"):
    sugestao = "O que é a Pedra Furada?"
if c2.button("🧭 Precisa de guia?"):
    sugestao = "Precisa de guia para visitar?"
if c3.button("👩‍🔬 Quem foi Niède Guidon?"):
    sugestao = "Quem foi Niède Guidon?"
if c4.button("⏰ Qual o horário?"):
    sugestao = "Qual o horário de funcionamento?"

# Caixa de Entrada de Pergunta
pergunta_input = st.text_input(
    "Digite sua dúvida abaixo:", 
    value=sugestao,
    placeholder="Ex: Qual a melhor época para ir? Onde me hospedar? Como chegar?"
)

if st.button("Enviar Pergunta 🦫", use_container_width=True):
    texto = pergunta_input.lower().strip()

    if not texto:
        st.warning("⚠️ Por favor, digite uma pergunta antes de enviar.")
    else:
        # Exibe a pergunta do Usuário na bolha personalizada
        st.markdown(
            f'<div class="chat-user"><b>Você:</b><br>{pergunta_input}</div>', 
            unsafe_allow_html=True
        )

        # Lógica de Mapeamento das Respostas (>30 Perguntas/Palavras-chave)
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

        elif any(w in texto for w in ["carro", "chegar de carro", "distância de teresina"]):
            resposta = "🚗 Partindo de Teresina (capital do Piauí), a viagem de carro até São Raimundo Nonato dura cerca de 6 a 7 horas pela rodovia BR-302 / PI-140."

        elif any(w in texto for w in ["hospedagem", "onde ficar", "hotel", "pousada"]):
            resposta = "🏨 As cidades de São Raimundo Nonato e Coronel José Dias oferecem ótimas opções de hotéis, pousadas e restaurantes para os turistas."

        elif any(w in texto for w in ["animais", "fauna", "bichos", "fauna da caatinga"]):
            resposta = "🐾 A fauna da região conta com tatu-bola, veado-catingueiro, macaco-prego, jaguatirica, gaviões e várias outras espécies adaptadas à Caatinga."

        elif any(w in texto for w in ["plantas", "flora", "árvores", "vegetação"]):
            resposta = "🌵 A vegetação é típica da Caatinga, com árvores de médio porte, cactus (como o mandacaru e o xique-xique), bromélias e arbustos resistentes à seca."

        elif any(w in texto for w in ["tatu-bola", "mascote"]):
            resposta = "🦡 O tatu-bola é um dos animais emblemáticos da região e serviu de inspiração para o mascote da Copa do Mundo de 2014 (o Fuleco)."

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

        elif any(w in texto for w in ["horário", "funciona", "abertura"]):
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

        # Exibe a resposta do Bot na bolha customizada estilo Neon/Dark Emerald
        st.markdown(
            f'''
            <div class="chat-bot">
                <div class="chat-bot-header">🦫 CapivaraBot</div>
                {resposta}
            </div>
            ''', 
            unsafe_allow_html=True
        )

# --- RODAPÉ INSTITUCIONAL ---
st.divider()
st.markdown(
    "<div style='text-align: center; color: #64748B; font-size: 0.85rem; padding: 10px;'>"
    "🦫 <b>CapivaraBot</b> | Projeto Educativo em Homenagem ao Parque Nacional da Serra da Capivara, Piauí.<br>"
    "Desenvolvido por: <b>Professor Daniel</b> e os alunos <b>Felype, David, Laiane e Mariana</b>."
    "</div>",
    unsafe_allow_html=True
)
