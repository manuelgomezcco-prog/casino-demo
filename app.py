import streamlit as st

# -----------------------------
# CONFIG
# -----------------------------
st.set_page_config(page_title="Fortuna MX", layout="wide")

# -----------------------------
# ESTADO (SALDO)
# -----------------------------
if "saldo" not in st.session_state:
    st.session_state.saldo = 1000

# -----------------------------
# FUNCIONES
# -----------------------------
def depositar():
    st.session_state.saldo += 100

def jugar(costo):
    if st.session_state.saldo >= costo:
        st.session_state.saldo -= costo
        st.success(f"Jugaste (-${costo})")
    else:
        st.error("Saldo insuficiente")

# -----------------------------
# CSS
# -----------------------------
st.markdown("""
<style>
body {
    background-color: #0b1118;
}

/* HEADER */
.header {
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:10px 20px;
    background:#111827;
    border-radius:12px;
}

/* LOGO */
.logo {
    height:60px;
}

/* DERECHA */
.right {
    display:flex;
    align-items:center;
    gap:10px;
}

/* BOTÓN */
.deposit {
    background:#76b82a;
    color:white;
    padding:8px 14px;
    border-radius:8px;
    font-weight:bold;
    font-size:13px;
}

/* SALDO */
.balance {
    background:#2c3a4d;
    padding:6px 12px;
    border-radius:8px;
    font-size:12px;
    color:white;
}

/* USER */
.user {
    background:#2c3a4d;
    padding:6px 10px;
    border-radius:8px;
    font-size:16px;
}

/* TARJETAS */
.card {
    background:#16202b;
    padding:10px;
    border-radius:12px;
}

/* TITULOS */
.title {
    font-size:22px;
    font-weight:bold;
    margin-top:20px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
col1, col2 = st.columns([3,2])

with col1:
    st.image("https://raw.githubusercontent.com/ManuelG-Prog/casino-demo/principal/Logo.jpg", width=140)

with col2:
    c1, c2, c3 = st.columns([1,1,1])

    with c1:
        if st.button("💳 Depositar"):
            depositar()

    with c2:
        st.markdown(f"""
        <div class="balance">
            ${st.session_state.saldo}
        </div>
        """, unsafe_allow_html=True)

    with c3:
        with st.popover("👤"):
            st.write("💸 Retiros")
            st.write("📥 Depósitos")
            st.write("💬 Mensajes")
            st.write("🚪 Cerrar sesión")

# -----------------------------
# BANNER
# -----------------------------
st.image("https://images.unsplash.com/photo-1518546305927-5a555bb7020d?w=1200", use_container_width=True)

# -----------------------------
# CATEGORÍAS
# -----------------------------
st.write("")
c1, c2, c3, c4 = st.columns(4)

c1.button("🔍 Buscar")
c2.button("🏠 Hogar")
c3.button("🆕 Nuevo")
c4.button("🎰 Slots")

# -----------------------------
# JUEGOS
# -----------------------------
st.markdown('<div class="title">🎰 Sigue Jugando</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://images.unsplash.com/photo-1605810230434-7631ac76ec81?w=400")
    if st.button("JUGAR $10", key="g1"):
        jugar(10)

with col2:
    st.image("https://images.unsplash.com/photo-1596838132731-3301c3fd4317?w=400")
    if st.button("JUGAR $20", key="g2"):
        jugar(20)

with col3:
    st.image("https://images.unsplash.com/photo-1607082350899-7e105aa886ae?w=400")
    if st.button("JUGAR $50", key="g3"):
        jugar(50)
