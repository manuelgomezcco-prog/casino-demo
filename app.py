import streamlit as st
import base64
import requests
from io import BytesIO

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="Fortuna MX",
    page_icon="🍀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. FUNCIÓN PARA CARGAR EL LOGO (SOLUCIÓN DEFINITIVA)
def get_base64_img(url):
    try:
        response = requests.get(url)
        return base64.b64encode(response.content).decode()
    except:
        return ""

# URL de tu logo en GitHub
url_logo = "https://raw.githubusercontent.com/ManuelG-Prog/casino-demo/principal/logo.PNG"
logo_base64 = get_base64_img(url_logo)

# 3. CSS DE ALTA FIDELIDAD (Estilo Winpot)
st.markdown(f"""
    <style>
    /* Fondo y Reset General */
    .stApp {{ background-color: #0b0e11; }}
    [data-testid="stHeader"] {{display: none;}}
    header {{visibility: hidden;}}
    
    /* HEADER FIJO */
    .custom-header {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 5px 20px;
        background-color: #1a1f26;
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 9999;
        height: 65px;
        border-bottom: 1px solid #2d343f;
    }}

    /* Estilo del Logotipo */
    .logo-container img {{
        max-height: 45px;
        width: auto;
        display: block;
    }}

    /* Contenedor de Acciones (Botón y Saldo) */
    .user-actions {{
        display: flex;
        align-items: center;
        gap: 12px;
    }}

    .deposit-btn {{
        background-color: #76b82a;
        color: #000 !important;
        padding: 8px 16px;
        border-radius: 8px;
        font-weight: bold;
        font-size: 14px;
        text-decoration: none;
        display: flex;
        align-items: center;
        gap: 6px;
    }}

    .balance-badge {{
        background-color: #2d343f;
        color: #fff;
        padding: 8px 12px;
        border-radius: 8px;
        font-weight: bold;
        font-size: 14px;
        border: 1px solid #3e4652;
        font-family: 'Roboto', sans-serif;
    }}

    /* BANNER Y CONTENIDO */
    .main-wrapper {{
        margin-top: 85px; /* Espacio para que no choque con el header */
    }}

    .banner-img {{
        width: 100%;
        border-radius: 15px;
        margin-bottom: 25px;
    }}

    .section-title {{
        color: #ffffff;
        font-size: 16px;
        font-weight: bold;
        margin-bottom: 15px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}

    /* Ajuste de botones de juego nativos de Streamlit */
    .stButton > button {{
        background-color: #1a1f26 !important;
        color: white !important;
        border: 1px solid #3e4652 !important;
        font-weight: bold !important;
        width: 100%;
    }}
    
    .stButton > button:hover {{
        border-color: #76b82a !important;
        color: #76b82a !important;
    }}

    /* MENÚ INFERIOR MÓVIL */
    .bottom-nav {{
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: #1a1f26;
        display: flex;
        justify-content: space-around;
        padding: 12px 0;
        border-top: 1px solid #2d343f;
        z-index: 9999;
    }}

    .nav-item {{
        text-align: center;
        color: #8a96a3;
        font-size: 11px;
        text-decoration: none;
    }}
    </style>

    <div class="custom-header">
        <div class="logo-container">
            <img src="data:image/png;base64,{logo_base64}" alt="Fortuna MX">
        </div>
        <div class="user-actions">
            <a class="deposit-btn">📥 Depositar</a>
            <div class="balance-badge">$ 5,000.00</div>
            <div style="color: #8a96a3; font-size: 24px; cursor: pointer;">👤</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 4. CONTENIDO DE LA APLICACIÓN
st.markdown('<div class="main-wrapper">', unsafe_allow_html=True)

# Banner Principal
st.markdown('<img src="https://images.unsplash.com/photo-1518623489648-a173ef7824f3?w=1200" class="banner-img">', unsafe_allow_html=True)

# Sección de Juegos
st.markdown('<div class="section-title">Sigue Jugando</div>', unsafe_allow_html=True)

# Cuadrícula de 2 columnas para móvil (se ve mejor)
col1, col2 = st.columns(2)
img_juego = "https://images.unsplash.com/photo-1596711762462-850f28584813?w=400"

with col1:
    st.image(img_juego, use_container_width=True)
    st.button("JUGAR", key="game_1")

with col2:
    st.image(img_juego, use_container_width=True)
    st.button("JUGAR", key="game_2")

st.markdown('</div>', unsafe_allow_html=True) # Cierre de main-wrapper

# 5. MENÚ INFERIOR (Visual)
st.markdown("""
    <div class="bottom-nav">
        <a class="nav-item">🏠<br>Inicio</a>
        <a class="nav-item" style="color: #76b82a;">📥<br>Depositar</a>
        <a class="nav-item">🎰<br>Slots</a>
        <a class="nav-item">☰<br>Menú</a>
    </div>
    <div style="height: 80px;"></div>
    """, unsafe_allow_html=True)

# 6. LÓGICA DE BOTONES (OPCIONAL)
if st.session_state.get('game_1'):
    st.toast("Cargando juego...")
