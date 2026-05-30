```python
import streamlit as st
import random
import time
import base64
import os
from PIL import Image

st.set_page_config(layout="wide", page_title="Fortuna MX - Casino")

# ---------------- PERSISTENCIA DE SALDO ----------------
if "saldo" not in st.session_state:
    st.session_state.saldo = 5000.00

# ---------------- FUNCIÓN PARA CARGAR LOGO EN BASE64 ----------------
def obtener_logo_base64():
    # Intentamos buscar el archivo de logo con diferentes nombres comunes
    nombres_posibles = ["Logo.jpg", "logo.jpg", "Logo.png", "logo.png"]
    for nombre in nombres_posibles:
        if os.path.exists(nombre):
            try:
                with open(nombre, "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read()).decode()
                    # Retornamos el formato correcto según la extensión
                    ext = nombre.split(".")[-1].lower()
                    mime = "jpeg" if ext == "jpg" else ext
                    return f"data:image/{mime};base64,{encoded_string}"
            except Exception:
                pass
    return None

logo_base64 = obtener_logo_base64()

# ---------------- ESTILOS CSS PERSONALIZADOS ----------------
st.markdown("""
<style>
/* --- OCULTAR BARRA SUPERIOR DE GITHUB Y MENÚS DE DEPURACIÓN (MANDATORIO) --- */
[data-testid="stHeader"] {
    display: none !important;
}
#MainMenu {
    visibility: hidden;
}
footer {
    visibility: hidden;
}
.stDeployButton {
    display: none !important;
}

/* Fondo oscuro general */
.stApp {
    background-color: #0f172a;
}

/* Ajuste de márgenes para que se pegue arriba */
.block-container {
    padding-top: 1rem !important;
    padding-bottom: 1rem !important;
}

/* HEADER EN LÍNEA PARA EVITAR EL APILADO EN CELULARES */
.custom-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #1e293b;
    padding: 8px 12px;
    border-radius: 12px;
    margin-bottom: 20px;
    border: 1px solid #334155;
    height: 70px;
}

/* Contenedor del Logo */
.logo-container {
    display: flex;
    align-items: center;
    height: 100%;
}

.logo-img {
    max-height: 55px;
    width: auto;
    object-fit: contain;
    border-radius: 6px;
}

.brand-title-fallback {
    color: #f59e0b;
    font-size: 18px;
    font-weight: bold;
    margin: 0;
}

/* Contenedor del Saldo */
.header-right {
    display: flex;
    align-items: center;
}

.balance-display {
    background-color: #0f172a;
    color: #4ade80; /* Verde brillante */
    padding: 8px 16px;
    border-radius: 8px;
    font-size: 16px;
    font-weight: bold;
    border: 1px solid #22c55e;
}

/* Contenedor de la Pantalla del Tragamonedas */
.slot-machine-container {
    background-color: #000000;
    padding: 30px;
    border-radius: 15px;
    border: 3px solid #f59e0b;
    text-align: center;
    margin-bottom: 20px;
    box-shadow: 0px 0px 15px rgba(245, 158, 11, 0.3);
}

.slot-emoji {
    font-size: 65px;
    padding: 0 15px;
    display: inline-block;
}

/* Estilo para los títulos */
h2, h3 {
    color: #f8fafc !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER OPTIMIZADO (LOGOTIPO + SALDO EN UNA FILA) ----------------
if logo_base64:
    # Si encontramos el logotipo físico lo mostramos perfectamente alineado
    header_html = f"""
    <div class="custom-header">
        <div class="logo-container">
            <img src="{logo_base64}" class="logo-img" alt="Fortuna MX Logo">
        </div>
        <div class="header-right">
            <div class="balance-display">${st.session_state.saldo:,.2f} MXN</div>
        </div>
    </div>
    """
else:
    # Fallback de texto si el archivo de imagen no se encuentra en el repositorio
    header_html = f"""
    <div class="custom-header">
        <div class="brand-title-fallback">🎰 FORTUNA MX</div>
        <div class="header-right">
            <div class="balance-display">${st.session_state.saldo:,.2f} MXN</div>
        </div>
    </div>
    """

st.markdown(header_html, unsafe_allow_html=True)

# Botones de interacción rápida con el saldo
col_dep, col_ret = st.columns(2)
with col_dep:
    if st.button("💳 Recargar Saldo (+ $500)", use_container_width=True):
        st.session_state.saldo += 500
        st.toast("¡Recarga exitosa de $500!", icon="💰")
        st.rerun()
with col_ret:
    if st.button("💸 Retirar ganancias", use_container_width=True):
        if st.session_state.saldo > 0:
            st.toast(f"Procesando retiro de ${st.session_state.saldo:,.2f}...", icon="🏧")
            st.session_state.saldo = 0.00
            st.rerun()
        else:
            st.error("No tienes fondos para retirar.")

st.markdown("---")

# ---------------- JUEGO: TRAGAMONEDAS (SLOTS) ----------------
st.markdown("## 🎰 SIGUE JUGANDO - SLOTS FORTUNA")

# Lista de símbolos disponibles
SIMBOLOS = ["🍒", "🍋", "🍉", "💎", "7️⃣", "👑"]

# Selección de apuesta
apuesta = st.number_input("Monto de tu apuesta ($):", min_value=10.0, max_value=1000.0, value=50.0, step=10.0)

# Pantalla de visualización de los carretes
slot_placeholder = st.empty()

# Estado estático inicial
slot_placeholder.markdown("""
<div class="slot-machine-container">
    <span class="slot-emoji">❓</span>
    <span class="slot-emoji">❓</span>
    <span class="slot-emoji">❓</span>
</div>
""", unsafe_allow_html=True)

# Botón para activar el casino
if st.button("¡JUGAR AHORA!", type="primary", use_container_width=True):
    if st.session_state.saldo < apuesta:
        st.error("❌ Saldo insuficiente. Por favor, recarga saldo arriba.")
    else:
        # Descontar saldo
        st.session_state.saldo -= apuesta
        
        # Efecto visual de giro rápido
        for _ in range(5):
            giro_temporal = [random.choice(SIMBOLOS) for _ in range(3)]
            slot_placeholder.markdown(f"""
            <div class="slot-machine-container">
                <span class="slot-emoji">{giro_temporal[0]}</span>
                <span class="slot-emoji">{giro_temporal[1]}</span>
                <span class="slot-emoji">{giro_temporal[2]}</span>
            </div>
            """, unsafe_allow_html=True)
            time.sleep(0.15)
            
        # Resultado final
        resultado = [random.choice(SIMBOLOS) for _ in range(3)]
        
        slot_placeholder.markdown(f"""
        <div class="slot-machine-container">
            <span class="slot-emoji">{resultado[0]}</span>
            <span class="slot-emoji">{resultado[1]}</span>
            <span class="slot-emoji">{resultado[2]}</span>
        </div>
        """, unsafe_allow_html=True)
        
        # Lógica de juego
        if resultado[0] == resultado[1] == resultado[2]:
            multiplicador = 10 if resultado[0] in ["7️⃣", "💎"] else 5
            premio = apuesta * multiplicador
            st.session_state.saldo += premio
            st.success(f"🎉 ¡JACKPOT! Ganaste ${premio:,.2f} MXN (x{multiplicador})")
            st.balloons()
            
        elif resultado[0] == resultado[1] or resultado[1] == resultado[2] or resultado[0] == resultado[2]:
            premio = apuesta * 1.5
            st.session_state.saldo += premio
            st.warning(f"✨ ¡2 iguales! Ganaste ${premio:,.2f} MXN")
            
        else:
            st.error(f"😢 Suerte para la próxima. Perdiste ${apuesta:,.2f} MXN")
            
        st.rerun()

# ---------------- SECCIÓN INFERIOR ----------------
st.markdown("## 🔥 WINPOT POPULAR")
col_game1, col_game2 = st.columns(2)
with col_game1:
    st.info("🃏 Próximamente: Ruleta de la Fortuna.")
with col_game2:
    st.info("🚀 Próximamente: Juego de Cohete multiplicador.")

```
