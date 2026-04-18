import streamlit as st

# ---------------- CONFIG ----------------
st.set_page_config(layout="wide")

# ---------------- ESTADO ----------------
if "menu" not in st.session_state:
    st.session_state.menu = False

if "page" not in st.session_state:
    st.session_state.page = "inicio"

if "saldo" not in st.session_state:
    st.session_state.saldo = 100  # saldo inicial ficticio

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

.deposit-btn button {
    background-color: #28a745 !important;
    color: white !important;
    font-weight: bold;
    border-radius: 6px;
}

.balance-box {
    background:#2c3a4d;
    padding:6px;
    border-radius:6px;
    text-align:center;
    font-size:11px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
col1, col2 = st.columns([6,4])

# LOGO (más grande)
with col1:
    st.image("Logo.jpg", width=150)

# DERECHA (saldo + botones)
with col2:
    c1, c2, c3 = st.columns([2,2,1])

    # BOTÓN DEPOSITAR
    with c1:
        st.markdown('<div class="deposit-btn">', unsafe_allow_html=True)
        if st.button("💳 Depositar"):
            st.session_state.page = "depositos"
        st.markdown('</div>', unsafe_allow_html=True)

    # SALDO
    with c2:
        st.markdown(f"""
        <div class="balance-box">
        ${st.session_state.saldo}
        </div>
        """, unsafe_allow_html=True)

    # BOTÓN USUARIO
    with c3:
        if st.button("👤"):
            st.session_state.menu = not st.session_state.menu

# ---------------- MENÚ ----------------
if st.session_state.menu:
    st.markdown("""
    <div class="menu-box">
        <div>💸 Retiros</div>
        <div>📥 Depósitos</div>
        <div>💬 Mensajes</div>
        <div>🚪 Cerrar sesión</div>
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

            costo = 10

            if st.button(f"JUGAR ${costo}", key=f"play{i}"):

                if st.session_state.saldo >= costo:
                    st.session_state.saldo -= costo
                    st.success(f"Jugaste y gastaste ${costo}")
                else:
                    st.error("Saldo insuficiente")

# 💳 DEPÓSITOS
elif st.session_state.page == "depositos":

    st.markdown("## 💳 Depósitos")

    monto = st.number_input("Monto a agregar", min_value=1)

    if st.button("Agregar fondos"):
        st.session_state.saldo += monto
        st.success(f"Se agregaron ${monto}")

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
font-size:12px;
">
<div>🏠 Inicio</div>
<div>💳 Deposita</div>
<div>🎰 Slots</div>
<div>☰ Menú</div>
</div>
""", unsafe_allow_html=True)
