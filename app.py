import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="Fortuna MX",
    page_icon="🍀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. CSS OPTIMIZADO
st.markdown("""
    <style>
    .stApp { background-color: #0b0e11; }
    header {visibility: hidden;}
    
    /* Contenedor del Header para alinear Logo y Saldo */
    .header-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 5px 0px;
        margin-bottom: 10px;
    }

    /* ESTILO ESPECÍFICO PARA LA CUADRÍCULA DE JUEGOS */
    /* Usamos un selector que no afecte a las columnas del header */
    [data-testid="stVerticalBlock"] > [data-testid="stHorizontalBlock"] {
        gap: 6px !important;
    }

    /* Solo aplicar el ancho del 19% a las columnas de la cuadrícula de juegos */
    .grid-column [data-testid="column"] {
        width: 19% !important;
        flex: 1 1 19% !important;
        min-width: 60px !important;
    }

    /* Ajuste de imágenes de juegos */
    [data-testid="stImage"] img {
        border-radius: 6px !important;
        aspect-ratio: 1 / 1;
        object-fit: cover;
    }
    
    /* Botón Jugar */
    .stButton > button {
        background-color: #76b82a !important;
        color: white !important;
        font-size: 9px !important;
        height: 22px !important;
        width: 100%;
        border-radius: 4px !important;
        border: none !important;
        text-transform: uppercase;
        font-weight: bold;
    }

    .section-label {
        color: #8a96a3;
        font-size: 11px;
        font-weight: bold;
        margin: 15px 0 5px 0;
        text-transform: uppercase;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. LÓGICA DE USUARIO
if 'saldo' not in st.session_state: st.session_state.saldo = 5000.0

@st.dialog("Cuenta")
def mostrar_perfil():
    st.write(f"### 👤 Manuel Gómez")
    st.divider()
    st.button("💰 Depósitos", use_container_width=True)
    st.button("💸 Retiros", use_container_width=True)
    if st.button("🚪 Salir", type="primary", use_container_width=True):
        st.session_state.clear()
        st.rerun()

# 4. HEADER (LOGO Y ÁREA DE SALDO)
# Usamos columnas con proporciones para proteger el tamaño del logo
head_left, head_right = st.columns([2, 1])

with head_left:
    # El logo mantiene su tamaño original
    st.image("https://raw.githubusercontent.com/ManuelG-Prog/casino-demo/principal/logo.PNG", width=120)

with head_right:
    # Saldo y Botón alineados a la derecha
    col_s, col_p = st.columns([3, 1])
    with col_s:
        st.markdown(f"""
            <div style="display: flex; justify-content: flex-end; align-items: center; height: 35px;">
                <div style="background:#1a1f26; color:#76b82a; padding:5px 10px; border-radius:5px; font-weight:bold; font-size:14px; border:1px solid #2d343f;">
                    ${st.session_state.saldo:,.2f}
                </div>
            </div>
        """, unsafe_allow_html=True)
    with col_p:
        if st.button("👤", key="btn_perfil"):
            mostrar_perfil()

# 5. CONTENIDO PRINCIPAL
st.image("https://images.unsplash.com/photo-1518623489648-a173ef7824f3?w=1200", use_container_width=True)

def render_grid(titulo, n_items):
    st.markdown(f"<div class='section-label'>{titulo}</div>", unsafe_allow_html=True)
    img_placeholder = "https://images.unsplash.com/photo-1596711762462-850f28584813?w=150"
    
    # Creamos la cuadrícula
    # Nota: Para móviles, 5 columnas pueden ser muy pequeñas, pero aquí forzamos la estructura
    for fila in range(0, n_items, 5):
        cols = st.columns(5)
        for i in range(5):
            if (fila + i) < n_items:
                with cols[i]:
                    st.image(img_placeholder, use_container_width=True)
                    st.button("Jugar", key=f"p_{titulo}_{fila+i}")

render_grid("Populares", 10)
render_grid("Nuevos Lanzamientos", 5)
