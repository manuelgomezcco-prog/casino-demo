import streamlit as st
import pandas as pd
import time

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="Fortuna MX - Casino",
    page_icon="🍀",
    layout="wide"
)

# 2. ESTILOS CSS BLINDADOS (Dark Mode & Gold)
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
    }
    .main-logo {
        font-size: 80px;
        text-align: center;
        margin-bottom: 0px;
    }
    .gold-title {
        color: #D4AF37;
        text-align: center;
        font-family: 'Helvetica', sans-serif;
        font-weight: 800;
        font-size: 40px;
        margin-top: -20px;
        letter-spacing: 2px;
    }
    .balance-box {
        background: linear-gradient(135deg, #D4AF37 0%, #B8860B 100%);
        color: black;
        padding: 15px;
        border-radius: 15px;
        text-align: center;
        font-weight: bold;
        font-size: 22px;
        box-shadow: 0px 4px 15px rgba(212, 175, 55, 0.3);
        margin-bottom: 25px;
    }
    /* Estilo de tarjetas de juego */
    .game-container {
        background-color: #1f2630;
        border-radius: 15px;
        padding: 10px;
        border: 1px solid #333;
    }
    div.stButton > button {
        background-color: #D4AF37;
        color: black;
        font-weight: bold;
        border-radius: 10px;
        border: none;
        padding: 10px;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #ffffff;
        color: black;
        transform: translateY(-2px);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. ESTADO DE LA SESIÓN
if 'saldo' not in st.session_state:
    st.session_state.saldo = 5000.0
if 'ggr' not in st.session_state:
    st.session_state.ggr = 0.0
if 'logs' not in st.session_state:
    st.session_state.logs = []

# --- NAVEGACIÓN ---
st.sidebar.markdown("<h2 style='color: #D4AF37;'>♣️ FORTUNA MX</h2>", unsafe_allow_html=True)
menu = st.sidebar.radio("Ir a:", ["🎰 Lobby de Juegos", "💰 Cajero", "📊 Panel Admin"])

# --- LOBBY DE JUEGOS ---
if menu == "🎰 Lobby de Juegos":
    # Logo Respaldo (Emoji + Texto Estilizado)
    st.markdown("<div class='main-logo'>🍀</div>", unsafe_allow_html=True)
    st.markdown("<h1 class='gold-title'>FORTUNA MX</h1>", unsafe_allow_html=True)
    
    st.markdown(f"<div class='balance-box'>SALDO DISPONIBLE: ${st.session_state.saldo:,.2f}</div>", unsafe_allow_html=True)

    st.subheader("🔥 Los más jugados")
    
    # Juegos con imágenes estables de Unsplash (Servidor profesional)
    juegos = [
        {"n": "Fruity Fortune", "id": "play1", "img": "https://images.unsplash.com/photo-1596711762462-850f28584813?auto=format&fit=crop&q=80&w=400"},
        {"n": "Ancient Zeus", "id": "play2", "img": "https://images.unsplash.com/photo-1503197979108-c824168d51a8?auto=format&fit=crop&q=80&w=400"},
        {"n": "Royal Roulette", "id": "play3", "img": "https://images.unsplash.com/photo-1606167668584-78701c57f13d?auto=format&fit=crop&q=80&w=400"},
        {"n": "Blackjack Gold", "id": "play4", "img": "https://images.unsplash.com/photo-1511193311914-0346f16efe90?auto=format&fit=crop&q=80&w=400"}
    ]

    cols = st.columns(2)
    for i, j in enumerate(juegos):
        with cols[i % 2]:
            st.image(j["img"], use_container_width=True)
            st.markdown(f"**{j['n']}**")
            if st.button(f"APOSTAR $50", key=j["id"], use_container_width=True):
                if st.session_state.saldo >= 50:
                    st.session_state.saldo -= 50
                    st.session_state.ggr += 10.0
                    st.session_state.logs.insert(0, {"Hora": time.strftime("%H:%M:%S"), "Juego": j['n'], "Acción": "Apuesta -$50"})
                    st.toast(f"¡Girando en {j['n']}!")
                    time.sleep(0.3)
                    st.rerun()
                else:
                    st.error("Recarga saldo en el Cajero")

# --- CAJERO ---
elif menu == "💰 Cajero":
    st.markdown("<h2 class='gold-title'>DEPÓSITOS</h2>", unsafe_allow_html=True)
    with st.container(border=True):
        monto = st.select_slider("Selecciona monto a recargar:", options=[200, 500, 1000, 2000, 5000])
        if st.button("RECARGAR AHORA", use_container_width=True):
            with st.spinner("Conectando con el banco..."):
                time.sleep(1.2)
                st.session_state.saldo += monto
                st.balloons()
                st.success(f"¡Has cargado ${monto} MXN!")
                time.sleep(1)
                st.rerun()

# --- ADMIN ---
else:
    st.title("📊 Auditoría Fortuna MX")
    col1, col2 = st.columns(2)
    col1.metric("GGR (Ganancia)", f"${st.session_state.ggr:,.2f}")
    col2.metric("Sesiones", "Activa")
    
    st.divider()
    if st.session_state.logs:
        st.table(pd.DataFrame(st.session_state.logs))
