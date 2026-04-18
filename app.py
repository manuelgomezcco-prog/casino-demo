import streamlit as st
from PIL import Image
import random

st.set_page_config(layout="wide")

# ---------------- ESTADO ----------------
if "saldo" not in st.session_state:
    st.session_state.saldo = 1000

if "menu" not in st.session_state:
    st.session_state.menu = False

# ---------------- ESTILOS ----------------
st.markdown("""
<style>

/* Quitar espacio arriba */
.block-container {
    padding-top: 0.5rem;
}

/* HEADER */
.header {
    display:flex;
    justify-content:space-between;
    align-items:center;
    margin-bottom:20px;
}

/* LOGO */
.logo img {
    height:70px;
}

/* RIGHT SIDE */
.right {
    display:flex;
    align-items:center;
    gap:10px;
}

/* BOTÓN */
.deposit {
    background:#4cd137;
    color:white;
    padding:8px 14px;
    border-radius:8px;
    font-size:14px;
    font-weight:bold;
}

/* SALDO */
.balance {
    background:#2c3a4d;
    padding:6px 12px;
    border-radius:6px;
    font-size:13px;
}

/* USER */
.user {
    background:#2c3a4d;
    padding:6px 10px;
    border-radius:6px;
}

/* MENÚ */
.menu {
    position:absolute;
    right:20px;
    top:70px;
    background:#1e2a38;
    padding:15px;
    border-radius:10px;
    width:150px;
}

/* CARDS */
.card {
    background:#13263a;
    padding:20px;
    border-radius:12px;
    text-align:center;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
logo = Image.open("Logo.jpg")

col1, col2 = st.columns([3,2])

with col1:
    st.image(logo, width=160)

with col2:
    c1, c2, c3 = st.columns([1.2,1,0.6])

    with c1:
        if st.button("💳 Depositar"):
            st.session_state.saldo += 500

    with c2:
        st.markdown(
            f"<div class='balance'>${st.session_state.saldo}</div>",
            unsafe_allow_html=True
        )

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

# ---------------- LÓGICA CASINO ----------------
def jugar(costo):
    if st.session_state.saldo >= costo:
        if random.random() < 0.4:  # 40% ganar
            ganancia = costo * 2
            st.session_state.saldo += ganancia
            st.success(f"Ganaste ${ganancia}")
        else:
            st.session_state.saldo -= costo
            st.error(f"Perdiste ${costo}")
    else:
        st.warning("Saldo insuficiente")

# ---------------- JUEGOS ----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='card'>🍒 Slot Básico</div>", unsafe_allow_html=True)
    if st.button("Jugar $50"):
        jugar(50)

with col2:
    st.markdown("<div class='card'>👑 Slot Premium</div>", unsafe_allow_html=True)
    if st.button("Jugar $100"):
        jugar(100)

with col3:
    st.markdown("<div class='card'>💎 Mega Slot</div>", unsafe_allow_html=True)
    if st.button("Jugar $200"):
        jugar(200)
