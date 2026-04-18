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
/* Quitar espacio superior innecesario */
.block-container {
    padding-top: 1rem;
}

/* Contenedor para alinear el saldo y el icono de persona */
.right-align {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    gap: 10px;
}

/* Estilo para la caja de saldo */
.balance-box {
    background-color: #2c3a4d;
    color: white;
    padding: 6px 15px;
    border-radius: 8px;
    font-weight: bold;
    font-size: 14px;
    border: 1px solid #3d4e63;
    display: flex;
    align-items: center;
    height: 38px;
}

/* Ajuste de los botones para que no se desalineen */
.stButton>button {
    width: 100%;
    border-radius: 8px;
}

/* Estilo del menú flotante */
.menu-dropdown {
    position: absolute;
    right: 0;
    top: 10px;
    background: #1e2a38;
    padding: 15px;
    border-radius: 10px;
    width: 180px;
    z-index: 1000;
    border: 1px solid #3d4e63;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
# Usamos una distribución de columnas donde la última sea para los elementos de la derecha
col_logo, col_espacio, col_derecha = st.columns([2, 2, 3])

with col_logo:
    # Ajustamos el tamaño para que luzca bien
    try:
        logo = Image.open("Logo.jpg")
        st.image(logo, width=180)
    except:
        st.subheader("FORTUNA MX")

with col_derecha:
    # Sub-columnas internas para alinear Depositar, Saldo y Perfil
    c1, c2, c3 = st.columns([1, 1, 0.4])
    
    with c1:
        if st.button("💳 Depositar"):
            st.session_state.saldo += 500
            st.rerun()

    with c2:
        st.markdown(f"""
            <div class="right-align">
                <div class="balance-box">${st.session_state.saldo}</div>
            </div>
        """, unsafe_allow_html=True)

    with c3:
        if st.button("👤"):
            st.session_state.menu = not st.session_state.menu
            st.rerun()

# ---------------- MENÚ DESPLEGABLE ----------------
if st.session_state.menu:
    with col_derecha:
        st.markdown("""
        <div class='menu-dropdown'>
            💸 <b>Retiros</b><br><hr style='margin:10px 0; opacity:0.2;'>
            💳 <b>Depósitos</b><br><hr style='margin:10px 0; opacity:0.2;'>
            💬 <b>Mensajes</b><br><hr style='margin:10px 0; opacity:0.2;'>
            🚪 <b>Cerrar sesión</b>
        </div>
        """, unsafe_allow_html=True)

st.write("---")

# ---------------- BANNER Y CONTENIDO ----------------
st.image("https://images.unsplash.com/photo-1601597111158-2fceff292cdc", use_column_width=True)

st.markdown("## 🎰 Sigue Jugando")

# ---------------- LÓGICA CASINO ----------------
def jugar(costo):
    if st.session_state.saldo >= costo:
        if random.random() < 0.4:
            ganancia = costo * 2
            st.session_state.saldo += ganancia
            st.toast(f"¡Ganaste ${ganancia}!", icon="🎉")
        else:
            st.session_state.saldo -= costo
            st.toast(f"Perdiste ${costo}", icon="😞")
    else:
        st.error("Saldo insuficiente")

# ---------------- JUEGOS ----------------
j1, j2, j3 = st.columns(3)

with j1:
    st.markdown("<div style='background:#13263a; padding:20px; border-radius:12px; text-align:center;'>🍒 Slot Básico</div>", unsafe_allow_html=True)
    if st.button("Jugar $50", key="b1"):
        jugar(50)

with j2:
    st.markdown("<div style='background:#13263a; padding:20px; border-radius:12px; text-align:center;'>👑 Slot Premium</div>", unsafe_allow_html=True)
    if st.button("Jugar $100", key="b2"):
        jugar(100)

with j3:
    st.markdown("<div style='background:#13263a; padding:20px; border-radius:12px; text-align:center;'>💎 Mega Slot</div>", unsafe_allow_html=True)
    if st.button("Jugar $200", key="b3"):
        jugar(200)
