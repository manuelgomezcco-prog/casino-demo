import streamlit as st
import pandas as pd
import time

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="Fortuna MX - Casino Online",
    page_icon="🎰",
    layout="wide"
)

# Estilo personalizado para el título dorado
st.markdown("""
    <style>
    .gold-text {
        color: #D4AF37;
        text-align: center;
        font-family: 'Serif';
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. INICIALIZACIÓN DE DATOS (Simulando base de datos)
if 'saldo' not in st.session_state:
    st.session_state.saldo = 5000.0
if 'ggr' not in st.session_state:
    st.session_state.ggr = 0.0
if 'logs' not in st.session_state:
    st.session_state.logs = []

# --- NAVEGACIÓN LATERAL ---
st.sidebar.title("♣️ FORTUNA MX")
pagina = st.sidebar.radio("Menú Principal", ["Lobby del Jugador", "Panel de Control (Admin)"])

# --- LÓGICA DEL LOBBY DEL JUGADOR ---
if pagina == "Lobby del Jugador":
    # Encabezado con Logo y Título
    col_a, col_b, col_c = st.columns([1, 2, 1])
    with col_b:
        # Aquí usamos la URL de la imagen del trébol dorado
        st.image("https://r.jina.ai/i/9e0e5a8f6d3c4b2a8e1d2f3a4b5c6d7e", use_container_width=True)
        st.markdown("<h1 class='gold-text'>FORTUNA MX</h1>", unsafe_allow_html=True)
    
    st.divider()

    # Fila de Saldo
    c_inv, c_saldo = st.columns([3, 1])
    with c_saldo:
        st.metric("Tu Billetera", f"${st.session_state.saldo:,.2f} MXN")

    st.subheader("🎰 Juegos Populares")
    
    # Grid de juegos con diseño mejorado
    juegos = [
        {"nombre": "Sweet Bonanza", "prov": "Pragmatic"},
        {"nombre": "Lightning Roulette", "prov": "Evolution"},
        {"nombre": "Blackjack VIP", "prov": "Evolution"},
        {"nombre": "Gates of Olympus", "prov": "Pragmatic"}
    ]
    
    cols = st.columns(2)
    for idx, juego in enumerate(juegos):
        with cols[idx % 2]:
            with st.container(border=True):
                st.write(f"### {juego['nombre']}")
                st.caption(f"Proveedor: {juego['prov']}")
                if st.button(f"Jugar $50.00", key=f"juego_{idx}", use_container_width=True):
                    if st.session_state.saldo >= 50:
                        st.session_state.saldo -= 50
                        # Simulación: El casino retiene un margen (GGR)
                        st.session_state.ggr += 5.0 
                        st.session_state.logs.insert(0, {
                            "Hora": time.strftime("%H:%M:%S"), 
                            "Evento": f"Apuesta: {juego['nombre']}", 
                            "Monto": "-$50.00"
                        })
                        st.toast(f"¡Girando en {juego['nombre']}!")
                        time.sleep(0.5)
                        st.rerun()
                    else:
                        st.error("Saldo insuficiente. Por favor recarga.")

# --- LÓGICA DEL PANEL DE ADMINISTRACIÓN ---
else:
    st.title("📊 Administración de Fortuna MX")
    
    # Métricas de Negocio
    m1, m2, m3 = st.columns(3)
    m1.metric("GGR (Utilidad Casa)", f"${st.session_state.ggr:,.2f} MXN", delta="Ganancia real")
    m2.metric("Jugadores en línea", "1", delta="Activo ahora")
    m3.metric("Estado de Red", "Excelente", delta="Ping: 45ms")
    
    st.divider()
    
    col_config, col_trans = st.columns([1, 1])
    
    with col_config:
        st.subheader("🔧 Conexión con Agregadores")
        agregador = st.selectbox("Seleccionar HUB", ["Slotegrator", "SoftGamings", "EveryMatrix"])
        st.text_input("Llave Privada (Production Key)", type="password", value="FORTUNA_MX_SECURE_KEY")
        if st.button("Verificar Sincronización"):
            st.success(f"Sincronizado con {agregador}. 1,200+ juegos listos.")
            
    with col_trans:
        st.subheader("📝 Auditoría de Apuestas")
        if st.session_state.logs:
            st.dataframe(pd.DataFrame(st.session_state.logs), use_container_width=True)
        else:
            st.info("Sin transacciones en esta sesión.")

# --- FOOTER ---
st.sidebar.divider()
st.sidebar.caption("© 2026 Fortuna MX | Proyecto Confidencial")
