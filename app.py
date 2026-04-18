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

# 2. CSS DE ALTA DENSIDAD VISUAL
st.markdown("""
    <style>
    .stApp { background-color: #0b0e11; }
    header {visibility: hidden;}
    
    /* BARRA SUPERIOR FIJA Y DELGADA */
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
        padding: 0 10px;
        z-index: 1000;
        border-bottom: 1px solid #2d343f;
    }

    /* REJILLA COMPACTA: 5 COLUMNAS EN MÓVIL */
    div[data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: wrap !important;
        gap: 4px !important;
        justify-content: flex-start;
    }

    div[data-testid="column"] {
        width: 19% !important; /* Aproximadamente 5 por fila */
        flex: 1 1 19% !important;
        min-width: 65px !important;
        margin-bottom: 5px;
    }

    /* MINI TARJETAS DE JUEGO */
    [data-testid="stImage"] img {
        border-radius: 4px !important;
        aspect-ratio: 1 / 1;
        object-fit: cover;
    }
    
    /* BOTÓN JUGAR ULTRA COMPACTO */
    .stButton > button {
        background-color: #76b82a !important;
        color: white !important;
        font-size: 7px !important;
        padding: 0px !important;
        height: 18px !important;
        min-height: 18px !important;
        border-radius: 2px !important;
        border: none !important;
        text-transform: uppercase;
        font-weight: bold;
    }

    .section-label {
        color: #5f6a75;
        font-size: 10px;
        font-weight: bold;
        margin: 8px 0 4px 5px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. LÓGICA DE USUARIO Y PERFIL
if 'saldo' not in st.session_state: st.session_state.saldo = 5000.0

@st.dialog("Cuenta")
def mostrar_perfil():
    st.write(f"### 👤 Manuel Gómez")
    st.divider()
    st.button("💰 Depósitos", use_container_width=True)
    st.button("💸 Retiros", use_container_width=True)
    if st.button("🚪 Salir", type="primary", use_container_width=True):
        st.session_state.clear()
        st.rerun()

# 4. HEADER (LOGO Y SALDO)
h1, h2 = st.columns([1, 1])
with h1:
    # URL Directa para que el logo siempre cargue
    st.image("https://raw.githubusercontent.com/ManuelG-Prog/casino-demo/principal/logo.PNG", width=90)
with h2:
    st.markdown(f"""
        <div style="display: flex; justify-content: flex-end; align-items: center; height: 50px;">
            <div style="background:#2d343f; color:white; padding:2px 6px; border-radius:3px; font-weight:bold; font-size:11px; margin-right:5px; border:1px solid #3e4652;">
                ${st.session_state.saldo:,.2f}
            </div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("👤", key="btn_perfil"):
        mostrar_perfil()

# 5. BANNER Y SECCIONES
st.image("https://images.unsplash.com/photo-1518623489648-a173ef7824f3?w=1200", use_container_width=True)

def render_grid(titulo, n_items):
    st.markdown(f"<div class='section-label'>{titulo}</div>", unsafe_allow_html=True)
    img_placeholder = "https://images.unsplash.com/photo-1596711762462-850f28584813?w=150"
    
    # Creamos la cuadrícula de 5 columnas
    for fila in range(0, n_items, 5):
        cols = st.columns(5)
        for i in range(5):
            if (fila + i) < n_items:
                with cols[i]:
                    st.image(img_placeholder, use_container_width=True)
                    st.button("Jugar", key=f"p_{titulo}_{fila+i}")

# Renderizamos dos secciones densas
render_grid("Populares", 10)
render_grid("Nuevos Lanzamientos", 5)
