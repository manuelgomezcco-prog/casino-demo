import streamlit as st
from PIL import Image
import random

st.set_page_config(layout="wide")

# ---------------- ESTADO ----------------
if "saldo" not in st.session_state:
    st.session_state.saldo = 1000.00

if "menu" not in st.session_state:
    st.session_state.menu = False

# ---------------- ESTILOS ----------------
st.markdown("""
<style>
/* Fondo general oscuro */
.block-container {
    padding-top: 1rem;
    background-color: #0f172a;
    color: #f8fafc;
}

/* HEADER */
.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 0px;
    margin-bottom: 20px;
}

/* RIGHT SIDE HEADER */
.right-header {
    display: flex;
    align-items: center;
    gap: 12px;
}

/* BOTÓN DEPOSITAR - Estilo original */
.stButton>button {
    border-radius: 8px;
    font-weight: bold;
}

/* Caja de Saldo */
.balance-box {
    background-color: #1e293b;
    color: #f8fafc;
    padding: 6px 15px;
    border-radius: 8px;
    font-size: 14px;
    border: 1px solid #334155;
    height: 38px;
    display: flex;
    align-items: center;
    font-weight: 600;
}

/* Icono de Persona */
.user-circle {
    background-color: #334155;
    color: white;
    width: 38px;
    height: 38px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
}

/* Tarjetas de Juegos */
.game-card {
    background: #1e293b;
    padding: 15px;
    border-radius: 15px;
    text-align: center;
    border: 1px solid #334155;
    transition: 0.3s;
}

.game-title {
    font-weight: bold;
    font-size: 16px;
    margin-bottom: 5px;
    color: #f1f5f9;
}

.developer-tag {
    color: #94a3b8;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Footer Nav */
.footer-nav {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: #0f172a;
    display: flex;
    justify-content: space-around;
    padding: 12px;
    border-top: 1px solid #334155;
    z-index: 1000;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
col_logo, col_actions = st.columns([1, 1])

with col_logo:
    try:
        # Restauramos tu logotipo original conservando su tamaño
        logo = Image.open("Logo.jpg")
        st.image(logo, width=180)
    except:
        st.markdown("<h2 style='color: #d4af37; margin:0;'>FORTUNA MX</h2>", unsafe_allow_html=True)

with col_actions:
    # Alineamos saldo y persona a la derecha
    c1, c2, c3 = st.columns([1, 0.8, 0.3])
    
    with c1:
        if st.button("💳 Depositar", use_container_width=True):
            st.session_state.saldo += 500
            st.rerun()
            
    with c2:
        st.markdown(f"<div class='balance-box'>${st.session_state.saldo:,.2f}</div>", unsafe_allow_html=True)
        
    with c3:
        if st.button("👤"):
            st.session_state.menu = not st.session_state.menu
            st.rerun()

# ---------------- BANNER ----------------
st.image("https://images.unsplash.com/photo-1601597111158-2fceff292cdc", use_column_width=True)

# ---------------- SECCIONES DE JUEGOS ----------------
st.markdown("### 🎰 SIGUE JUGANDO")

def render_game(titulo, developer, key):
    st.markdown(f"""
    <div class='game-card'>
        <div class='game-title'>{titulo}</div>
        <div class='developer-tag'>{developer}</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button(f"Jugar", key=key, use_container_width=True):
        st.toast(f"Cargando {titulo}...")

cols = st.columns(4)
juegos = [
    ("30 Spicy Fruits", "FORTUNA GAMES"),
    ("40 Shining Crown", "EGT"),
    ("Leprechaun Hot", "PRAGMATIC"),
    ("Mega Slot 777", "FORTUNA GAMES")
]

for i, (titulo, dev) in enumerate(juegos):
    with cols[i]:
        render_game(titulo, dev, f"game_{i}")

st.markdown("### 🔥 POPULARES")
cols_pop = st.columns(4)
populares = [
    ("Hot Blast", "RUBYPLAY"),
    ("Mad Hit Gold", "RUBYPLAY"),
    ("Voltage Rapid", "EGT"),
    ("Aztec Gold", "FORTUNA GAMES")
]

for i, (titulo, dev) in enumerate(populares):
    with cols_pop[i]:
        render_game(titulo, dev, f"pop_{i}")

# Espacio para el footer
st.markdown("<br><br><br>", unsafe_allow_html=True)

# ---------------- BARRA INFERIOR ----------------
st.markdown("""
<div class='footer-nav'>
    <div style='text-align:center; color:#94a3b8;'>🏠<br><small>Inicio</small></div>
    <div style='text-align:center; color:#94a3b8;'>💰<br><small>Depósitos</small></div>
    <div style='text-align:center; color:#94a3b8;'>🎲<br><small>En Vivo</small></div>
    <div style='text-align:center; color:#94a3b8;'>☰<br><small>Menú</small></div>
</div>
""", unsafe_allow_html=True)
