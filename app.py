import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Fortuna MX", page_icon="🍀", layout="wide")

# 2. CSS CORREGIDO
st.markdown("""
    <style>
    .stApp { background-color: #0b0e11; }
    header {visibility: hidden;}
    
    /* Contenedor especial para el Logo */
    .logo-container img {
        width: 180px !important; /* Ajusta este valor al tamaño que desees */
        height: auto !important;
        object-fit: contain !important;
        border-radius: 0px !important; /* Quita el redondeo que aplicamos a los juegos */
    }

    /* Estilo para el Saldo */
    .saldo-box {
        background: #1a1f26;
        color: #76b82a;
        padding: 5px 12px;
        border-radius: 5px;
        font-weight: bold;
        font-size: 16px;
        border: 1px solid #2d343f;
        display: inline-block;
    }

    /* SOLO para las imágenes de los juegos */
    .grid-item img {
        border-radius: 8px !important;
        aspect-ratio: 1 / 1;
        object-fit: cover;
    }
    
    /* Botón Perfil (Icono) */
    .stButton > button {
        border-radius: 6px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. HEADER (LOGO Y SALDO)
# Usamos una estructura de columnas limpia
c1, c2 = st.columns([1, 1])

with c1:
    # Usamos HTML para forzar que el logo se vea correctamente y no use el estilo de los juegos
    logo_url = "https://raw.githubusercontent.com/ManuelG-Prog/casino-demo/principal/logo.PNG"
    st.markdown(f'<div class="logo-container"><img src="{logo_url}"></div>', unsafe_allow_html=True)

with c2:
    # Alineación manual a la derecha
    st.markdown(f"""
        <div style="display: flex; justify-content: flex-end; align-items: center; gap: 10px; height: 60px;">
            <div class="saldo-box">${5000:,.2f}</div>
        </div>
    """, unsafe_allow_html=True)
    # El botón de perfil justo debajo o a un lado
    col_vacia, col_btn = st.columns([4, 1])
    with col_btn:
        if st.button("👤", key="perfil"):
            st.toast("Abriendo cuenta...")

# 4. CONTENIDO
st.image("https://images.unsplash.com/photo-1518623489648-a173ef7824f3?w=1200", use_container_width=True)

st.markdown("<div style='color:#8a96a3; font-size:12px; font-weight:bold; margin-top:20px;'>POPULARES</div>", unsafe_allow_html=True)

# Cuadrícula de juegos con clase específica para no romper el logo
cols = st.columns(5)
for i in range(5):
    with cols[i]:
        st.markdown('<div class="grid-item">', unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1596711762462-850f28584813?w=150", use_container_width=True)
        st.button("JUGAR", key=f"btn_{i}", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
