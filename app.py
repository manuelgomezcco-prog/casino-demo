import streamlit as st

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Fortuna MX",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- ESTADO ----------------
if "menu_open" not in st.session_state:
    st.session_state.menu_open = False

if "page" not in st.session_state:
    st.session_state.page = "inicio"

def go(page):
    st.session_state.page = page
    st.session_state.menu_open = False

# ---------------- CSS ----------------
st.markdown("""
<style>
html, body, [class*="css"] {
    margin: 0 !important;
    padding: 0 !important;
}

.stApp {
    background-color: #0b1118;
}

header {display:none;}
[data-testid="stHeader"] {display:none;}

.block-container {
    padding-top: 0 !important;
}

/* HEADER */
.custom-header {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    height: 70px;
    background: #1a232e;
    z-index: 9999;
    border-bottom: 1px solid #2d343f;
}

/* LOGO */
.logo {
    position: absolute;
    left: 15px;
    top: 50%;
    transform: translateY(-50%);
}

/* DERECHA */
.right-box {
    position: absolute;
    right: 15px;
    top: 50%;
    transform: translateY(-50%);
    display: flex;
    gap: 8px;
    align-items: center;
}

/* BOTONES */
.btn {
    background: #76b82a;
    padding: 8px 14px;
    border-radius: 6px;
    font-weight: bold;
    color: black;
    font-size: 13px;
}

.saldo {
    background: #2d343f;
    padding: 8px 12px;
    border-radius: 6px;
    color: white;
    font-weight: bold;
}

/* MENU */
.menu-box {
    position: fixed;
    top: 70px;
    right: 15px;
    width: 200px;
    background: #1a232e;
    border: 1px solid #2d343f;
    border-radius: 10px;
    padding: 10px;
    z-index: 9999;
}

/* CONTENIDO */
.main {
    margin-top: 80px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<div class="custom-header">', unsafe_allow_html=True)

# Logo
st.markdown('<div class="logo">', unsafe_allow_html=True)
st.image("Logo.jpg", width=100)
st.markdown('</div>', unsafe_allow_html=True)

# Botones derecha
st.markdown('<div class="right-box">', unsafe_allow_html=True)

col1, col2, col3 = st.columns([2,2,1])

with col1:
    if st.button("📥 Depositar"):
        go("depositos")

with col2:
    st.markdown('<div class="saldo">$ 5,000.00</div>', unsafe_allow_html=True)

with col3:
    if st.button("👤"):
        st.session_state.menu_open = not st.session_state.menu_open

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---------------- MENU ----------------
if st.session_state.menu_open:
    st.markdown('<div class="menu-box">', unsafe_allow_html=True)

    if st.button("💸 Retiros"):
        go("retiros")

    if st.button("📥 Depósitos"):
        go("depositos")

    if st.button("💬 Mensajes"):
        go("mensajes")

    if st.button("🚪 Cerrar sesión"):
        go("logout")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- CONTENIDO ----------------
st.markdown('<div class="main">', unsafe_allow_html=True)

# -------- PANTALLAS --------

if st.session_state.page == "inicio":

    st.image(
        "https://images.unsplash.com/photo-1518623489648-a173ef7824f3?w=1200",
        use_container_width=True
    )

    st.markdown("### 🎮 Sigue jugando")

    col1, col2 = st.columns(2)

    with col1:
        st.image("https://images.unsplash.com/photo-1596711762462-850f28584813?w=400")
        st.button("JUGAR", key="g1")

    with col2:
        st.image("https://images.unsplash.com/photo-1596711762462-850f28584813?w=400")
        st.button("JUGAR", key="g2")

elif st.session_state.page == "depositos":

    st.markdown("## 📥 Depósitos")

    monto = st.number_input("Monto", min_value=100, step=100)

    if st.button("Confirmar"):
        st.success(f"Depósito de ${monto} realizado")

    if st.button("⬅ Volver"):
        go("inicio")

elif st.session_state.page == "retiros":

    st.markdown("## 💸 Retiros")

    monto = st.number_input("Monto a retirar", min_value=100, step=100)

    if st.button("Solicitar"):
        st.warning(f"Retiro de ${monto} en proceso")

    if st.button("⬅ Volver"):
        go("inicio")

elif st.session_state.page == "mensajes":

    st.markdown("## 💬 Mensajes")
    st.info("No tienes mensajes")

    if st.button("⬅ Volver"):
        go("inicio")

elif st.session_state.page == "logout":

    st.markdown("## 🚪 Sesión cerrada")
    st.success("Has cerrado sesión")

    if st.button("Ir al inicio"):
        go("inicio")

st.markdown('</div>', unsafe_allow_html=True)
