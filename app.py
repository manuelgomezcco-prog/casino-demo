import streamlit as st
from PIL import Image
import random

# ---------------- CONFIG ----------------
st.set_page_config(layout="wide")

# ---------------- ESTADO ----------------
if "saldo" not in st.session_state:
    st.session_state.saldo = 1000

if "menu" not in st.session_state:
    st.session_state.menu = False

# ---------------- ESTILOS ----------------
st.markdown("""
<style>
body {
    background-color: #0b1c2c;
}

.block-container {
    padding-top: 1rem;
}

/* HEADER */
.header {
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:10px 0;
}

.logo {
    height:60px;
}

.right-box {
    display:flex;
    gap:10px;
    align-items:center;
}

/* BOTÓN DEPOSITAR */
.deposit-btn {
    background:#4cd137;
    color:white;
    padding:8px 14px;
    border-radius:8px;
    font-weight:bold;
    font-size:14px;
}

/* SALDO */
.balance {
    background:#2c3a4d;
    padding:6px 12px;
    border-radius:6px;
    font-size:13px;
}

/* USER */
.user-btn {
    background:#2c3a4d;
    padding:6px 10px;
    border-radius:6px;
    cursor:pointer;
}

/* MENÚ */
.menu {
    position:absolute;
    right:20px;
    top:70px;
    background:#1e2a38;
    padding:15px;
    border-radius:10px;
}

/* TARJETAS */
.card {
    background:#13263a;
    padding:15px;
    border-radius:12px;
    text-align:center;
}

/* BOTÓN JUGAR */
.play-btn {
    background:#e84118;
    color:white;
    padding:6px 12px;
    border-radius:6px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
logo = Image.open("Logo.jpg")

col1, col2 = st.columns([2,3])

with col1:
    st.image(logo, width=140)

with col2:
    c1, c2, c3 = st.columns([1,1,1])

    with c1:
        if st.button("💳 Depositar"):
            st.session_state.saldo += 500

    with c2:
        st.markdown(f"<div class='balance'>${st.session_state.saldo}</div>", unsafe_allow_html=True)

    with c3:
        if st.button("👤"):
            st.session_state.menu = not st.session_state.menu

# ---------------- MENÚ ----------------
if st.session_state.menu:
    st.markdown("""
    <div class='menu'>
        💸 Retiros<br><br>
        💳 Depósitos<br><br>
        💬 Mensajes<br><br>
        🚪 Cerrar sesión
    </div>
    """, unsafe_allow_html=True)

# ---------------- BANNER ----------------
st.image("https://images.unsplash.com/photo-1601597111158-2fceff292cdc", use_column_width=True)

st.markdown("## 🎰 Sigue Jugando")

# ---------------- JUEGOS ----------------
col1, col2, col3 = st.columns(3)

def jugar(costo):
    if st.session_state.saldo >= costo:
        resultado = random.choice(["ganar", "perder"])
        if resultado == "ganar":
            ganancia = costo * 2
            st.session_state.saldo += ganancia
            st.success(f"Ganaste ${ganancia}")
        else:
            st.session_state.saldo -= costo
            st.error(f"Perdiste ${costo}")
    else:
        st.warning("Saldo insuficiente")

with col1:
    st.markdown("<div class='card'>🍒 Slot Básico</div>", unsafe_allow_html=True)
    if st.button("Jugar $50", key="j1"):
        jugar(50)

with col2:
    st.markdown("<div class='card'>👑 Slot Premium</div>", unsafe_allow_html=True)
    if st.button("Jugar $100", key="j2"):
        jugar(100)

with col3:
    st.markdown("<div class='card'>💎 Mega Slot</div>", unsafe_allow_html=True)
    if st.button("Jugar $200", key="j3"):
        jugar(200)
