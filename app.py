import streamlit as st

# 1. CONFIGURACIÓN INICIAL
st.set_page_config(page_title="Fortuna MX", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS DE ALTA FIDELIDAD (Estilo Winpot)
st.markdown("""
    <style>
    /* Fondo y Reset */
    .stApp { background-color: #0f172a; }
    header {visibility: hidden;}
    
    /* HEADER FIJO */
    .custom-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 20px;
        background-color: #0f172a;
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 1000;
        height: 60px;
    }

    /* LOGOTIPO: Ajuste de claridad */
    .logo-img {
        height: 40px;
        width: auto;
        object-fit: contain;
    }

    /* CONTENEDOR DE SALDO Y DEPÓSITO */
    .user-actions {
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .deposit-btn {
        background-color: #76b82a;
        color: black;
        padding: 5px 12px;
        border-radius: 5px;
        font-weight: bold;
        font-size: 14px;
        text-decoration: none;
    }

    .balance-badge {
        background-color: #1e293b;
        color: white;
        padding: 5px 10px;
        border-radius: 5px;
        font-family: monospace;
        border: 1px solid #334155;
    }

    /* BANNER PRINCIPAL */
    .main-banner {
        width: 100%;
        border-radius: 15px;
        margin-top: 70px;
        margin-bottom: 20px;
    }

    /* GRID DE JUEGOS */
    .game-card {
        border-radius: 10px;
        overflow: hidden;
        margin-bottom: 10px;
        transition: transform 0.2s;
    }
    .game-card:hover { transform: scale(1.05); }
    
    /* Etiquetas de sección */
    .section-title {
        color: white;
        font-size: 16px;
        font-weight: bold;
        margin: 20px 0 10px 0;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Ocultar elementos nativos que estorban */
    [data-testid="stHeader"] {display: none;}
    div.block-container {padding-top: 2rem;}
    </style>
    """, unsafe_allow_html=True)

# 3. HEADER PERSONALIZADO (Logo siempre visible)
logo_url = "https://raw.githubusercontent.com/ManuelG-Prog/casino-demo/principal/logo.PNG"

st.markdown(f"""
    <div class="custom-header">
        <img src="{logo_url}" class="logo-img">
        <div class="user-actions">
            <div class="deposit-btn">📥 Deposta</div>
            <div class="balance-badge">$ 5,000.00</div>
            <div style="color: white; font-size: 20px;">👤</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 4. BANNER (Imagen Principal)
st.markdown('<img src="https://images.unsplash.com/photo-1518623489648-a173ef7824f3?w=1200" class="main-banner">', unsafe_allow_html=True)

# 5. SECCIONES DE JUEGOS
def render_section(titulo):
    st.markdown(f'<div class="section-title">{titulo}</div>', unsafe_allow_html=True)
    
    # Usamos columnas de Streamlit para la rejilla
    cols = st.columns(4) # 4 juegos por fila para que se vean grandes
    for i in range(4):
        with cols[i]:
            # Contenedor de imagen de juego
            st.markdown('<div class="game-card">', unsafe_allow_html=True)
            st.image(f"https://images.unsplash.com/photo-1596711762462-850f28584813?w=300", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
            st.button("JUGAR", key=f"{titulo}_{i}", use_container_width=True)

# Dibujar las secciones
render_section("Sigue Jugando")
render_section("Fortuna Popular")

# 6. MENÚ INFERIOR (Opcional, estilo móvil)
st.markdown("""
    <div style="position: fixed; bottom: 0; left: 0; right: 0; background: #1e293b; display: flex; justify-content: space-around; padding: 10px; border-top: 1px solid #334155; z-index: 1000;">
        <div style="text-align: center; color: white; font-size: 10px;">🏠<br>Inicio</div>
        <div style="text-align: center; color: white; font-size: 10px;">📥<br>Deposta</div>
        <div style="text-align: center; color: white; font-size: 10px;">🎰<br>Slots</div>
        <div style="text-align: center; color: white; font-size: 10px;">☰<br>Menú</div>
    </div>
    <div style="height: 60px;"></div>
    """, unsafe_allow_html=True)
