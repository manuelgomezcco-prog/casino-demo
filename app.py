import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Fortuna MX", layout="wide", initial_sidebar_state="collapsed")

# 2. CSS DE ALTA FIDELIDAD
st.markdown("""
    <style>
    .stApp { background-color: #0b0e11; }
    header {visibility: hidden;}
    [data-testid="stHeader"] {display: none;}
    
    /* HEADER FIJO Y LIMPIO */
    .custom-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 15px;
        background-color: #1a1f26;
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 1000;
        height: 65px;
        border-bottom: 1px solid #2d343f;
    }

    /* LOGO: Forzamos visibilidad */
    .logo-container img {
        max-height: 45px;
        width: auto;
        display: block;
    }

    .user-actions {
        display: flex;
        align-items: center;
        gap: 8px;
    }

    /* BOTÓN DEPOSITAR CORREGIDO */
    .deposit-btn {
        background-color: #76b82a;
        color: #000 !important;
        padding: 6px 14px;
        border-radius: 6px;
        font-weight: bold;
        font-size: 13px;
        text-decoration: none;
        display: flex;
        align-items: center;
        gap: 5px;
    }

    .balance-badge {
        background-color: #2d343f;
        color: #fff;
        padding: 6px 12px;
        border-radius: 6px;
        font-weight: bold;
        font-size: 13px;
        border: 1px solid #3e4652;
    }

    /* Ajuste de Banner */
    .banner-container {
        margin-top: 80px;
        width: 100%;
    }
    .banner-container img {
        border-radius: 15px;
        width: 100%;
    }

    .section-title {
        color: white;
        font-size: 15px;
        font-weight: bold;
        margin: 25px 0 15px 0;
        text-transform: uppercase;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. LOGO Y HEADER (Corregido)
# Usamos la URL raw de GitHub que es la que permite visualización directa
logo_url = "https://raw.githubusercontent.com/ManuelG-Prog/casino-demo/principal/logo.PNG"

st.markdown(f"""
    <div class="custom-header">
        <div class="logo-container">
            <img src="{logo_url}" alt="Fortuna MX">
        </div>
        <div class="user-actions">
            <a class="deposit-btn">📥 Depositar</a>
            <div class="balance-badge">$ 5,000.00</div>
            <div style="color: #8a96a3; font-size: 22px; margin-left: 5px;">👤</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 4. CONTENIDO PRINCIPAL
st.markdown(f"""
    <div class="banner-container">
        <img src="https://images.unsplash.com/photo-1518623489648-a173ef7824f3?w=1200">
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-title">Sigue Jugando</div>', unsafe_allow_html=True)

# 5. CUADRÍCULA DE JUEGOS (Sin errores de ceros)
cols = st.columns(2) # 2 columnas para que en móvil se vean bien grandes
img_game = "https://images.unsplash.com/photo-1596711762462-850f28584813?w=400"

for i in range(2):
    with cols[i]:
        st.image(img_game, use_container_width=True)
        st.button("JUGAR", key=f"game_{i}", use_container_width=True)

# 6. MENÚ INFERIOR ESTILO APP
st.markdown("""
    <div style="position: fixed; bottom: 0; left: 0; right: 0; background: #1a1f26; display: flex; justify-content: space-around; padding: 12px; border-top: 1px solid #2d343f; z-index: 1000;">
        <div style="text-align: center; color: white; font-size: 11px;">🏠<br>Inicio</div>
        <div style="text-align: center; color: white; font-size: 11px;">📥<br>Depositar</div>
        <div style="text-align: center; color: white; font-size: 11px;">🎰<br>Slots</div>
        <div style="text-align: center; color: white; font-size: 11px;">☰<br>Menú</div>
    </div>
    <div style="height: 70px;"></div>
    """, unsafe_allow_html=True)
