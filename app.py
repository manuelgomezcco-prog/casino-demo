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

# 2. ESTILOS CSS PERSONALIZADOS (MODO OSCURO Y DORADO)
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
    }
    .gold-title {
        color: #D4AF37;
        text-align: center;
        font-family: 'Helvetica', sans-serif;
        font-weight: bold;
        font-size: 38px;
        margin-top: -10px;
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
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #ffffff;
        color: black;
        transform: scale(1.02);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. ESTADO DE SESIÓN
if 'saldo' not in st.session_state:
    st.session_state.saldo = 5000.0
if 'ggr' not in st.session_state:
    st.session_state.ggr = 0.0
if 'logs' not in st.session_state:
    st.session_state.logs = []

# --- NAVEGACIÓN ---
menu = st.sidebar.radio("Navegación:", ["🎰 Lobby de Juegos", "💰 Cajero", "📊 Admin Panel"])

# --- LOBBY DE JUEGOS ---
if menu == "🎰 Lobby de Juegos":
    col_a, col_b, col_c = st.columns([1, 2, 1])
    with col_b:
        # Cargamos el logo que ya confirmamos que funciona
        st.image("logo.PNG", use_container_width=True) #
        st.markdown("<h1 class='gold-title'>FORTUNA MX</h1>", unsafe_allow_html=True)
    
    st.divider()

    # Caja de Saldo
    st.markdown(f"<div class='balance-box'>SALDO: ${st.session_state.saldo:,.2f} MXN</div>", unsafe_allow_html=True)

    st.subheader("🔥 Juegos Destacados")
    
    # Juegos con imágenes de alta calidad
    juegos = [
        {"n": "Fruity Fortune", "img": "https://images.unsplash.com/photo-1596711762462-850f28584813?w=600"},
        {"n": "Ancient Zeus", "img": "https://images.unsplash.com/photo-1503197979108-c824168d51a8?w=600"},
        {"n": "Royal Roulette", "img": "https://images.unsplash.com/photo-1606167668584-78701c57f13d?w=600"},
        {"n": "Blackjack Gold", "img": "https://images.unsplash.com/photo-1511193311914-0346f16efe90?w=600"}
    ]

    cols = st.columns(2)
    for i, j in enumerate(juegos):
        with cols[i % 2]:
            with st.container(border=True):
                st.image(j["img"], use_container_width=True)
                st.write(f"**{j['n']}**")
                if st.button(f"APOSTAR $50", key=f"btn_{i}"):
                    if st.session_state.saldo >= 50:
                        st.session_state.saldo -= 50
                        st.session_state.ggr += 12.50
                        st.session_state.logs.insert(0, {"Hora": time.strftime("%H:%M:%S"), "Juego": j['n'], "Acción": "-$50.00"})
                        st.toast(f"¡Suerte en {j['n']}!")
                        time.sleep(0.3)
                        st.rerun()
                    else:
                        st.error("Recarga saldo en el Cajero")

# --- CAJERO ---
elif menu == "💰 Cajero":
    st.markdown("<h2 class='gold-title'>CAJERO</h2>", unsafe_allow_html=True)
    with st.container(border=True):
        monto = st.select_slider("Monto a depositar:", options=[200, 500, 1000, 2000, 5000])
        if st.button("RECARGAR AHORA"):
            with st.spinner("Procesando pago..."):
                time.sleep(1)
                st.session_state.saldo += monto
                st.balloons()
                st.success(f"¡Has cargado ${monto} MXN!")
                time.sleep(1)
                st.rerun()

# --- PANEL ADMIN ---
else:
    st.title("📊 Panel Admin")
    st.metric("GGR (Ganancia Casa)", f"${st.session_state.ggr:,.2f}")
    st.write("### Historial")
    if st.session_state.logs:
        st.table(pd.DataFrame(st.session_state.logs))
