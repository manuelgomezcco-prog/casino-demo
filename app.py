import streamlit as st
import base64
import requests

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(page_title="Fortuna MX", layout="wide", initial_sidebar_state="collapsed")

# 2. FUNCIÓN PARA CARGAR LA IMAGEN (SOLUCIÓN AL LOGO ROTO)
def get_base64(url):
    try:
        response = requests.get(url)
        return base64.b64encode(response.content).decode()
    except:
        return ""

# Cargamos el logo una sola vez
logo_url = "https://raw.githubusercontent.com/ManuelG-Prog/casino-demo/principal/logo.PNG"
logo_data = get_base64(logo_url)

# 3. CSS PROFESIONAL (ESTILO WINPOT)
st.markdown(f"""
    <style>
    /* Fondo y reseteo */
    .stApp {{ background-color: #0b1118; }}
    header {{visibility: hidden;}}
    [data-testid="stHeader"] {{display: none;}}
    div.block-container {{padding-top: 0rem;}}

    /* HEADER FIJO */
    .custom-header {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 15px;
        background-color: #1a232e;
        position: fixed;
        top: 0; left: 0; right: 0;
        z-index: 9999;
        height: 65px;
        border-bottom: 1px solid #2d343f;
    }}

    .logo-img {{
        height: 38px;
        width: auto;
    }}

    .header-right {{
        display: flex;
        align-items: center;
        gap: 8px;
    }}

    /* BOTÓN DEPOSITAR CORREGIDO */
    .btn-dep {{
        background-color: #76b82a;
        color: black !important;
        padding: 8px 14px;
        border-radius: 6px;
        font-weight: bold;
        font-size: 13px;
        text-decoration: none;
    }}

    .bal-badge {{
        background-color: #2d343f;
        color: white;
        padding: 8px 12px;
        border-radius: 6px;
        font-weight: bold;
        font-size: 13px;
    }}

    /* Ajuste para que el contenido no quede oculto bajo el header */
    .main-body {{
        margin-top: 80px;
    }}

    /* Grid de juegos */
    .game-title {{
        color: white;
        font-weight: bold;
        margin: 20px 0 10px 0;
        text-transform: uppercase;
        font-size: 14px;
    }}

    /* Menú Inferior */
    .footer-nav {{
        position: fixed;
        bottom: 0; left: 0; right: 0;
        background: #1a232e;
        display: flex;
        justify-content: space-around;
        padding: 12px 0;
        border-top: 1px solid #2d343f;
        z-index: 9999;
    }}
    </style>

    <div class="custom-header">
        <img src="data:image/png;base64,{logo_data}" class="logo-img">
        <div class="header-right">
            <a class="btn-dep">📥 Depositar</a>
            <div class="bal-badge">$ 5,000.00</div>
            <div style="font-size: 24px; color: #8a96a3;">👤</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 4. CONTENIDO DE LA APP
st.markdown('<div class="main-body">', unsafe_allow_html=True)

# Banner
st.image("https://images.unsplash.com/photo-1518623489648-a173ef7824f3?w=1200", use_container_width=True)

# Sección de Juegos
st.markdown('<div class="game-title">Sigue Jugando</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.image("https://images.unsplash.com/photo-1596711762462-850f28584813?w=400", use_container_width=True)
    st.button("JUGAR", key="g1", use_container_width=True)
with col2:
    st.image("https://images.unsplash.com/photo-1596711762462-850f28584813?w=400", use_container_width=True)
    st.button("JUGAR", key="g2", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# 5. NAVEGACIÓN INFERIOR
st.markdown("""
    <div class="footer-nav">
        <div style="text-align: center; color: white; font-size: 10px;">🏠<br>Inicio</div>
        <div style="text-align: center; color: #76b82a; font-size: 10px;">📥<br>Depositar</div>
        <div style="text-align: center; color: white; font-size: 10px;">🎰<br>Slots</div>
        <div style="text-align: center; color: white; font-size: 10px;">☰<br>Menú</div>
    </div>
    <div style="height: 70px;"></div>
    """, unsafe_allow_html=True)
