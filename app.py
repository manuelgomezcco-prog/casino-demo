import streamlit as st
import pandas as pd
import time
import os

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="Fortuna MX - Elite Gaming",
    page_icon="🎰",
    layout="wide"
)

# 2. ESTILOS CSS
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .gold-title {
        color: #D4AF37;
        text-align: center;
        font-family: 'Helvetica', sans-serif;
        font-weight: bold;
        font-size: 40px;
        margin-top: -15px;
        letter-spacing: 2px;
    }
    .balance-box {
        background: linear-gradient(135deg, #D4AF37 0%, #B8860B 100%);
        color: black;
        padding: 15px;
        border-radius: 15px;
        text-align: center;
        font-weight: bold;
        font-size: 24px;
        box-shadow: 0px 4px 15px rgba(212, 175, 55, 0.4);
        margin-bottom: 25px;
    }
    div.stButton > button {
        background-color: #D4AF37;
        color: black;
        font-weight: bold;
        border-radius: 10px;
        border: none;
        padding: 12px;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. ESTADO DE SESIÓN
if 'saldo' not in st.session_state: st.session_state.saldo = 5000.0
if 'ggr' not in st.session_state: st.session_state.ggr = 0.0
if 'logs' not in st.session_state: st.session_state.logs = []

# --- NAVEGACIÓN ---
menu = st.sidebar.radio("Ir a:", ["🎰 Lobby", "💰 Cajero", "📊 Admin"])

# --- LOBBY ---
if menu == "🎰 Lobby":
    col_a, col_b, col_c = st.columns([1, 2, 1])
    with col_b:
        # AJUSTE SEGÚN TU GITHUB: Usamos logo.PNG con mayúsculas
        nombre_logo = "logo.PNG" 
        
        if os.path.exists(nombre_logo):
            st.image(nombre_logo, use_container_width=True)
        else:
            st.error("Aún no detecto el archivo logo.PNG")
            
        st.markdown("<h1 class='gold-title'>FORTUNA MX</h1>", unsafe_allow_html=True)
    
    st.markdown(f"<div class='balance-box'>SALDO: ${st.session_state.saldo:,.2f} MXN</div>", unsafe_allow_html=True)

    st.subheader("🔥 Los más jugados")
    juegos = [
        {"n": "Fruity Fortune", "img": "https://images.unsplash.com/photo-1596711762462-850f28584813?w=500"},
        {"n": "Ancient Zeus", "img": "https://images.unsplash.com/photo-1503197979108-c824168d51a8?w=500"}
    ]

    cols = st.columns(2)
    for i, j in enumerate(juegos):
        with cols[i % 2]:
            with st.container(border=True):
                st.image(j["img"], use_container_width=True)
                if st.button(f"APOSTAR $50", key=f"b_{i}"):
                    if st.session_state.saldo >= 50:
                        st.session_state.saldo -= 50
                        st.session_state.ggr += 12.5
                        st.rerun()

elif menu == "💰 Cajero":
    st.markdown("<h2 class='gold-title'>CAJERO</h2>", unsafe_allow_html=True)
    monto = st.number_input("Monto:", 100)
    if st.button("DEPOSITAR"):
        st.session_state.saldo += monto
        st.rerun()
else:
    st.metric("GGR (Ganancia Casa)", f"${st.session_state.ggr:,.2f}")
