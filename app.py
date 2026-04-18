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
    .stApp { background-color: #0e1117; }
    
    /* Título principal */
    .gold-title {
        color: #D4AF37;
        text-align: center;
        font-family: 'Helvetica', sans-serif;
        font-weight: bold;
        font-size: 35px;
        margin-top: 10px;
        letter-spacing: 2px;
    }

    /* BARRA DE USUARIO COMPACTA EN LA ESQUINA */
    .user-container {
        position: absolute;
        top: -50px;
        right: 0px;
        display: flex;
        flex-direction: column;
        align-items: flex-end;
        gap: 5px;
    }
    
    .user-bar-mini {
        background-color: #1f2630;
        padding: 5px 12px;
        border-radius: 20px;
        display: flex;
        align-items: center;
        border: 1px solid #D4AF37;
        width: fit-content;
    }
    
    .user-balance-mini {
        color: #D4AF37;
        font-weight: bold;
        font-size: 14px;
        margin-right: 8px;
    }

    /* Botón de perfil más pequeño */
    .stButton > button {
        border-radius: 8px;
        font-weight: bold;
    }
    
    /* Ajuste para que el botón de Perfil no use tanto espacio */
    .profile-btn-container {
        display: flex;
        justify-content: flex-end;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. ESTADO DE SESIÓN
if 'saldo' not in st.session_state: st.session_state.saldo = 5000.0
if 'ggr' not in st.session_state: st.session_state.ggr = 0.0
if 'logs' not in st.session_state: st.session_state.logs = []
if 'mensajes' not in st.session_state: 
    st.session_state.mensajes = ["¡Bienvenido, Manuel!", "Bono de lealtad disponible."]

# --- FUNCIÓN DE PERFIL ---
@st.dialog("Mi Cuenta - Fortuna MX")
def mostrar_perfil():
    st.write("### 👤 Manuel Gómez")
    tab1, tab2, tab3 = st.tabs(["💬 Mensajes", "📜 Movimientos", "⚙️ Salir"])
    with tab1:
        for m in st.session_state.mensajes: st.info(m)
    with tab2:
        if st.session_state.logs: st.dataframe(pd.DataFrame(st.session_state.logs), use_container_width=True)
        else: st.write("Sin movimientos.")
    with tab3:
        if st.button("Cerrar Sesión Ahora", type="primary"):
            st.session_state.clear()
            st.rerun()

# --- BARRA SUPERIOR ESTRUCTURADA ---
# Usamos columnas para separar el Logo de la Barra de Usuario
col_logo, col_espacio, col_user = st.columns([2, 1, 2])

with col_logo:
    # Conservamos el tamaño original del logo
    if os.path.exists("logo.PNG"):
        st.image("logo.PNG", use_container_width=False, width=150)

with col_user:
    # Saldo e icono compactos a la derecha
    st.markdown(f"""
        <div style="display: flex; flex-direction: column; align-items: flex-end;">
            <div class="user-bar-mini">
                <span class="user-balance-mini">${st.session_state.saldo:,.2f}</span>
                <span style="font-size: 18px;">👤</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    # Botón pequeño para entrar al perfil
    if st.button("Mi Perfil", key="perfil_top"):
        mostrar_perfil()

st.markdown("<h1 class='gold-title'>FORTUNA MX</h1>", unsafe_allow_html=True)
st.divider()

# --- LOBBY DE JUEGOS (3 POR FILA) ---
menu = st.sidebar.radio("Menú:", ["🎰 Lobby", "💰 Cajero", "📊 Admin"])

if menu == "🎰 Lobby":
    st.subheader("🔥 Juegos en Vivo")
    juegos = [
        {"n": "Fruity Fortune", "img": "https://images.unsplash.com/photo-1596711762462-850f28584813?w=500"},
        {"n": "Ancient Zeus", "img": "https://images.unsplash.com/photo-1503197979108-c824168d51a8?w=500"},
        {"n": "Royal Roulette", "img": "https://images.unsplash.com/photo-1606167668584-78701c57f13d?w=500"},
        {"n": "Blackjack Gold", "img": "https://images.unsplash.com/photo-1511193311914-0346f16efe90?w=500"},
        {"n": "Golden Slots", "img": "https://images.unsplash.com/photo-1596711762462-850f28584813?w=500"},
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
                                st.session_state.logs.insert(0, {"Hora": time.strftime("%H:%M"), "Evento": juego['n'], "Monto": "-$50.00"})
                                st.rerun()

elif menu == "💰 Cajero":
    monto = st.select_slider("Monto:", [500, 1000, 2000, 5000])
    if st.button("Depositar"):
        st.session_state.saldo += monto
        st.session_state.logs.insert(0, {"Hora": time.strftime("%H:%M"), "Evento": "Depósito", "Monto": f"+${monto}"})
        st.balloons()
        st.rerun()
else:
    st.metric("GGR Casa", f"${st.session_state.ggr:,.2f}")
