import streamlit as st

# CONFIG
st.set_page_config(
    page_title="Fortuna MX",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ESTADO PARA MENÚ
if "menu_open" not in st.session_state:
    st.session_state.menu_open = False

# CSS LIMPIO Y CORREGIDO
st.markdown("""
<style>
/* ELIMINA ESPACIOS SUPERIORES */
.stApp {
    background-color: #0b1118;
}
header {visibility: hidden;}
[data-testid="stHeader"] {display: none;}
.block-container {
    padding-top: 0rem !important;
}

/* HEADER */
.custom-header {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    height: 70px;
    background: #1a232e;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 15px;
    z-index: 9999;
    border-bottom: 1px solid #2d343f;
}

/* CONTENIDO */
.main {
    margin-top: 80px;
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
    font-size: 13px;
}

/* MENÚ DROPDOWN */
.menu-box {
    position: absolute;
    top: 70px;
    right: 10px;
    background: #1a232e;
    border: 1px solid #2d343f;
    border-radius: 8px;
    width: 180px;
    padding: 10px;
    z-index: 9999;
}

.menu-item {
    padding: 10px;
    color: white;
    cursor: pointer;
}

.menu-item:hover {
    background: #2d343f;
    border-radius: 5px;
}
</style>
""", unsafe_allow_html=True)

# HEADER
st.markdown('<div class="custom-header">', unsafe_allow_html=True)

col1, col2 = st.columns([1, 3])

with col1:
    st.image("Logo.jpg", width=110)

with col2:
    c1, c2, c3 = st.columns([2,2,1])

    with c1:
        st.markdown('<div class="btn">📥 Depositar</div>', unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="saldo">$ 5,000.00</div>', unsafe_allow_html=True)

    with c3:
        if st.button("👤"):
            st.session_state.menu_open = not st.session_state.menu_open

st.markdown('</div>', unsafe_allow_html=True)

# MENÚ DESPLEGABLE
if st.session_state.menu_open:
    st.markdown("""
        <div class="menu-box">
            <div class="menu-item">💸 Retiros</div>
            <div class="menu-item">📥 Depósitos</div>
            <div class="menu-item">💬 Mensajes</div>
            <div class="menu-item">🚪 Cerrar sesión</div>
        </div>
    """, unsafe_allow_html=True)

# CONTENIDO
st.markdown('<div class="main">', unsafe_allow_html=True)

# Banner
st.image(
    "https://images.unsplash.com/photo-1518623489648-a173ef7824f3?w=1200",
    use_container_width=True
)

# Título
st.markdown(
    '<div style="color:white; font-weight:bold; margin:20px 0 10px;">SIGUE JUGANDO</div>',
    unsafe_allow_html=True
)

# Juegos
col1, col2 = st.columns(2)

with col1:
    st.image(
        "https://images.unsplash.com/photo-1596711762462-850f28584813?w=400",
        use_container_width=True
    )
    st.button("JUGAR", key="g1", use_container_width=True)

with col2:
    st.image(
        "https://images.unsplash.com/photo-1596711762462-850f28584813?w=400",
        use_container_width=True
    )
    st.button("JUGAR", key="g2", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)
