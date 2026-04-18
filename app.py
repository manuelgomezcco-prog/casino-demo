import streamlit as st

st.set_page_config(layout="wide")

# -------- ESTADO --------
if "menu" not in st.session_state:
    st.session_state.menu = False

# -------- CSS --------
st.markdown("""
<style>

/* RESET */
html, body, .stApp {
    margin: 0;
    padding: 0;
    background: #0f1b2a;
    color: white;
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
.logo img {
    height: 35px;
}

/* RIGHT BUTTONS */
.right {
    display: flex;
    gap: 10px;
    align-items: center;
}

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

.user {
    background: #2c3a4d;
    padding: 8px;
    border-radius: 8px;
    cursor: pointer;
}

/* BANNER */
.banner {
    margin-top: 80px;
}

.banner img {
    border-radius: 15px;
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

/* GRID JUEGOS */
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
    backdrop-filter: blur(10px);
}

/* BOTÓN FLOTANTE */
.search {
    position: fixed;
    bottom: 60px;
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

# -------- HEADER --------
st.markdown("""
<div class="header">
    <div class="logo">
        <img src="https://i.imgur.com/8Km9tLL.png">
    </div>
    <div class="right">
        <div class="deposit">💳 Deposita</div>
        <div class="balance">$0.32</div>
        <div class="user">👤</div>
    </div>
</div>
""", unsafe_allow_html=True)

# -------- BANNER --------
st.markdown("""
<div class="banner">
    <img src="https://images.unsplash.com/photo-1601597111158-2fceff292cdc?w=1200">
</div>
""", unsafe_allow_html=True)

# -------- CATEGORÍAS --------
st.markdown("""
<div class="cats">
    <div class="cat">🔍</div>
    <div class="cat">🏠 Hogar</div>
    <div class="cat">🆕 Nuevo</div>
    <div class="cat">🎰 Slots</div>
    <div class="cat">🔥 En Vivo</div>
</div>
""", unsafe_allow_html=True)

st.markdown("### Sigue Jugando")

# -------- JUEGOS --------
st.markdown("""
<div class="games">
    <div class="game"><img src="https://i.imgur.com/3ZQ3Z3K.png"></div>
    <div class="game"><img src="https://i.imgur.com/0rVeh4A.png"></div>
    <div class="game"><img src="https://i.imgur.com/ZK7dF8R.png"></div>
    <div class="game"><img src="https://i.imgur.com/3ZQ3Z3K.png"></div>
</div>
""", unsafe_allow_html=True)

st.markdown("### Winpot Popular")

st.markdown("""
<div class="games">
    <div class="game"><img src="https://i.imgur.com/0rVeh4A.png"></div>
    <div class="game"><img src="https://i.imgur.com/ZK7dF8R.png"></div>
    <div class="game"><img src="https://i.imgur.com/3ZQ3Z3K.png"></div>
</div>
""", unsafe_allow_html=True)

# -------- FOOTER --------
st.markdown("""
<div class="footer">
    <div>🏠 Inicio</div>
    <div>💳 Deposita</div>
    <div>🎥 En Vivo</div>
    <div>☰ Menú</div>
</div>

<div class="search">🔍</div>
""", unsafe_allow_html=True)
