import streamlit as st
import pandas as pd
import time

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="Fortuna MX - Elite Gaming",
    page_icon="🍀",
    layout="wide"
)

# 2. ESTILOS CSS PARA UNA INTERFAZ "PREMIUM"
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
    }
    .gold-title {
        color: #D4AF37;
        text-align: center;
        font-family: 'Serif';
        font-weight: bold;
        font-size: 36px;
        margin-top: -20px;
    }
    .balance-box {
        background-color: #D4AF37;
        color: black;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        font-weight: bold;
        font-size: 20px;
        margin-bottom: 20px;
    }
    div.stButton > button {
        background-color: #D4AF37;
        color: black;
        font-weight: bold;
        border-radius: 8px;
        border: none;
        width: 100%;
    }
    div.stButton > button:hover {
        background-color: #B8860B;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. DATOS (Simulación de DB)
if 'saldo' not in st.session_state:
    st.session_state.saldo = 5000.0
if 'ggr' not in st.session_state:
    st.session_state.ggr = 0.0
if 'logs' not in st.session_state:
    st.session_state.logs = []

# --- NAVEGACIÓN LATERAL ---
st.sidebar.markdown("<h2 style='color: #D4AF37;'>♣️ FORTUNA MX</h2>", unsafe_allow_html=True)
pagina = st.sidebar.radio("Menú Principal", ["🎰 Lobby de Juegos", "💰 Cajero / Depósitos", "📊 Admin Panel"])

# --- LÓGICA DEL LOBBY ---
if pagina == "🎰 Lobby de Juegos":
    # Header con Logo y Título
    col_a, col_b, col_c = st.columns([1, 2, 1])
    with col_b:
        # Logo del Trébol Dorado (URL de respaldo estable)
        st.image("https://i.ibb.co/3WfK9F1/fortuna-mx-logo.png", use_container_width=True)
        st.markdown("<h1 class='gold-title'>FORTUNA MX</h1>", unsafe_allow_html=True)
    
    st.divider()

    # Saldo destacado
    st.markdown(f"<div class='balance-box'>TU SALDO: ${st.session_state.saldo:,.2f} MXN</div>", unsafe_allow_html=True)

    st.markdown("### 🔥 Juegos más populares")
    
    # Definición de juegos con imágenes de alta calidad
    juegos = [
        {"nombre": "Sweet Bonanza", "img": "https://img.freepik.com/premium-photo/colorful-candies-sweets-background_800531-152.jpg", "prov": "Pragmatic"},
        {"nombre": "Gates of Olympus", "img": "https://img.freepik.com/premium-photo/zeus-god-thunder-generative-ai_170984-1144.jpg", "prov": "Pragmatic"},
        {"nombre": "Lightning Roulette", "img": "https://img.freepik.com/free-photo/casino-roulette-wheel-with-chips-poker-cards-dark-background_155003-14545.jpg", "prov": "Evolution"},
        {"nombre": "Blackjack VIP", "img": "https://img.freepik.com/free-photo/poker-chips-cards-green-table_155003-14540.jpg", "prov": "Evolution"}
    ]

    # Grid de juegos
    cols = st.columns(2)
    for idx, juego in enumerate(juegos):
        with cols[idx % 2]:
            with st.container(border=True):
                st.image(juego["img"], use_container_width=True)
                st.write(f"**{juego['nombre']}**")
                st.caption(f"Proveedor: {juego['prov']}")
                if st.button(f"APOSTAR $50", key=f"play_{idx}"):
                    if st.session_state.saldo >= 50:
                        st.session_state.saldo -= 50
                        st.session_state.ggr += 7.50 # Margen de casa
                        st.session_state.logs.insert(0, {"Hora": time.strftime("%H:%M:%S"), "Juego": juego['nombre'], "Monto": "-$50.00"})
                        st.toast(f"¡Suerte en {juego['nombre']}!")
                        time.sleep(0.4)
                        st.rerun()
                    else:
                        st.error("Saldo insuficiente")

# --- CAJERO ---
elif pagina == "💰 Cajero / Depósitos":
    st.markdown("<h2 class='gold-title'>CAJERO</h2>", unsafe_allow_html=True)
    
    with st.container(border=True):
        monto = st.number_input("Monto a depositar (MXN)", min_value=100, step=500, value=1000)
        metodo = st.selectbox("Selecciona tu método", ["SPEI", "Tarjeta Débito/Crédito", "OXXO Pay"])
        
        if st.button("CONFIRMAR DEPÓSITO"):
            with st.spinner("Procesando pago seguro..."):
                time.sleep(1.5)
                st.session_state.saldo += monto
                st.success(f"¡Has depositado ${monto:,.2f} con éxito!")
                st.balloons()
                time.sleep(1)
                st.rerun()

# --- ADMIN PANEL ---
else:
    st.title("📊 Panel Administrativo - Fortuna MX")
    
    m1, m2 = st.columns(2)
    m1.metric("GGR Acumulado", f"${st.session_state.ggr:,.2f} MXN")
    m2.metric("Usuarios Conectados", "1")
    
    st.divider()
    st.write("### Historial de Movimientos")
    if st.session_state.logs:
        st.table(pd.DataFrame(st.session_state.logs))
    else:
        st.info("No hay transacciones registradas.")

# --- FOOTER ---
st.sidebar.divider()
st.sidebar.caption("Fortuna MX © 2026 | Desarrollo Seguro")
