import streamlit as st
import pandas as pd
import time

# Configuración inicial
st.set_page_config(page_title="Casino Pro", layout="wide")

# Inicialización de datos (Simulando una base de datos)
if 'saldo' not in st.session_state:
    st.session_state.saldo = 5000.0
if 'ggr' not in st.session_state:
    st.session_state.ggr = 0.0
if 'logs' not in st.session_state:
    st.session_state.logs = []

# --- NAVEGACIÓN ---
st.sidebar.title("Navegación")
pagina = st.sidebar.radio("Ir a:", ["Lobby del Jugador", "Panel de Control (Admin)"])

# --- LÓGICA DEL LOBBY DEL JUGADOR ---
if pagina == "Lobby del Jugador":
    col_l, col_r = st.columns([3, 1])
    with col_l:
        st.title("🎰 Bienvenido al Casino")
    with col_r:
        st.metric("Tu Saldo", f"${st.session_state.saldo:,.2f} MXN")

    st.subheader("Juegos Destacados")
    
    # Grid de juegos
    juegos = [
        {"nombre": "Sweet Bonanza", "color": "#FF5733"},
        {"nombre": "Lightning Roulette", "color": "#FFD700"},
        {"nombre": "Blackjack Live", "color": "#006400"},
        {"nombre": "Gates of Olympus", "color": "#4B0082"}
    ]
    
    cols = st.columns(2)
    for idx, juego in enumerate(juegos):
        with cols[idx % 2]:
            st.info(f"### {juego['nombre']}")
            if st.button(f"Apostar $50 en {juego['nombre']}", key=f"btn_{idx}"):
                if st.session_state.saldo >= 50:
                    st.session_state.saldo -= 50
                    # Simulamos que la casa gana el 10% (GGR)
                    st.session_state.ggr += 50 * 0.10
                    st.session_state.logs.insert(0, {"Hora": time.strftime("%H:%M:%S"), "Evento": f"Apuesta en {juego['nombre']}", "Monto": "-$50"})
                    st.success("¡Suerte! Procesando apuesta...")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("Saldo insuficiente")

# --- LÓGICA DEL PANEL DE ADMINISTRACIÓN ---
else:
    st.title("📊 Panel de Control Administrativo")
    
    c1, c2, c3 = st.columns(3)
    c1.metric("GGR (Ganancia Casa)", f"${st.session_state.ggr:,.2f} MXN")
    c2.metric("Usuarios Activos", "1")
    c3.metric("Status API", "🟢 Conectado")
    
    st.subheader("Configuración de Proveedores")
    prov = st.selectbox("Proveedor", ["Pragmatic Play", "Evolution Gaming"])
    st.text_input("API Key", type="password", value="demo_key_12345")
    
    if st.button("Probar Conexión"):
        st.toast("Sincronizando con el servidor del proveedor...")
        
    st.subheader("Historial de Transacciones en Vivo")
    if st.session_state.logs:
        st.table(pd.DataFrame(st.session_state.logs))
    else:
        st.write("No hay transacciones recientes.")
