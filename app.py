import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

# ---------------- ESTADO ----------------
if "saldo" not in st.session_state:
    st.session_state.saldo = 5000.00

# ---------------- ESTILOS CSS PERSONALIZADOS ----------------
st.markdown("""
<style>
/* Fondo oscuro general */
.stApp {
    background-color: #0f172a;
}

/* Quitar espacios de Streamlit */
.block-container {
    padding-top: 0rem;
    padding-bottom: 0rem;
}

/* Contenedor del Saldo (pequeño y elegante) */
.balance-box {
    background-color: #1e293b;
    color: white;
    padding: 4px 12px;
    border-radius: 6px;
    font-size: 14px;
    font-weight: 600;
    border: 1px solid #334155;
    display: flex;
    align-items: center;
    height: 35px;
    margin-right: 10px;
}

/* Estilo del Header */
.header-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 0px;
}

/* Ajuste de botones nativos */
.stButton>button {
    height: 35px;
    border-radius: 6px;
    font-weight: bold;
    padding: 0px 15px;
}

/* Botón de JUGAR verde */
.stButton>button[kind="primary"] {
    background-color: #72af24;
    border: none;
    color: white;
    width: 100px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER (LOGOTIPO + CONTROLES) ----------------
# Usamos columnas con proporciones para empujar el saldo a la derecha
col_logo, col_vacio, col_derecha = st.columns([1, 2, 2])

with col_logo:
    try:
        logo = Image.open("Logo.jpg")
        st.image(logo, width=150)
    except:
        st.markdown("<h3 style='color:white; margin:0;'>FORTUNA MX</h3>", unsafe_allow_html=True)

with col_derecha:
    # Sub-columnas para alinear saldo y botones en la esquina superior derecha
    c1, c2, c3 = st.columns([1, 0.8, 0.2])
    
    with c1:
        # Botón de depósito optimizado
        if st.button("💳 Depositar", use_container_width=True):
            st.session_state.saldo += 500
            st.rerun()
            
    with c2:
        # Saldo reducido pegado al icono de usuario
        st.markdown(f"<div class='balance-box'>${st.session_state.saldo:,.2f}</div>", unsafe_allow_html=True)
        
    with c3:
        # Botón de Persona que activa el Sidebar
        if st.button("👤"):
            pass # Streamlit abre el sidebar por defecto si hay contenido

# ---------------- MENÚ LATERAL (RETIROS, DEPÓSITOS, ETC.) ----------------
with st.sidebar:
    st.markdown("### 👤 Mi Cuenta")
    st.write(f"**Saldo disponible:** ${st.session_state.saldo:,.2f}")
    st.markdown("---")
    if st.button("💸 Retiros", use_container_width=True):
        st.write("Cargando sección de retiros...")
    if st.button("💳 Depósitos", use_container_width=True):
        st.write("Cargando sección de depósitos...")
    if st.button("💬 Mensajes", use_container_width=True):
        st.write("No tienes mensajes nuevos.")
    st.markdown("---")
    if st.button("🚪 Cerrar Sesión", use_container_width=True):
        st.warning("Sesión cerrada.")

# ---------------- CONTENIDO PRINCIPAL ----------------
st.markdown("## SIGUE JUGANDO")

# Representación del área de juego negra como en tu imagen
st.markdown("""
<div style="background-color: #000; width: 100%; height: 400px; border-radius: 10px; display: flex; align-items: center; justify-content: center; border: 1px solid #334155;">
    <span style="color: #334155; font-size: 50px;">?</span>
</div>
""", unsafe_allow_html=True)

# Botón JUGAR verde abajo a la izquierda
st.write("")
if st.button("JUGAR", type="primary"):
    st.balloons()

st.markdown("## WINPOT POPULAR")
