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

# 2. ESTILOS CSS (DISEÑO PREMIUM)
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .gold-title {
        color: #D4AF37;
        text-align: center;
        font-family: 'Helvetica', sans-serif;
        font-weight: bold;
        font-size: 30px;
        margin-top: -10px;
    }
    .user-bar {
        background-color: #1f2630;
        padding: 8px 15px;
        border-radius: 50px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        border: 1px solid #D4AF37;
    }
    .user-balance { color: #D4AF37; font-weight: bold; font-size: 16px; }
    /* Botones de apuesta */
    div.stButton > button {
        background-color: #D4AF37;
        color: black;
        font-weight: bold;
        border-radius: 8px;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. ESTADO DE SESIÓN
if 'saldo' not in st.session_state: st.session_state.saldo = 5000.0
if 'ggr' not in st.session_state: st.session_state.ggr = 0.0
if 'logs' not in st.session_state: st.session_state.logs = []
if 'mensajes' not in st.session_state: 
    st.session_state.mensajes = ["¡Bienvenido a Fortuna MX!", "Tu bono de bienvenida ha sido activado."]

# --- FUNCIÓN PARA EL PERFIL ---
@st.dialog("Mi Perfil - Fortuna MX")
def mostrar_perfil():
    st.write(f"### 👤 Usuario: Manuel Gómez")
    st.write(f"**Saldo actual:** ${st.session_state.saldo:,.2f} MXN")
    
    tab1, tab2, tab3 = st.tabs(["💬 Mensajes", "📜 Movimientos", "⚙️ Cuenta"])
    
    with tab1:
        for msg in st.session_state.mensajes:
            st.info(msg)
            
    with tab2:
        if st.session_state.logs:
            df = pd.DataFrame(st.session_state.logs)
            st.dataframe(df, use_container_width=True)
        else:
            st.write("No hay movimientos recientes.")
            
    with tab3:
        if st.button("Cerrar Sesión", type="primary", use_container_width=True):
            st.session_state.clear()
            st.rerun()

# --- NAVEGACIÓN ---
menu = st.sidebar.radio("Menú:", ["🎰 Lobby", "💰 Cajero", "📊 Admin"])

# --- BARRA SUPERIOR ---
head_left, head_mid, head_right = st.columns([1, 2, 1.2])

with head_left:
    if os.path.exists("logo.PNG"):
        st.image("logo.PNG", width=70)

with head_mid:
    st.markdown("<h1 class='gold-title'>FORTUNA MX</h1>", unsafe_allow_html=True)

with head_right:
    # Creamos el contenedor visual y el botón que activa el diálogo
    st.markdown(f"""
        <div class="user-bar">
            <span class="user-balance">${st.session_state.saldo:,.2f}</span>
            <span style="color:white;">👤</span>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Ver Mi Perfil", use_container_width=True):
        mostrar_perfil()

st.divider()

# --- LOBBY DE JUEGOS (3 POR FILA) ---
if menu == "🎰 Lobby":
    st.subheader("🔥 Juegos en Vivo")
    
    juegos = [
        {"n": "Fruity Fortune", "img": "https://images.unsplash.com/photo-1596711762462-850f28584813?w=600"},
        {"n": "Ancient Zeus", "img": "https://images.unsplash.com/photo-1503197979108-c824168d51a8?w=600"},
        {"n": "Royal Roulette", "img": "https://images.unsplash.com/photo-1606167668584-78701c57f13d?w=600"},
        {"n": "Blackjack Gold", "img": "https://images.unsplash.com/photo-1511193311914-0346f16efe90?w=600"},
        {"n": "Golden Slots", "img": "https://images.unsplash.com/photo-1596711762462-850f28584813?w=600"},
        {"n": "Poker Night", "img": "https://images.unsplash.com/photo-1511193311914-0346f16efe90?w=600"}
    ]

    for i in range(0, len(juegos), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(juegos):
                juego = juegos[i + j]
                with cols[j]:
                    with st.container(border=True):
                        st.image(juego["img"], use_container_width=True)
                        st.markdown(f"<p style='text-align:center; font-size:12px; font-weight:bold;'>{juego['n']}</p>", unsafe_allow_html=True)
                        if st.button(f"APOSTAR", key=f"btn_{i+j}"):
                            if st.session_state.saldo >= 50:
                                st.session_state.saldo -= 50
                                st.session_state.ggr += 12.50
                                st.session_state.logs.insert(0, {"Hora": time.strftime("%H:%M"), "Juego": juego['n'], "Monto": "-50.00"})
                                st.toast(f"¡Suerte en {juego['n']}!")
                                time.sleep(0.3)
                                st.rerun()

elif menu == "💰 Cajero":
    st.markdown("<h2 class='gold-title'>DEPÓSITO</h2>", unsafe_allow_html=True)
    monto = st.select_slider("Selecciona monto:", options=[500, 1000, 2000, 5000])
    if st.button("Confirmar Recarga"):
        st.session_state.saldo += monto
        st.session_state.logs.insert(0, {"Hora": time.strftime("%H:%M"), "Juego": "Depósito", "Monto": f"+{monto}.00"})
        st.balloons()
        st.rerun()

else:
    st.title("📊 GGR House")
    st.metric("Total Ganado Casa", f"${st.session_state.ggr:,.2f}")
