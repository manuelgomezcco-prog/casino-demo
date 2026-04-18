import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

# ---------------- ESTADO ----------------
if "saldo" not in st.session_state:
    st.session_state.saldo = 1000.00

# ---------------- ESTILOS ----------------
st.markdown("""
<style>
/* Fondo y contenedor */
.block-container {
    padding-top: 1rem;
    background-color: #0f172a;
}

/* Caja de Saldo Compacta */
.balance-container {
    background-color: #1e293b;
    color: #f8fafc;
    padding: 5px 12px;
    border-radius: 8px;
    font-size: 14px;
    border: 1px solid #334155;
    font-weight: bold;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 38px;
    min-width: 80px;
}

/* Ajuste de botones para que sean uniformes */
.stButton>button {
    height: 38px;
    border-radius: 8px;
    font-weight: bold;
}

/* Quitar padding innecesario de las columnas */
[data-testid="column"] {
    display: flex;
    align-items: center;
    justify-content: flex-end;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
# Dividimos en 2 grandes bloques: Logo (izquierda) y Controles (derecha)
col_logo, col_controles = st.columns([1, 1])

with col_logo:
    try:
        # Alineamos el logo a la izquierda
        logo = Image.open("Logo.jpg")
        st.image(logo, width=170)
    except:
        st.header("FORTUNA MX")

with col_controles:
    # Sub-columnas muy ajustadas para mover todo a la derecha
    # c1: Depósito, c2: Saldo, c3: Menú Persona
    c1, c2, c3 = st.columns([0.4, 0.3, 0.15])
    
    with c1:
        if st.button("💳 Depositar", use_container_width=True):
            st.session_state.saldo += 500
            st.rerun()
            
    with c2:
        # Contenedor de saldo reducido
        st.markdown(f"<div class='balance-container'>${st.session_state.saldo:,.2f}</div>", unsafe_allow_html=True)
        
    with c3:
        # El botón de persona ahora dispara el menú en la barra lateral
        if st.button("👤", use_container_width=True):
            st.session_state.show_menu = True

# ---------------- MENÚ DESPLEGABLE (Sidebar) ----------------
# Usamos el Sidebar para un menú limpio y profesional
with st.sidebar:
    st.title("Mi Cuenta")
    st.markdown("---")
    if st.button("💸 Retiros", use_container_width=True):
        st.info("Sección de Retiros")
    if st.button("💳 Depósitos", use_container_width=True):
        st.info("Sección de Depósitos")
    if st.button("💬 Mensajes", use_container_width=True):
        st.info("Tienes 0 mensajes nuevos")
    st.markdown("---")
    if st.button("🚪 Cerrar Sesión", use_container_width=True):
        st.warning("Cerrando sesión...")

# ---------------- BANNER ----------------
st.image("https://images.unsplash.com/photo-1601597111158-2fceff292cdc", use_column_width=True)

# ---------------- SECCIONES DE JUEGOS ----------------
st.markdown("### 🎰 SIGUE JUGANDO")
cols = st.columns(4)
juegos = [("30 Spicy Fruits", "EGT"), ("40 Shining Crown", "EGT"), ("Leprechaun Hot", "PRAGMATIC"), ("Mega Slot", "FORTUNA")]

for i, (titulo, dev) in enumerate(juegos):
    with cols[i]:
        st.markdown(f"""
        <div style='background:#1e293b; padding:15px; border-radius:12px; text-align:center; border:1px solid #334155;'>
            <div style='font-weight:bold;'>{titulo}</div>
            <div style='color:#94a3b8; font-size:10px;'>{dev}</div>
        </div>
        """, unsafe_allow_html=True)
        st.button("Jugar", key=f"btn_{i}", use_container_width=True)
