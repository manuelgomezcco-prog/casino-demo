import streamlit as st
import pandas as pd
import time
import os

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="Fortuna MX - Elite Gaming",
    page_icon="🍀",
    layout="wide"
)

# 2. CSS DE ALTA PRECISIÓN PARA LOGO Y REJILLA MÓVIL
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    
    /* LOGOTIPO: Forzamos tamaño original y alineación */
    [data-testid="stImage"] img {
        max-width: none !important;
        width: 180px !important; /* Ajustado para que luzca imponente */
    }

    /* TÍTULO PRINCIPAL */
    .gold-title {
        color: #D4AF37;
        text-align: center;
        font-family: 'Helvetica', sans-serif;
        font-weight: bold;
        font-size: 30px;
        margin-top: 10px;
    }

    /* SECCIÓN DE USUARIO COMPACTA */
    .user-section {
        display: flex;
        flex-direction: column;
        align-items: flex-end;
        gap: 5px;
    }
    
    .user-bar-mini {
        background-color: #1f2630;
        padding: 4px 10px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        border: 1px solid #D4AF37;
    }
    
    .user-balance-mini {
        color: #D4AF37;
        font-weight: bold;
        font-size: 13px;
        margin-right: 5px;
    }

    /* --- SOLUCIÓN PARA 3 COLUMNAS EN MÓVIL --- */
    /* Forzamos al contenedor horizontal a no saltar de línea */
    div[data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important; 
        overflow-x: auto; /* Permite scroll si fuera necesario */
    }

    /* Cada columna ocupará exactamente el 33% */
    div[data-testid="column"] {
        width: 33% !important;
        flex: 1 1 33% !important;
        min-width: 33% !important;
    }

    /* Ajuste de botones JUGAR para que no se deformen */
    div.stButton > button {
        width: 100% !important;
        font-size: 10px !important;
        padding: 2px !important;
        background-color: #D4AF37;
        color: black;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. ESTADO DE SESIÓN
if 'saldo' not in st.session_state: st.session_state.saldo = 5000.0

# --- DIÁLOGO DE PERFIL ---
@st.dialog("Perfil")
def mostrar_perfil():
    st.write("### 👤 Mi Cuenta")
    st.write(f"Saldo: ${st.session_state.saldo:,.2f} MXN")
    if st.button("Cerrar Sesión", type="primary"):
        st.session_state.clear()
        st.rerun()

# --- BARRA SUPERIOR (LOGO IZQUIERDA | PERFIL DERECHA) ---
col_logo, col_user = st.columns([1, 1])

with col_logo:
    if os.path.exists("logo.PNG"):
        st.image("logo.PNG")

with col_user:
    st.markdown('<div class="user-section">', unsafe_allow_html=True)
    if st.button("Mi Perfil", key="btn_p"):
        mostrar_perfil()
    st.markdown(f"""
        <div class="user-bar-mini">
            <span class="user-balance-mini">${st.session_state.saldo:,.2f}</span>
            <span style="font-size: 14px;">👤</span>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<h1 class='gold-title'>FORTUNA MX</h1>", unsafe_allow_html=True)
st.divider()

# --- LOBBY CON REJILLA FORZADA ---
st.subheader("🔥 Destacados")

juegos = [
    {"n": "Fruity Fortune", "img": "https://images.unsplash.com/photo-1596711762462-850f28584813?w=400"},
    {"n": "Ancient Zeus", "img": "https://images.unsplash.com/photo-1503197979108-c824168d51a8?w=400"},
    {"n": "Royal Roulette", "img": "https://images.unsplash.com/photo-1606167668584-78701c57f13d?w=400"}
]

# Filas de 3 juegos
cols = st.columns(3)
for i in range(3):
    juego = juegos[i]
    with cols[i]:
        st.image(juego["img"], use_container_width=True)
        st.markdown(f"<p style='text-align:center; font-size:9px; font-weight:bold;'>{juego['n']}</p>", unsafe_allow_html=True)
        if st.button("JUGAR", key=f"play_{i}"):
            if st.session_state.saldo >= 50:
                st.session_state.saldo -= 50
                st.rerun()
