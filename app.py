import streamlit as st

# ---------------- CONFIG ----------------
st.set_page_config(layout="wide")

# ---------------- ESTADO ----------------
if "menu" not in st.session_state:
    st.session_state.menu = False

# ---------------- CSS ----------------
st.markdown("""
<style>
header {display:none;}
[data-testid="stHeader"] {display:none;}
.block-container {padding-top: 0rem;}

.main {
    background:#0f1b2a;
    color:white;
}

/* menú */
.menu-box {
    position: fixed;
    top: 70px;
    right: 10px;
    background: #1a232e;
    padding: 10px;
    border-radius: 10px;
    z-index: 9999;
}
</style>
""", unsafe_allow_html=True)

# -------- HEADER REAL (SIN HTML ROTO) --------
with st.container():
    col1, col2, col3 = st.columns([2, 5, 3])

    with col1:
        st.image("Logo.jpg", width=90)

    with col3:
        c1, c2, c3 = st.columns([2,2,1])

        with c1:
            st.markdown(
                '<div style="background:#6be234;padding:6px;border-radius:6px;text-align:center;font-size:12px;">💳 Deposita</div>',
                unsafe_allow_html=True
            )

        with c2:
            st.markdown(
                '<div style="background:#2c3a4d;padding:6px;border-radius:6px;text-align:center;font-size:12px;">$0.32</div>',
                unsafe_allow_html=True
            )

        with c3:
            if st.button("👤"):
                st.session_state.menu = not st.session_state.menu

# -------- MENÚ --------
if st.session_state.menu:
    st.markdown("""
    <div class="menu-box">
        <div>💸 Retiros</div>
        <div>📥 Depósitos</div>
        <div>💬 Mensajes</div>
        <div>🚪 Cerrar sesión</div>
    </div>
    """, unsafe_allow_html=True)

# -------- CONTENIDO --------
st.image(
    "https://images.unsplash.com/photo-1601597111158-2fceff292cdc?w=1200",
    use_container_width=True
)

st.markdown("## Sigue Jugando")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://picsum.photos/200")

with col2:
    st.image("https://picsum.photos/201")

with col3:
    st.image("https://picsum.photos/202")
