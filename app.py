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

# 2. ESTILOS CSS PERSONALIZADOS
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
        font-size: 32px;
        margin-top: -10px;
        letter-spacing: 2px;
    }
    /* Estilo para la barra superior de usuario */
    .user-bar {
        background-color: #1f2630;
        padding: 10px 20px;
        border-radius: 50px;
        display: flex;
        align-items: center;
        justify-content: center;
        border: 1px solid #D4AF37;
        margin-bottom: 10px;
    }
    .user-balance {
        color: #D4AF37;
        font-weight: bold;
        font-size: 18px;
        margin-right: 15px;
    }
    .user-icon {
        font-size: 24px;
        color: white;
    }
    /* Botones de apuesta */
    div.stButton > button {
        background-color: #D4AF37;
        color: black;
        font-weight: bold;
        border-radius: 8px;
        border: none;
        padding: 8px;
        width: 100%;
        font-size: 12px;
    }
    div.stButton > button:hover {
        background-color: #ffffff;
        color: black;
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
menu = st.sidebar.radio("Navegación:", ["🎰 Lobby", "💰 Cajero", "📊 Admin"])

# --- ENCABEZADO SUPERIOR (Logo, Título y Perfil/Saldo) ---
# Creamos 3 columnas: [Logo][Título][Saldo/Perfil]
head_left, head_mid, head_right = st.columns([1, 2, 1])

with head_left:
    if os.path.exists("logo.PNG"):
        st.image("logo.PNG", width=80)

with head_mid:
    st.markdown("<h1 class='gold-title'>FORTUNA MX</h1>", unsafe_allow_html=True)

with head_right:
    # Contenedor para el saldo y el icono de persona
    st.markdown(f"""
        <div class="user-bar">
            <span class="user-balance">${st.session_state.saldo:,.2f}</span>
            <span class="user-icon">👤</span>
        </div>
    """, unsafe_allow_html=True)

st.divider()

# --- LOBBY DE JUEGOS ---
if menu == "🎰 Lobby":
    st.subheader("🔥 Juegos Destacados")
    
    juegos = [
        {"n": "Fruity Fortune", "img": "https://images.unsplash.com/photo-1596711762462-850f28584813?w=600"},
        {"n": "Ancient Zeus", "img": "https://images.unsplash.com/photo-1503197979108-c824168d51a8?w=600"},
        {"n": "Royal Roulette", "img": "https://images.unsplash.com/photo-1606167668584-78701c57f13d?w=600"},
        {"n": "Blackjack Gold", "img": "https://images.unsplash.com/photo-1511193311914-0346f16efe90?w=600"},
        {"n": "Golden Slots", "img": "https://images.unsplash.com/photo-1596711762462-850f28584813?w=600"},
        {"n": "Poker Night", "img": "https://images.unsplash.com/photo-1511193311914-0346f16efe90?w=600"}
    ]

    # Distribución de 3 juegos por fila
    for i in range(0, len(juegos), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(juegos):
                juego = juegos[i + j]
                with cols[j]:
                    with st.container(border=True):
                        st.image(juego["img"], use_container_width=True)
                        st.markdown(f"<p style='text-align:center; font-weight:bold; color:white; font-size:14px; margin-bottom:5px;'>{juego['n']}</p>", unsafe_allow_html=True)
                        if st.button(f"APOSTAR", key=f"btn_{i+j}"):
                            if st.session_state.saldo >= 50:
                                st.session_state.saldo -= 50
                                st.session_state.ggr += 12.50
                                st.session_state.logs.insert(0, {"Hora": time.strftime("%H:%M:%S"), "Juego": juego['n'], "Acción": "-$50.00"})
                                st.toast(f"¡Suerte en {juego['n']}!")
                                time.sleep(0.3)
                                st.rerun()
                            else:
                                st.error("Sin saldo")

elif menu == "💰 Cajero":
    st.markdown("<h2 class='gold-title'>CAJERO</h2>", unsafe_allow_html=True)
    monto = st.select_slider("Monto a depositar:", options=[200, 500, 1000, 2000, 5000])
    if st.button("RECARGAR AHORA"):
        st.session_state.saldo += monto
        st.balloons()
        st.rerun()

else:
    st.title("📊 Panel Admin")
    st.metric("GGR (Ganancia Casa)", f"${st.session_state.ggr:,.2f}")
