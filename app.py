import streamlit as st
import pandas as pd
import time
import os

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="Fortuna MX - Elite",
    page_icon="🍀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. CSS PARA DISEÑO TIPO WINPOT (MODERNO Y COMPACTO)
st.markdown("""
    <style>
    /* Fondo oscuro profundo */
    .stApp { background-color: #0b0e11; }
    header {visibility: hidden;}
    
    /* ENCABEZADO TIPO APP BAR */
    .top-bar {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        height: 60px;
        background-color: #1a1f26;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 15px;
        z-index: 999;
        border-bottom: 1px solid #2d343f;
    }
    
    /* LOGO POSICIONADO A LA IZQUIERDA */
    .logo-img {
        height: 40px !important;
        width: auto !important;
    }

    /* CONTENEDOR DE ACCIONES (DEPÓSITO Y SALDO) */
    .header-actions {
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .balance-tag {
        background-color: #2d343f;
        color: white;
        padding: 4px 10px;
        border-radius: 4px;
        font-weight: bold;
        font-size: 14px;
        border: 1px solid #3e4652;
    }

    /* REJILLA DE JUEGOS (ESTILO WINPOT) */
    div[data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        gap: 8px !important;
        overflow-x: auto;
    }

    div[data-testid="column"] {
        width: 24% !important; /* 4 juegos por fila */
        flex: 1 1 24% !important;
        min-width: 85px !important;
    }

    /* TARJETAS DE JUEGO */
    .game-card img {
        border-radius: 12px;
        border: 2px solid #2d343f;
        transition: transform 0.2s;
    }
    .game-card img:hover { transform: scale(1.05); }

    /* BOTÓN DE DEPÓSITO VERDE WINPOT */
    .stButton > button {
        background-color: #76b82a !important;
        color: white !important;
        border: none !important;
        font-weight: bold !important;
        border-radius: 4px !important;
        padding: 5px 15px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. ESTADO DE SESIÓN
if 'saldo' not in st.session_state: st.session_state.saldo = 5000.0

# --- COMPONENTE DE ENCABEZADO ---
st.markdown(f"""
    <div class="top-bar">
        <div style="display:flex; align-items:center;">
            <img src="https://raw.githubusercontent.com/{os.getenv('GITHUB_REPOSITORY', 'ManuelG-Prog/casino-demo')}/principal/logo.PNG" class="logo-img">
        </div>
        <div class="header-actions">
            <div class="balance-tag">${st.session_state.saldo:,.2f}</div>
            <div style="font-size:22px;">👤</div>
        </div>
    </div>
    <div style="margin-top: 80px;"></div>
""", unsafe_allow_html=True)

# --- BANNER PROMOCIONAL ---
st.image("https://images.unsplash.com/photo-1518623489648-a173ef7824f3?w=1200", use_container_width=True)
st.markdown("<h4 style='color:white; margin: 15px 0 5px 0;'>SIGUE JUGANDO</h4>", unsafe_allow_html=True)

# --- REJILLA DE JUEGOS (ESTILO WINPOT POPULAR) ---
juegos = [
    {"n": "Spicy Fruits", "img": "https://images.unsplash.com/photo-1596711762462-850f28584813?w=300"},
    {"n": "Shining Crown", "img": "https://images.unsplash.com/photo-1503197979108-c824168d51a8?w=300"},
    {"n": "Leprechaun", "img": "https://images.unsplash.com/photo-1606167668584-78701c57f13d?w=300"},
    {"n": "Voltage Rapid", "img": "https://images.unsplash.com/photo-1511193311914-0346f16efe90?w=300"}
]

# Primera Fila (Sigue Jugando)
cols = st.columns(len(juegos))
for i, juego in enumerate(juegos):
    with cols[i]:
        st.markdown('<div class="game-card">', unsafe_allow_html=True)
        st.image(juego["img"], use_container_width=True)
        if st.button("JUGAR", key=f"j_{i}"):
            if st.session_state.saldo >= 50:
                st.session_state.saldo -= 50
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<h4 style='color:white; margin: 20px 0 5px 0;'>WINPOT POPULAR</h4>", unsafe_allow_html=True)

# Segunda Fila (Popular)
cols2 = st.columns(len(juegos))
for i, juego in enumerate(juegos):
    with cols2[i]:
        st.image(juego["img"], use_container_width=True)
        st.button("INFO", key=f"inf_{i}")
