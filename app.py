import streamlit as st

# CONFIGURACIÓN
st.set_page_config(
    page_title="Fortuna MX",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# OCULTAR HEADER NATIVO
st.markdown("""
    <style>
    .stApp { background-color: #0b1118; }
    header {visibility: hidden;}
    [data-testid="stHeader"] {display: none;}
    div.block-container {padding-top: 10px;}

    /* HEADER */
    .custom-header {
        position: fixed;
        top: 0; left: 0; right: 0;
        height: 70px;
        background: #1a232e;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 15px;
        z-index: 9999;
        border-bottom: 1px solid #2d343f;
    }

    .right-box {
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .btn {
        background: #76b82a;
        padding: 8px 14px;
        border-radius: 6px;
        font-weight: bold;
        color: black;
        font-size: 13px;
    }

    .saldo {
        background: #2d343f;
        padding: 8px 12px;
        border-radius: 6px;
        color: white;
        font-weight: bold;
        font-size: 13px;
    }

    .main {
        margin-top: 90px;
    }

    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: #1a232e;
        display: flex;
        justify-content: space-around;
        padding: 12px 0;
        border-top: 1px solid #2d343f;
    }
    </style>
""", unsafe_allow_html=True)

# HEADER CON LOGO LOCAL
st.markdown('<div class="custom-header">', unsafe_allow_html=True)

col1, col2 = st.columns([1, 3])

with col1:
    st.image("Logo.jpg", width=110)

with col2:
    st.markdown("""
        <div class="right-box">
            <div class="btn">📥 Depositar</div>
            <div class="saldo">$ 5,000.00</div>
            <div style="font-size:22px; color:#8a96a3;">👤</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# CONTENIDO
st.markdown('<div class="main">', unsafe_allow_html=True)

# Banner
st.image(
    "https://images.unsplash.com/photo-1518623489648-a173ef7824f3?w=1200",
    use_container_width=True
)

# Título
st.markdown(
    '<div style="color:white; font-weight:bold; margin:20px 0 10px;">SIGUE JUGANDO</div>',
    unsafe_allow_html=True
)

# Juegos
col1, col2 = st.columns(2)

with col1:
    st.image(
        "https://images.unsplash.com/photo-1596711762462-850f28584813?w=400",
        use_container_width=True
    )
    st.button("JUGAR", key="g1", use_container_width=True)

with col2:
    st.image(
        "https://images.unsplash.com/photo-1596711762462-850f28584813?w=400",
        use_container_width=True
    )
    st.button("JUGAR", key="g2", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# FOOTER
st.markdown("""
    <div class="footer">
        <div style="text-align:center; color:white; font-size:10px;">🏠<br>Inicio</div>
        <div style="text-align:center; color:#76b82a; font-size:10px;">📥<br>Depositar</div>
        <div style="text-align:center; color:white; font-size:10px;">🎰<br>Slots</div>
        <div style="text-align:center; color:white; font-size:10px;">☰<br>Menú</div>
    </div>
    <div style="height:70px;"></div>
""", unsafe_allow_html=True)
