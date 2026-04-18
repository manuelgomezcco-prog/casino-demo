import streamlit as st

# ---------------- CONFIG ----------------
st.set_page_config(layout="wide")

# ---------------- ESTADO ----------------
if "menu" not in st.session_state:
    st.session_state.menu = False

# ---------------- CSS ----------------
st.markdown("""
<style>

/* RESET */
html, body, .stApp {
    margin: 0;
    padding: 0;
    background: #0f1b2a;
    color: white;
}

header {display:none;}
[data-testid="stHeader"] {display:none;}

.block-container {
    padding-top: 0 !important;
}

/* HEADER */
.header {
    position: fixed;
    top: 0;
    width: 100%;
    height: 70px;
    background: #162334;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 15px;
    z-index: 999;
}

/* LOGO */
.logo {
    position: absolute;
    left: 15px;
    top: 50%;
    transform: translateY(-50%);
}

/* DERECHA */
.right {
    position: absolute;
    right: 15px;
    top: 50%;
    transform: translateY(-50%);
    display: flex;
    gap: 10px;
    align-items: center;
}

/* BOTONES */
.deposit {
    background: #6be234;
    color: black;
    padding: 8px 14px;
    border-radius: 8px;
    font-weight: bold;
}

.balance {
    background: #2c3a4d;
    padding: 8px 12px;
    border-radius: 8px;
}

.user-btn button {
    background: #2c3a4d;
    border-radius: 8px;
}

/* MENÚ */
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

/* CATEGORÍAS */
.cats {
    display: flex;
    gap: 10px;
    overflow-x: auto;
    margin-top: 15px;
}

.cat {
    min-width: 90px;
    background: #1c2b3f;
    padding: 12px;
    border-radius: 12px;
    text-align: center;
}

/* JUEGOS */
.games {
    display: flex;
    gap: 10px;
    overflow-x: auto;
}

.game img {
    border-radius: 12px;
    width: 120px;
}

/* FOOTER */
.footer {
    position: fixed;
    bottom: 0;
    width: 100%;
    background: rgba(20,30,45,0.9);
    display: flex;
    justify-content: space-around;
    padding: 10px 0;
}

/* BOTÓN FLOTANTE */
.search {
    position: fixed;
    bottom: 70px;
    right: 20px;
    background: radial-gradient(circle, #ff2d75, #a800ff);
    width: 60px;
    height: 60px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<div class="header">', unsafe_allow_html=True)

# LOGO (LOCAL - FUNCIONA SIEMPRE)
st.markdown('<div class="logo">', unsafe_allow_html=True)
st.image("Logo.jpg", width=110)
st.markdown('</div>', unsafe_allow_html=True)

# BOTONES DERECHA
st.markdown('<div class="right">', unsafe_allow_html=True)

col1, col2, col3 = st.columns([2,2,1])

with col1:
    st.markdown('<div class="deposit">💳 Deposita</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="balance">$0.32</div>', unsafe_allow_html=True)

with col3:
    if st.button("👤", key="user_btn"):
        st.session_state.menu = not st.session_state.menu

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

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

# ---------------- CONTENIDO ----------------
st.markdown('<div class="main">', unsafe_allow_html=True)

# BANNER
st.image(
    "https://images.unsplash.com/photo-1601597111158-2fceff292cdc?w=1200",
    use_container_width=True
)

# CATEGORÍAS
st.markdown("""
<div class="cats">
    <div class="cat">🔍</div>
    <div class="cat">🏠 Hogar</div>
    <div class="cat">🆕 Nuevo</div>
    <div class="cat">🎰 Slots</div>
    <div class="cat">🔥 En Vivo</div>
</div>
""", unsafe_allow_html=True)

st.markdown("## Sigue Jugando")

# JUEGOS
st.markdown("""
<div class="games">
    <div class="game"><img src="https://picsum.photos/200"></div>
    <div class="game"><img src="https://picsum.photos/201"></div>
    <div class="game"><img src="https://picsum.photos/202"></div>
    <div class="game"><img src="https://picsum.photos/203"></div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
    <div>🏠 Inicio</div>
    <div>💳 Deposita</div>
    <div>🎥 En Vivo</div>
    <div>☰ Menú</div>
</div>

<div class="search">🔍</div>
""", unsafe_allow_html=True)
