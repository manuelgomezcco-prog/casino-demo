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
    /* Fondo general oscuro */
    .stApp {
        background-color: #0e1117;
    }
    /* Estilo para las tarjetas de juegos */
    .game-card {
        background-color: #1f2630;
        border-radius: 15px;
        padding: 10px;
        border: 1px solid #D4AF37;
        transition: transform .2s;
    }
    .game-card:hover {
        transform: scale(1.02);
    }
    .gold-title {
        color: #D4AF37;
        text-align: center;
        font-family: 'Serif';
        font-weight: bold;
        font-size: 42px;
        margin-bottom: 0px;
    }
    .balance-box {
        background-color: #D4AF37;
        color: black;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        font-weight: bold;
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

# --- NAVEGACIÓN ---
st.sidebar.markdown("<h2 style='color: #D4AF37;'>♣️ FORTUNA MX</h2>", unsafe_allow_html=True)
pagina = st.sidebar.radio("Navegación", ["🎰 Lobby de Juegos", "💰 Cajero / Depósitos", "📊 Admin Panel"])

# --- LÓGICA DEL LOBBY ---
if pagina == "🎰 Lobby de Juegos":
    # Header centrado
    col_a, col_b, col_c = st.columns([1, 2, 1])
    with col_b:
        st.image("https://r.jina.ai/i/9e0e5a8f6d3c4b2a8e1d2f3a4b5c6d7e", use_container_width=True)
        st.markdown("<h1 class='gold-title'>FORTUNA MX</h1>", unsafe_allow_html=True)
    
    st.divider()

    # Saldo en una posición fija
    c_inf, c_sal = st.columns([4, 1])
    with c_sal:
        st.markdown(f"<div class='balance-box'>SALDO: ${st.session_state.saldo:,.2f} MXN</div>", unsafe_allow_html=True)

    st.markdown("### 🔥 Juegos más populares")
    
    # Definición de juegos con imágenes reales
    juegos = [
        {"nombre": "Sweet Bonanza", "img": "https://images.ctfassets.net/69mcl89p8l6v/7d2fEof2C0y6yOQUy6e2Yy/719f9f592d3e4f0d8a5a5a5a5a5a5a5a/sweet-bonanza.jpg", "prov": "Pragmatic"},
        {"nombre": "Gates of Olympus", "img": "https://images.ctfassets.net/69mcl89p8l6v/5P6p7o8n9m0l1k2j3i4h5g/9a8b7c6d5e4f3g2h1i0j9k8l7m6n5o4p/gates-of-olympus.jpg", "prov": "Pragmatic"},
        {"nombre": "Lightning Roulette", "img": "https://www.evolution.com/sites/default/files/styles/game_thumbnail/public/game-thumbnails/lightning-roulette.jpg", "prov": "Evolution"},
        {"nombre": "Blackjack Live", "img": "https://www.evolution.com/sites/default/files/styles/game_thumbnail/public/game-thumbnails/blackjack.jpg", "prov": "Evolution"}
    ]

    # Grid de juegos en columnas
    cols = st.columns(2)
    for idx, juego in enumerate(juegos):
        with cols[idx % 2]:
            with st.container():
                # Simulación de tarjeta visual
                st.image(juego["img"], use_container_width=True, caption=f"By {juego['prov']}")
                st.write(f"**{juego['nombre']}**")
                if st.button(f"JUGAR AHORA", key=f"play_{idx}", use_container_width=True):
                    if st.session_state.saldo >= 50:
                        st.session_state.saldo -= 50
                        st.session_state.ggr += 5.0
                        st.session_state.logs.insert(0, {"Hora": time.strftime("%H:%M:%S"), "Evento": f"Jugó {juego['nombre']}", "Monto": "-$50.00"})
                        st.balloons()
                        st.toast(f"Abriendo {juego['nombre']}...")
                        time.sleep(1)
                        st.rerun()
                    else:
                        st.error("❌ Saldo insuficiente")

# --- CAJERO (Nuevo) ---
elif pagina == "💰 Cajero / Depósitos":
    st.markdown("<h2 class='gold-title'>CAJERO</h2>", unsafe_allow_html=True)
    st.write("Recarga tu cuenta para seguir jugando.")
    
    monto_recarga = st.number_input("Monto a depositar (MXN)", min_value=100, step=100)
    metodo = st.selectbox("Método de Pago", ["SPEI (Transferencia)", "OXXO Pay", "Tarjeta Bancaria"])
    
    if st.button("PROCESAR DEPÓSITO", use_container_width=True):
        with st.spinner("Conectando con pasarela de pago..."):
            time.sleep(2)
            st.session_state.saldo += monto_recarga
            st.success(f"¡Depósito de ${monto_recarga} MXN exitoso!")
            st.rerun()

# --- ADMIN PANEL ---
else:
    st.title("📊 Control Administrativo")
    st.metric("GGR Acumulado (Revenue)", f"${st.session_state.ggr:,.2f} MXN")
    st.write("### Historial de Movimientos")
    st.dataframe(pd.DataFrame(st.session_state.logs), use_container_width=True)
