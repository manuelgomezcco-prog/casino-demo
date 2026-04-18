import streamlit as st
import base64
import requests

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Fortuna MX", layout="wide", initial_sidebar_state="collapsed")

# 2. FUNCIÓN ANTI-BLOQUEO (Usando Proxy de imágenes)
@st.cache_data
def get_base64_img(url):
    # Usamos un proxy de imágenes para saltar el bloqueo de GitHub
    proxy_url = f"https://images.weserv.nl/?url={url.replace('https://', '')}"
    try:
        response = requests.get(proxy_url, timeout=10)
        if response.status_code == 200:
            return base64.b64encode(response.content).decode()
    except Exception as e:
        return ""
    return ""

# URL corregida de tu logo
url_logo = "raw.githubusercontent.com/ManuelG-Prog/casino-demo/principal/logo.PNG"
logo_data = get_base64_img(url_logo)

# 3. CSS PROFESIONAL
st.markdown(f"""
    <style>
    .stApp {{ background-color: #0b0e11; }}
    [data-testid="stHeader"] {{display: none;}}
    header {{visibility: hidden;}}
    
    .custom-header {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 5px 15px;
        background-color: #1a1f26;
        position: fixed;
        top: 0; left: 0; right: 0;
        z-index: 99999;
        height: 65px;
        border-bottom: 1px solid #2d343f;
    }}

    /* Contenedor del Logo */
    .logo-box {{
        display: flex;
        align-items: center;
        min-width: 120px;
    }}

    .logo-box img {{
        max-height: 45px;
        width: auto;
        filter: drop-shadow(0px 0px 2px rgba(255,255,255,0.2));
    }}

    .user-actions {{
        display: flex;
        align-items: center;
        gap: 10px;
    }}

    .deposit-btn {{
        background-color: #76b82a;
        color: #000 !important;
        padding: 8px 12px;
        border-radius: 6px;
        font-weight: bold;
        font-size: 13px;
        text-decoration: none;
    }}

    .balance-badge {{
        background-color: #2d343f;
        color: #fff;
        padding: 8px 10px;
        border-radius: 6px;
        font-weight: bold;
        font-size: 13px;
        border: 1px solid #3e4652;
    }}

    .main-content {{ margin-top: 85px; }}
    
    .section-title {{
        color: white;
        font-size: 16px;
        font-weight: bold;
        margin: 20px 0;
        text-transform: uppercase;
    }}
    </style>

    <div class="custom-header">
        <div class="logo-box">
            <img src="data:image/png;base64,{logo_data}" onerror="this.src='https://via.placeholder.com/150x50?text=Fortuna+MX'">
        </div>
        <div class="user-actions">
            <a class="deposit-btn">📥 Depositar</a>
            <div class="balance-badge">$ 5,000.00</div>
            <div style="color: #8a96a3; font-size: 24px;">👤</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 4. CONTENIDO
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Banner
st.image("https://images.unsplash.com/photo-1518623489648-a173ef7824f3?w=1200", use_container_width=True)

st.markdown('<div class="section-title">Sigue Jugando</div>', unsafe_allow_html=True)

# Rejilla limpia de 2 columnas
c1, c2 = st.columns(2)
with c1:
    st.image("https://images.unsplash.com/photo-1596711762462-850f28584813?w=400", use_container_width=True)
    st.button("JUGAR", key="g1", use_container_width=True)
with c2:
    st.image("https://images.unsplash.com/photo-1596711762462-850f28584813?w=400", use_container_width=True)
    st.button("JUGAR", key="g2", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# 5. MENÚ INFERIOR
st.markdown("""
    <div style="position: fixed; bottom: 0; left: 0; right: 0; background: #1a1f26; display: flex; justify-content: space-around; padding: 12px; border-top: 1px solid #2d343f; z-index: 99999;">
        <div style="text-align: center; color: white; font-size: 11px;">🏠<br>Inicio</div>
        <div style="text-align: center; color: #76b82a; font-size: 11px;">📥<br>Depositar</div>
        <div style="text-align: center; color: white; font-size: 11px;">🎰<br>Slots</div>
        <div style="text-align: center; color: white; font-size: 11px;">☰<br>Menú</div>
    </div>
    <div style="height: 70px;"></div>
    """, unsafe_allow_html=True)
