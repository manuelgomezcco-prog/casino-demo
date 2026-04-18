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

# 2. CSS DE ALTA DENSIDAD (ASPECTO PROFESIONAL)
st.markdown("""
    <style>
    .stApp { background-color: #0b0e11; }
    header {visibility: hidden;}
    
    /* BARRA SUPERIOR */
    .nav-bar {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        height: 55px;
        background-color: #1a1f26;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 10px;
        z-index: 1000;
        border-bottom: 1px solid #2d343f;
    }

    /* REJILLA DE JUEGOS COMPACTA (5 POR FILA EN MÓVIL) */
    div[data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: wrap !important; /* Ahora permite múltiples filas */
        gap: 6px !important;
        justify-content: center;
    }

    div[data-testid="column"] {
        width: 18% !important; /* Reducimos a un 18% para que quepan 5 por fila */
        flex: 1 1 18% !important;
        min-width: 70px !important; /* Tamaño mínimo para que no se pierda la imagen */
        margin-bottom: 10px;
    }

    /* AJUSTE DE IMÁGENES DE JUEGOS */
    [data-testid="stImage"] img {
        border-radius: 6px !important;
        transition: transform 0.2s;
    }
    
    /* BOTONES MINI */
    .stButton > button {
        background-color: #76b82a !important;
        color: white !important;
        font-size: 8px !important;
        padding: 1px !important;
        height: 20px !important;
        min-height: 20px !important;
        border-radius: 3px !important;
    }

    .section-title {
        color: #8a96a3;
        font-size: 11px;
        font-weight: bold;
        margin: 10px 0 5px 10px;
        text-transform: uppercase;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. LÓGICA DE PERFIL
@st.dialog("Mi Cuenta")
def menu_perfil():
    st.write(f"### 👤 Mi Perfil")
    st.button("💰 Depósito", use_container_width=True)
    st.button("💸 Retiro", use_container_width=True)
    if st.button("🚪 Salir", type="primary", use_container_width=True):
        st.session_state.clear()
        st.rerun()

# 4. HEADER
if 'saldo' not in st.session_state: st.session_state.saldo = 5000.0

t1, t2 = st.columns([1, 1])
with t1:
    st.image("https://raw.githubusercontent.com/ManuelG-Prog/casino-demo/principal/logo.PNG", width=110)
with t2:
    st.markdown(f"""
        <div style="display: flex; justify-content: flex-end; align-items: center; height: 70px;">
            <div style="background:#2d343f; color:white; padding:2px 8px; border-radius:4px; font-weight:bold; font-size:12px; margin-right:8px; border:1px solid #3e4652;">
                ${st.session_state.saldo:,.2f}
            </div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("👤", key="perfil_btn"):
        menu_perfil()

# 5. CONTENIDO (BANNER REDUCIDO)
st.image("https://images.unsplash.com/photo-1518623489648-a173ef7824f3?w=1200", use_container_width=True)

# 6. REJILLA DE JUEGOS (5 POR FILA)
st.markdown("<div class='section-title'>Populares</div>", unsafe_allow_html=True)

# Lista extendida de juegos para llenar la pantalla
juegos = [
    "https://images.unsplash.com/photo-1596711762462-850f28584813?w=200",
    "https://images.unsplash.com/photo-1503197979108-c824168d51a8?w=200",
    "https://images.unsplash.com/photo-1606167668584-78701c57f13d?w=200",
    "https://images.unsplash.com/photo-1511193311914-0346f16efe90?w=200",
    "https://images.unsplash.com/photo-1596711762462-850f28584813?w=200",
    "https://images.unsplash.com/photo-1503197979108-c824168d51a8?w=200",
    "https://images.unsplash.com/photo-1606167668584-78701c57f13d?w=200",
    "https://images.unsplash.com/photo-1511193311914-0346f16efe90?w=200",
    "https://images.unsplash.com/photo-1596711762462-850f28584813?w=200",
    "https://images.unsplash.com/photo-1503197979108-c824168d51a8?w=200"
]

# Crear filas de 5
for i in range(0, len(juegos), 5):
    cols = st.columns(5)
    for j in range(5):
        if i + j < len(juegos):
            with cols[j]:
                st.image(juegos[i+j], use_container_width=True)
                st.button("PLAY", key=f"play_{i+j}")
