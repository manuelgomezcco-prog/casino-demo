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

# 2. ESTILOS CSS (DISEÑO DE ALTA PRECISIÓN Y FORZADO DE COLUMNAS)
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    
    /* TÍTULO PRINCIPAL */
    .gold-title {
        color: #D4AF37;
        text-align: center;
        font-family: 'Helvetica', sans-serif;
        font-weight: bold;
        font-size: 35px;
        margin-top: 20px;
        letter-spacing: 2px;
    }

    /* CONTENEDOR DE USUARIO (ESQUINA SUPERIOR DERECHA) */
    .user-section {
        display: flex;
        flex-direction: column;
        align-items: flex-end;
        gap: 8px;
    }
    
    .user-bar-mini {
        background-color: #1f2630;
        padding: 6px 15px;
        border-radius: 20px;
        display: flex;
        align-items: center;
        border: 1px solid #D4AF37;
    }
    
    .user-balance-mini {
        color: #D4AF37;
        font-weight: bold;
        font-size: 15px;
        margin-right: 10px;
    }

    /* BOTÓN DE PERFIL ESTILIZADO */
    div.stButton > button {
        background-color: transparent;
        color: #D4AF37;
        border: 1px solid #D4AF37;
        border-radius: 8px;
        font-size: 12px;
        padding: 2px 10px;
        height: auto;
        width: fit-content;
    }
    div.stButton > button:hover {
        background-color: #D4AF37;
        color: black;
    }

    /* FORZAR TAMAÑO DE LOGO Y EVITAR QUE SE ENCOJA */
    [data-testid="stImage"] img {
        max-width: none !important;
        width: 180px !important; 
    }

    /* --- SOLUCIÓN PARA MÓVIL: FORZAR 3 COLUMNAS --- */
    [data-testid="column"] {
        flex: 1 1 30% !important; /* Obliga a que cada columna ocupe un tercio */
        min-width: 30% !important;
    }
    
    div[data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important; /* Evita que se pongan una abajo de otra */
        flex-wrap: wrap !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. ESTADO DE SESIÓN
if 'saldo' not in st.session_state: st.session_state.saldo = 5000.0
if 'ggr' not in st.session_state: st.session_state.ggr = 0.0
if 'logs' not in st.session_state: st.session_state.logs = []
if 'mensajes' not in st.session_state: 
    st.session_state.mensajes = ["¡Bienvenido!", "Nuevo juego de Poker añadido."]

# --- DIÁLOGO DE PERFIL ---
@st.dialog("Perfil de Usuario")
def mostrar_perfil():
    st.write("### 👤 Usuario Registrado")
    tabs = st.tabs(["💬 Mensajes", "📜 Actividad", "⚙️ Sistema"])
    with tabs[0]:
        for m in st.session_state.mensajes: st.info(m)
    with tabs[1]:
        if st.session_state.logs: st.table(pd.DataFrame(st.session_state.logs))
        else: st.write("Sin actividad reciente.")
    with tabs[2]:
        if st.button("Cerrar Sesión", type="primary"):
            st.session_state.clear()
            st.rerun()

# --- BARRA SUPERIOR ---
col_izq, col_der = st.columns([2, 1])

with col_izq:
    if os.path.exists("logo.PNG"):
        st.image("logo.PNG")

with col_der:
    st.markdown('<div class="user-section">', unsafe_allow_html=True)
    if st.button("Mi Perfil", key="btn_perfil_top"):
        mostrar_perfil()
    
    st.markdown(f"""
        <div class="user-bar-mini">
            <span class="user-balance-mini">${st.session_state.saldo:,.2f}</span>
            <span style="font-size: 18px;">👤</span>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<h1 class='gold-title'>FORTUNA MX</h1>", unsafe_allow_html=True)
st.divider()

# --- LOBBY (FORZADO A 3 POR FILA) ---
menu = st.sidebar.radio("Navegación", ["🎰 Lobby", "💰 Cajero", "📊 Admin"])

if menu == "🎰 Lobby":
    st.subheader("🔥 Destacados")
    juegos = [
        {"n": "Fruity Fortune", "img": "https://images.unsplash.com/photo-1596711762462-850f28584813?w=500"},
        {"n": "Ancient Zeus", "img": "https://images.unsplash.com/photo-1503197979108-c824168d51a8?w=500"},
        {"n": "Royal Roulette", "img": "https://images.unsplash.com/photo-1606167668584-78701c57f13d?w=500"},
        {"n": "Blackjack Gold", "img": "https://images.unsplash.com/photo-1511193311914-0346f16efe90?w=500"},
        {"n": "Golden Slots", "img": "https://images.unsplash.com/photo-1596711762462-850f28584813?w=500"},
        {"n": "Poker Night", "img": "https://images.unsplash.com/photo-1511193311914-0346f16efe90?w=600"}
    ]

    # Generamos los juegos en bloques de 3
    for i in range(0, len(juegos), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(juegos):
                item = juegos[i + j]
                with cols[j]:
                    with st.container(border=True):
                        st.image(item["img"], use_container_width=True)
                        st.markdown(f"<p style='text-align:center; font-size:10px; font-weight:bold;'>{item['n']}</p>", unsafe_allow_html=True)
                        if st.button("JUGAR", key=f"play_{i+j}"):
                            if st.session_state.saldo >= 50:
                                st.session_state.saldo -= 50
                                st.session_state.ggr += 15.0
                                st.session_state.logs.insert(0, {"Hora": time.strftime("%H:%M"), "Juego": item['n'], "Acción": "-$50.00"})
                                st.rerun()

elif menu == "💰 Cajero":
    monto = st.select_slider("Monto:", [500, 1000, 2000, 5000])
    if st.button("Depositar"):
        st.session_state.saldo += monto
        st.balloons()
        st.rerun()
else:
    st.metric("GGR Casa", f"${st.session_state.ggr:,.2f}")
