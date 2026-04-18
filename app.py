import streamlit as st

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="Fortuna MX",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. CSS PARA ELIMINAR ERRORES VISUALES Y CORREGIR EL HEADER
st.markdown("""
    <style>
    /* Fondo oscuro y limpieza de espacios */
    .stApp { background-color: #0b1118; }
    header {visibility: hidden;}
    [data-testid="stHeader"] {display: none;}
    div.block-container {padding-top: 0rem; padding-bottom: 5rem;}

    /* HEADER PERSONALIZADO */
    .header-wrapper {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 15px;
        background-color: #1a1f26;
        border-bottom: 1px solid #2d343f;
        margin-bottom: 20px;
    }

    .logo-box img {
        height: 45px !important; /* Altura fija para evitar que desaparezca */
        width: auto;
    }

    .user-info {
        display: flex;
        align-items: center;
        gap: 10px;
    }

    /* Botón Depositar */
    .dep-button {
        background-color: #76b82a;
        color: #000 !important;
        padding: 8px 16px;
        border-radius: 8px;
        font-weight: bold;
        font-size: 14px;
        text-decoration: none;
    }

    /* Badge de Saldo */
    .bal-badge {
        background-color: #2d343f;
        color: #ffffff;
        padding: 8px 12px;
        border-radius: 8px;
        font-weight: bold;
        font-size: 14px;
        border: 1px solid #3e4652;
    }

    /* Quitar cuadros vacíos y ceros */
    [data-testid="stVerticalBlock"] > div:empty {display: none;}
    
    /* Títulos de sección */
    .sect-title {
        color: #ffffff;
        font-size: 16px;
        font-weight: bold;
        margin: 20px 0 10px 0;
        text-transform: uppercase;
    }

    /* Menú Inferior Fijo */
    .nav-bottom {
        position: fixed;
        bottom: 0; left: 0; right: 0;
        background-color: #1a1f26;
        display: flex;
        justify-content: space-around;
        padding: 12px 0;
        border-top: 1px solid #2d343f;
        z-index: 1000;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. HEADER (CONSTRUCCIÓN MANUAL PARA EVITAR ERRORES)
# IMPORTANTE: He cambiado la URL a una que GitHub sirve de forma más estable
logo_url = "https://raw.githubusercontent.com/ManuelG-Prog/casino-demo/principal/logo.PNG"

st.markdown(f"""
    <div class="header-wrapper">
        <div class="logo-box">
            <img src="{logo_logo_url if 'logo_logo_url' in locals() else logo_url}">
        </div>
        <div class="user-info">
            <a class="dep-button">📥 Depositar</a>
            <div class="bal-badge">$ 5,000.00</div>
            <div style="font-size: 24px; color: #8a96a3;">👤</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 4. CONTENIDO PRINCIPAL
# Banner
st.image("https://images.unsplash.com/photo-1518623489648-a173ef7824f3?w=1200", use_container_width=True)

# Sección de Juegos
st.markdown('<div class="sect-title">Sigue Jugando</div>', unsafe_allow_html=True)

# Cuadrícula limpia de 2 columnas
c1, c2 = st.columns(2)
img_game = "https://images.unsplash.com/photo-1596711762462-850f28584813?w=400"

with c1:
    st.image(img_game, use_container_width=True)
    st.button("JUGAR", key="g1", use_container_width=True)

with c2:
    st.image(img_game, use_container_width=True)
    st.button("JUGAR", key="g2", use_container_width=True)

# 5. MENÚ INFERIOR
st.markdown("""
    <div class="nav-bottom">
        <div style="text-align: center; color: white; font-size: 11px;">🏠<br>Inicio</div>
        <div style="text-align: center; color: #76b82a; font-size: 11px;">📥<br>Depositar</div>
        <div style="text-align: center; color: white; font-size: 11px;">🎰<br>Slots</div>
        <div style="text-align: center; color: white; font-size: 11px;">☰<br>Menú</div>
    </div>
    <div style="height: 80px;"></div>
    """, unsafe_allow_html=True)
