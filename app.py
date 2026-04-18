import streamlit as st

# ---------------- CONFIG ----------------
st.set_page_config(layout="wide")

# ---------------- ESTADO ----------------
if "menu" not in st.session_state:
    st.session_state.menu = False

# ---------------- CSS GLOBAL ----------------
st.markdown("""
<style>
html, body, .stApp {
    margin: 0;
    padding: 0;
    background: #0f1b2a;
    color: white;
}

header {display:none;}
[data-testid="stHeader"] {display:none;}
.block-container {padding-top: 0 !important;}

/* MENU */
.menu-box {
    position: fixed;
    top: 70px;
    right: 10px;
    width: 200px;
    background: #1a232e;
    border-radius: 10px;
    padding: 10px;
    z-index: 9999;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER (HTML PURO) ----------------
st.markdown("""
<div style="
position:fixed;
top:0;
left:0;
right:0;
height:65px;
background:#162334;
z-index:9999;
display:flex;
align-items:center;
justify-content:space-between;
padding:0 12px;
">

    <!-- LOGO -->
    <img src="Logo.jpg" style="height:40px; border-radius:6px;">

    <!-- DERECHA -->
    <div style="display:flex; gap:6px; align-items:center;">

        <div style="
        background:#6be234;
        color:black;
        padding:6px 10px;
        border-radius:6px;
        font-weight:bold;
        font-size:12px;">
        💳 Deposita
        </div>

        <div style="
        background:#2c3a4d;
        padding:6px 10px;
        border-radius:6px;
        font-size:12px;">
        $0.32
        </div>

    </div>
</div>
""", unsafe_allow_html=True)

# -------- BOTÓN REAL 👤 (STREAMLIT) --------
# Lo posicionamos encima del header
st.markdown("""
<div style="position:fixed; top:12px; right:10px; z-index:10000;">
""", unsafe_allow_html=True)

if st.button("👤", key="user_btn"):
    st.session_state.menu = not st.session_state.menu

st.markdown("</div>", unsafe_allow_html=True)

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

# -------- ESPACIO PARA NO TAPAR CONTENIDO --------
st.markdown('<div style="margin-top:80px;"></div>', unsafe_allow_html=True)

# ---------------- CONTENIDO ----------------

# Banner
st.image(
    "https://images.unsplash.com/photo-1601597111158-2fceff292cdc?w=1200",
    use_container_width=True
)

# Categorías
st.markdown("""
<div style="display:flex; gap:10px; overflow-x:auto; margin-top:15px;">
    <div style="min-width:90px; background:#1c2b3f; padding:12px; border-radius:12px;">🔍</div>
    <div style="min-width:90px; background:#1c2b3f; padding:12px; border-radius:12px;">🏠 Hogar</div>
    <div style="min-width:90px; background:#1c2b3f; padding:12px; border-radius:12px;">🆕 Nuevo</div>
    <div style="min-width:90px; background:#1c2b3f; padding:12px; border-radius:12px;">🎰 Slots</div>
    <div style="min-width:90px; background:#1c2b3f; padding:12px; border-radius:12px;">🔥 En Vivo</div>
</div>
""", unsafe_allow_html=True)

st.markdown("## Sigue Jugando")

# Juegos
st.markdown("""
<div style="display:flex; gap:10px; overflow-x:auto;">
    <img src="https://picsum.photos/200" style="border-radius:12px; width:120px;">
    <img src="https://picsum.photos/201" style="border-radius:12px; width:120px;">
    <img src="https://picsum.photos/202" style="border-radius:12px; width:120px;">
    <img src="https://picsum.photos/203" style="border-radius:12px; width:120px;">
</div>
""", unsafe_allow_html=True)

# -------- BOTÓN FLOTANTE --------
st.markdown("""
<div style="
position:fixed;
bottom:70px;
right:20px;
background: radial-gradient(circle, #ff2d75, #a800ff);
width:60px;
height:60px;
border-radius:50%;
display:flex;
align-items:center;
justify-content:center;
font-size:20px;
z-index:9999;
">
🔍
</div>
""", unsafe_allow_html=True)

# -------- FOOTER --------
st.markdown("""
<div style="
position:fixed;
bottom:0;
width:100%;
background:rgba(20,30,45,0.9);
display:flex;
justify-content:space-around;
padding:10px 0;
">
<div>🏠 Inicio</div>
<div>💳 Deposita</div>
<div>🎥 En Vivo</div>
<div>☰ Menú</div>
</div>
""", unsafe_allow_html=True)
