import streamlit as st

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="Fortuna MX",
    page_icon="🍀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. CSS PARA INTERFAZ PROFESIONAL (ESTILO WINPOT)
st.markdown("""
    <style>
    /* Fondo oscuro y eliminación de elementos nativos */
    .stApp { background-color: #0b1118; }
    header {visibility: hidden;}
    [data-testid="stHeader"] {display: none;}
    div.block-container {padding-top: 1rem; padding-bottom: 5rem;}

    /* Contenedor del Saldo */
    .balance-badge {
        background-color: #1a1f26;
        color: #ffffff;
        padding: 6px 12px;
        border-radius: 6px;
        font-weight: bold;
        font-size: 14px;
        border: 1px solid #2d343f;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    /* Botón Depositar Corregido */
    .deposit-btn {
        background-color: #76b82a;
        color: #000000 !important;
        padding: 8px 15px;
        border-radius: 8px;
        font-weight: bold;
        font-size: 14px;
        text-decoration: none;
        display: inline-block;
        text-align: center;
    }

    /* Estilo para las secciones de juegos */
    .section-title {
        color: #ffffff;
        font-size: 16px;
        font-weight: bold;
        margin: 20px 0 10px 0;
        text-transform: uppercase;
    }

    /* Ajuste de imágenes de juegos */
    [data-testid="stImage"] img {
        border-radius: 12px !important;
        transition: transform 0.3s;
    }
    
    /* Menú Inferior Fijo */
    .footer-nav {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background-color: #1a1f26;
        display: flex;
        justify-content: space-around;
        padding: 10px 0;
        border-top: 1px solid #2d343f;
        z-index: 1000;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. HEADER: LOGO, DEPÓSITO Y SALDO
# Usamos columnas con proporciones específicas para que el logo tenga espacio
h_col1, h_col2, h_col3, h_col4 = st.columns([3, 3, 3, 1])

with h_col1:
    # URL directa de GitHub
    logo_url = "https://raw.githubusercontent.com/ManuelG-Prog/casino-demo/principal/logo.PNG"
    st.image(logo_url, width=150)

with h_col2:
    # Botón de Depositar con ortografía corregida
    st.markdown('<a class="deposit-btn">📥 Depositar</a>', unsafe_allow_html=True)

with h_col3:
    # Badge de saldo
    st.markdown('<div class="balance-badge">$ 5,000.00</div>', unsafe_allow_html=True)

with h_col4:
    # Icono de perfil simple
    st.markdown('<div style="font-size: 24px; text-align: right; color: #8a96a3;">👤</div>', unsafe_allow_html=True)

# 4. CONTENIDO PRINCIPAL
st.divider()

# Banner Promocional
st.image("https://images.unsplash.com/photo-1518623489648-a173ef7824f3?w=1200", use_container_width=True)

# Sección "Sigue Jugando"
st.markdown('<div class="section-title">Sigue Jugando</div>', unsafe_allow_html=True)

# Cuadrícula de juegos (2 columnas para móvil para que no se vea amontonado)
grid_col1, grid_col2 = st.columns(2)
img_juego = "https://images.unsplash.com/photo-1596711762462-850f28584813?w=400"

with grid_col1:
    st.image(img_juego, use_container_width=True)
    st.button("JUGAR", key="juego_1", use_container_width=True)

with grid_col2:
    st.image(img_juego, use_container_width=True)
    st.button("JUGAR", key="juego_2", use_container_width=True)

# 5. MENÚ INFERIOR ESTILO APLICACIÓN
st.markdown("""
    <div class="footer-nav">
        <div style="text-align: center; color: white; font-size: 11px;">🏠<br>Inicio</div>
        <div style="text-align: center; color: #76b82a; font-size: 11px;">📥<br>Depositar</div>
        <div style="text-align: center; color: white; font-size: 11px;">🎰<br>Slots</div>
        <div style="text-align: center; color: white; font-size: 11px;">☰<br>Menú</div>
    </div>
    """, unsafe_allow_html=True)

# Espaciador final para que el contenido no quede oculto tras el menú inferior
st.markdown('<div style="height: 100px;"></div>', unsafe_allow_html=True)
