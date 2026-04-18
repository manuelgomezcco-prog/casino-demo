import streamlit as st
import pandas as pd
import os

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="Fortuna MX",
    page_icon="🍀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. CSS ESTILO CASINO PREMIUM
st.markdown("""
    <style>
    .stApp { background-color: #0b0e11; }
    header {visibility: hidden;}
    
    /* BARRA SUPERIOR SLIM */
    .nav-bar {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        height: 50px;
        background-color: #1a1f26;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 15px;
        z-index: 1000;
        border-bottom: 1px solid #2d343f;
    }
    
    .logo-container img {
        height: 30px !important;
        width: auto !important;
    }

    .user-stats {
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .balance-box {
        background-color: #2d343f;
        color: #ffffff;
        padding: 2px 12px;
        border-radius: 4px;
        font-weight: bold;
        font-size: 14px;
        border: 1px solid #3e4652;
    }

    /* REJILLA DE JUEGOS COMPACTA (4 EN MÓVIL) */
    div[data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        gap: 6px !important;
        overflow-x: auto;
        padding-bottom: 10px;
    }

    div[data-testid="column"] {
        width: 23% !important;
        flex: 1 1 23% !important;
        min-width: 80px !important;
    }

    /* ESTILO DE TARJETAS */
    .stImage img {
        border-radius: 8px !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }

    /* BOTONES TIPO WINPOT */
    .stButton > button {
        width: 100%;
        background-color: #76b82a !important; /* Verde Winpot */
        color: white !important;
        border: none !important;
        font-size: 10px !important;
        padding: 2px !important;
        border-radius: 4px !important;
        text-transform: uppercase;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. BARRA DE NAVEGACIÓN (LOGO + SALDO)
if 'saldo' not in st.session_state: st.session_state.saldo = 5000.0

# Inyectamos la barra superior manualmente para control total
st.markdown(f"""
    <div class="nav-bar">
        <div class="logo-container">
            <img src="https://raw.githubusercontent.com/ManuelG-Prog/casino-demo/principal/logo.PNG">
        </div>
        <div class="user-stats">
            <div class="balance-box">${st.session_state.saldo:,.2f}</div>
            <div style="color:#D4AF37; font-size:20px;">👤</div>
        </div>
    </div>
    <div style="margin-top: 60px;"></div>
""", unsafe_allow_html=True)

# 4. BANNER PRINCIPAL
st.image("https://images.unsplash.com/photo-1518623489648-a173ef7824f3?w=1200", use_container_width=True)

# 5. SECCIONES DE JUEGOS
def crear_fila_juegos(titulo, imagenes):
    st.markdown(f"<h5 style='color:white; margin: 15px 0 10px 0; font-size:14px;'>{titulo}</h5>", unsafe_allow_html=True)
    cols = st.columns(len(imagenes))
    for i, img_url in enumerate(imagenes):
        with cols[i]:
            st.image(img_url, use_container_width=True)
            if st.button("Jugar", key=f"{titulo}_{i}"):
                st.session_state.saldo -= 10.0
                st.rerun()

# Ejemplo de filas
juegos_urls = [
    "https://images.unsplash.com/photo-1596711762462-850f28584813?w=300",
    "https://images.unsplash.com/photo-1503197979108-c824168d51a8?w=300",
    "https://images.unsplash.com/photo-1606167668584-78701c57f13d?w=300",
    "https://images.unsplash.com/photo-1511193311914-0346f16efe90?w=300"
]

crear_fila_juegos("SIGUE JUGANDO", juegos_urls)
crear_fila_juegos("FORTUNA POPULAR", juegos_urls)
