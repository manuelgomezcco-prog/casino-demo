import streamlit as st

# ---------------- CONFIG ----------------
st.set_page_config(layout="wide")

# ---------------- ESTADO ----------------
if "menu" not in st.session_state:
    st.session_state.menu = False

if "page" not in st.session_state:
    st.session_state.page = "inicio"

# ---------------- CSS ----------------
st.markdown("""
<style>
header {display:none;}
[data-testid="stHeader"] {display:none;}
.block-container {padding-top: 0rem;}

.menu-box {
    position: fixed;
    top: 70px;
    right: 10px;
    background: #1a232e;
    padding: 10px;
    border-radius: 10px;
    z-index: 9999;
    width: 180px;
}

.menu-box div {
    padding: 8px;
    cursor: pointer;
}

.menu-box div:hover {
    background: #2c3a4d;
    border-radius: 6px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
col1, col2, col3 = st.columns([2,5,3])

with col1:
    st.image("Logo.jpg", width=90)

with col3:
    c1, c2, c3 = st.columns([2,2,1])

    with c1:
        if st.button("💳 Deposita"):
            st.session_state.page = "depositos"

    with c2:
        st.markdown(
            '<div style="background:#2c3a4d;padding:8px;border-radius:6px;text-align:center;">$0.32</div>',
            unsafe_allow_html=True
        )

    with c3:
        if st.button("👤"):
            st.session_state.menu = not st.session_state.menu

# ---------------- MENÚ ----------------
if st.session_state.menu:
    st.markdown("""
    <div class="menu-box">
        <div onclick="window.location.reload()">💸 Retiros</div>
        <div onclick="window.location.reload()">📥 Depósitos</div>
        <div onclick="window.location.reload()">💬 Mensajes</div>
        <div onclick="window.location.reload()">🚪 Cerrar sesión</div>
    </div>
    """, unsafe_allow_html=True)

# ---------------- PANTALLAS ----------------

# 🏠 INICIO
if st.session_state.page == "inicio":

    st.image(
        "https://images.unsplash.com/photo-1601597111158-2fceff292cdc?w=1200",
        use_container_width=True
    )

    st.markdown("## 🎰 Sigue Jugando")

    cols = st.columns(4)

    for i, col in enumerate(cols):
        with col:
            st.image(f"https://picsum.photos/20{i}")
            if st.button("JUGAR", key=f"play{i}"):
                st.session_state.page = "juego"

# 💳 DEPÓSITOS
elif st.session_state.page == "depositos":

    st.markdown("## 💳 Depósitos")

    monto = st.number_input("Monto", min_value=1)

    metodo = st.selectbox("Método", ["Tarjeta", "Transferencia", "Crypto"])

    if st.button("Confirmar depósito"):
        st.success(f"Depósito de ${monto} realizado")

    if st.button("⬅ Volver"):
        st.session_state.page = "inicio"

# 💸 RETIROS
elif st.session_state.page == "retiros":

    st.markdown("## 💸 Retiros")

    monto = st.number_input("Monto a retirar", min_value=1)

    if st.button("Solicitar retiro"):
        st.success(f"Retiro de ${monto} solicitado")

    if st.button("⬅ Volver"):
        st.session_state.page = "inicio"

# 🎮 JUEGO
elif st.session_state.page == "juego":

    st.markdown("## 🎮 Juego en curso")

    st.image("https://picsum.photos/600")

    if st.button("⬅ Volver"):
        st.session_state.page = "inicio"

# ---------------- FOOTER ----------------
st.markdown("""
<div style="
position:fixed;
bottom:0;
width:100%;
background:#1a232e;
display:flex;
justify-content:space-around;
padding:10px;
">
<div>🏠 Inicio</div>
<div>💳 Deposita</div>
<div>🎰 Slots</div>
<div>☰ Menú</div>
</div>
""", unsafe_allow_html=True)
