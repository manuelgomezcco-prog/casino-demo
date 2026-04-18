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

# 2. CSS AVANZADO: FORZADO DE REJILLA MÓVIL Y LOGO GRANDE
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    
    /* LOGOTIPO: Forzamos tamaño para que luzca espectacular */
    [data-testid="stImage"] img {
        max-width: none !important;
        width: 220px !important; 
    }

    .gold-title {
        color: #D4AF37;
        text-align: center;
        font-family: 'Helvetica', sans-serif;
        font-weight: bold;
        font-size: 32px;
        margin-top: 10px;
    }

    /* BARRA DE USUARIO Y BOTÓN DE PERFIL */
    .user-section {
        display: flex;
        flex-direction: column;
        align-items: flex-end;
        gap: 5px;
    }
    
    .user-bar-mini {
        background-color: #1f2630;
        padding: 4px 12px;
        border-radius: 15px;
        display: flex;
        align-items: center;
        border: 1px solid #D4AF37;
    }
    
    .user-balance-mini {
        color: #D4AF37;
        font-weight: bold;
        font-size: 14px;
        margin-right: 8px;
    }

    /* --- SOLUCIÓN DEFINITIVA PARA FILAS DE 3 EN MÓVIL --- */
    /* Forzamos al contenedor de columnas a no saltar de línea */
    div[data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important; /* Evita que los juegos se vayan abajo */
        gap: 10px !important;
    }

    /* Ajustamos el ancho de cada columna al 33% fijo */
    div[data-testid="column"] {
        width: 33% !important;
        flex: 1 1 33% !important;
        min-width: 33% !important;
    }

    /* Ajuste de botones para que quepan en el espacio pequeño */
    div.stButton > button {
        font-size: 10px !important;
        padding: 5px !important;
        background-color: #D4AF37;
        color: black;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. ESTADO DE SESIÓN
if 'saldo' not in st.session_state: st.session_state.saldo = 5000.0
if 'logs' not in st.session_state: st.session_state.logs = []

# --- DIÁLOGO DE PERFIL ---
@st.dialog("Mi Cuenta")
def mostrar_perfil():
    st.write("### 👤 Manuel Gómez")
    if st.button("Cerrar Sesión", type="primary"):
        st.session_state.clear()
        st.rerun()

# --- BARRA SUPERIOR (LOGO Y PERFIL) ---
col_logo, col_user = st.columns([2, 1])

with col_logo:
    if os.path.exists("logo.PNG"):
        st.image("logo.PNG") # El CSS arriba le da el tamaño de 220px

with col_user:
    st.markdown('<div class="user-section">', unsafe_allow_html=True)
    if st.button("Mi Perfil", key="btn_p"):
        mostrar_perfil()
    st.markdown(f"""
        <div class="user-bar-mini">
            <span class="user-balance-mini">${st.session_state.saldo:,.2f}</span>
            <span style="font-size: 16px;">👤</span>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<h1 class='gold-title'>FORTUNA MX</h1>", unsafe_allow_html=True)
st.divider()

# --- LOBBY DE JUEGOS (OBLIGATORIO 3 POR FILA) ---
st.subheader("🔥 Destacados")

juegos = [
    {"n": "Fruity Fortune", "img": "https://images.unsplash.com/photo-1596711762462-850f28584813?w=400"},
    {"n": "Ancient Zeus", "img": "https://images.unsplash.com/photo-1503197979108-c824168d51a8?w=400"},
    {"n": "Royal Roulette", "img": "https://images.unsplash.com/photo-1606167668584-78701c57f13d?w=400"},
    {"n": "Blackjack", "img": "https://images.unsplash.com/photo-1511193311914-0346f16efe90?w=400"},
    {"n": "Slots Gold", "img": "https://images.unsplash.com/photo-1596711762462-850f28584813?w=400"},
    {"n": "Poker", "img": "https://images.unsplash.com/photo-1511193311914-0346f16efe90?w=400"}
]

# Dibujamos en filas de 3
for i in range(0, len(juegos), 3):
    cols = st.columns(3) # Creamos 3 columnas por cada fila
    for j in range(3):
        if i + j < len(juegos):
            juego = juegos[i + j]
            with cols[j]:
                # Usamos un contenedor visual compacto
                st.image(juego["img"], use_container_width=True)
                st.markdown(f"<p style='text-align:center; font-size:9px; font-weight:bold; color:white;'>{juego['n']}</p>", unsafe_allow_html=True)
                if st.button("JUGAR", key=f"j_{i+j}"):
                    if st.session_state.saldo >= 50:
                        st.session_state.saldo -= 50
                        st.toast(f"¡Suerte en {juego['n']}!")
                        st.rerun()
