import streamlit as st
import random
import time
import base64
import os

# Configuración de página
st.set_page_config(layout="wide", page_title="Fortuna MX")

# ---------------- ESTADO DE LA APP ----------------
if "saldo" not in st.session_state:
    st.session_state.saldo = 5000.00

# ---------------- FUNCIÓN DE CODIFICACIÓN PARA EL LOGOTIPO ----------------
def obtener_logo_base64():
    # Buscamos el archivo de imagen del logo en el directorio
    nombres_archivo = ["Logo.jpg", "logo.jpg", "Logo.png", "logo.png"]
    for nombre in nombres_archivo:
        if os.path.exists(nombre):
            try:
                with open(nombre, "rb") as f:
                    data = f.read()
                    encoded = base64.b64encode(data).decode()
                    ext = nombre.split(".")[-1].lower()
                    mime = "jpeg" if ext == "jpg" else ext
                    return f"data:image/{mime};base64,{encoded}"
            except Exception:
                pass
    return None

logo_url = obtener_logo_base64()

# ---------------- ESTILOS CSS AVANZADOS ----------------
st.markdown("""
<style>
/* --- OCULTAR DE MANERA ESTRICTA LA BARRA SUPERIOR DE GITHUB Y MENÚS --- */
header[data-testid="stHeader"] {
    display: none !important;
}
[data-testid="stHeader"] {
    display: none !important;
}
[data-testid="stDecoration"] {
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

/* Fondo oscuro de casino premium */
.stApp {
    background-color: #0f172a;
}

/* Optimizar márgenes móviles */
.block-container {
    padding-top: 0.5rem !important;
    padding-bottom: 1rem !important;
}

/* HEADER RESPONSIVO (LOGO + SALDO EN UNA MISMA LÍNEA) */
.custom-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #1e293b;
    padding: 10px 15px;
    border-radius: 12px;
    margin-bottom: 20px;
    border: 1px solid #334155;
    height: 75px;
}

.logo-box {
    display: flex;
    align-items: center;
    height: 100%;
}

.logo-image-styled {
    max-height: 55px;
    width: auto;
    object-fit: contain;
    border-radius: 6px;
}

.fallback-title {
    color: #f59e0b;
    font-size: 20px;
    font-weight: bold;
    margin: 0;
}

.balance-box {
    background-color: #0f172a;
    color: #4ade80; /* Verde brillante de dinero */
    padding: 8px 16px;
    border-radius: 8px;
    font-size: 16px;
    font-weight: bold;
    border: 1px solid #22c55e;
    text-shadow: 0px 0px 5px rgba(34, 197, 94, 0.2);
}

/* CONTENEDOR NEGRO DEL TRAGAMONEDAS */
.slot-machine-display {
    background-color: #000000;
    padding: 35px 20px;
    border-radius: 16px;
    border: 3px solid #f59e0b;
    text-align: center;
    margin-bottom: 20px;
    box-shadow: 0px 0px 20px rgba(245, 158, 11, 0.25);
}

.slot-symbol {
    font-size: 70px;
    padding: 0 12px;
    display: inline-block;
}

/* Estilo general para textos */
h2, h3 {
    color: #f8fafc !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------- RENDERIZACIÓN DEL HEADER EN LÍNEA ----------------
if logo_url:
    header_markup = f"""
    <div class="custom-header">
        <div class="logo-box">
            <img src="{logo_url}" class="logo-image-styled" alt="Fortuna MX">
        </div>
        <div>
            <div class="balance-box">${st.session_state.saldo:,.2f} MXN</div>
        </div>
    </div>
    """
else:
    header_markup = f"""
    <div class="custom-header">
        <div class="fallback-title">🎰 FORTUNA MX</div>
        <div>
            <div class="balance-box">${st.session_state.saldo:,.2f} MXN</div>
        </div>
    </div>
    """

st.markdown(header_markup, unsafe_allow_html=True)

# ---------------- BOTONES DE CONTROL DE SALDO ----------------
col_recargar, col_retirar = st.columns(2)
with col_recargar:
    if st.button("💳 Recargar Saldo (+ $500)", use_container_width=True):
        st.session_state.saldo += 500
        st.toast("¡Se han agregado $500.00 a tu saldo!", icon="💰")
        st.rerun()

with col_retirar:
    if st.button("💸 Retirar ganancias", use_container_width=True):
        if st.session_state.saldo > 0:
            st.toast(f"Retiro de ${st.session_state.saldo:,.2f} en proceso...", icon="🏦")
            st.session_state.saldo = 0.00
            st.rerun()
        else:
            st.error("No tienes saldo suficiente para retirar.")

st.markdown("---")

# ---------------- JUEGO TRAGAMONEDAS ----------------
st.markdown("## 🎰 SIGUE JUGANDO - SLOTS FORTUNA")

SIMBOLOS_CASINO = ["🍒", "🍋", "🍉", "💎", "7️⃣", "👑"]

# Ajuste de Apuesta
apuesta_usuario = st.number_input("Monto de tu apuesta ($):", min_value=10.0, max_value=2000.0, value=50.0, step=10.0)

# Espacio dinámico de la pantalla del tragamonedas
carretes_placeholder = st.empty()

# Estado estático inicial (El cuadro negro con signos de interrogación)
carretes_placeholder.markdown("""
<div class="slot-machine-display">
    <span class="slot-symbol">❓</span>
    <span class="slot-symbol">❓</span>
    <span class="slot-symbol">❓</span>
</div>
""", unsafe_allow_html=True)

# Botón para jugar
if st.button("¡JUGAR AHORA!", type="primary", use_container_width=True):
    if st.session_state.saldo < apuesta_usuario:
        st.error("❌ Saldo insuficiente. Realiza una recarga para continuar jugando.")
    else:
        # Descontar saldo inmediatamente
        st.session_state.saldo -= apuesta_usuario
        
        # Efecto de giro rápido (Animación)
        for _ in range(6):
            giro_previo = [random.choice(SIMBOLOS_CASINO) for _ in range(3)]
            carretes_placeholder.markdown(f"""
            <div class="slot-machine-display">
                <span class="slot-symbol">{giro_previo[0]}</span>
                <span class="slot-symbol">{giro_previo[1]}</span>
                <span class="slot-symbol">{giro_previo[2]}</span>
            </div>
            """, unsafe_allow_html=True)
            time.sleep(0.12)
            
        # Generar resultado final de forma aleatoria
        resultado_final = [random.choice(SIMBOLOS_CASINO) for _ in range(3)]
        
        # Renderizar resultado definitivo
        carretes_placeholder.markdown(f"""
        <div class="slot-machine-display">
            <span class="slot-symbol">{resultado_final[0]}</span>
            <span class="slot-symbol">{resultado_final[1]}</span>
            <span class="slot-symbol">{resultado_final[2]}</span>
        </div>
        """, unsafe_allow_html=True)
        
        # Lógica de premios
        # 3 Símbolos iguales
        if resultado_final[0] == resultado_final[1] == resultado_final[2]:
            multiplicador = 12 if resultado_final[0] in ["7️⃣", "💎"] else 6
            premio_obtenido = apuesta_usuario * multiplicador
            st.session_state.saldo += premio_obtenido
            st.success(f"🎉 ¡Felicidades! Lograste una línea de 3. Ganaste ${premio_obtenido:,.2f} MXN (x{multiplicador})")
            st.balloons()
        
        # 2 Símbolos iguales
        elif resultado_final[0] == resultado_final[1] or resultado_final[1] == resultado_final[2] or resultado_final[0] == resultado_final[2]:
            premio_obtenido = apuesta_usuario * 1.5
            st.session_state.saldo += premio_obtenido
            st.warning(f"✨ ¡Casi! 2 símbolos coinciden. Obtienes ${premio_obtenido:,.2f} MXN")
            
        # Sin coincidencias
        else:
            st.error(f"😢 Suerte para la próxima. Perdiste tu apuesta de ${apuesta_usuario:,.2f} MXN")
            
        # Recargar para actualizar el saldo en el Header inmediatamente
        st.rerun()

# ---------------- PIE DE PÁGINA ----------------
st.markdown("## 🔥 WINPOT POPULAR")
col_info1, col_info2 = st.columns(2)
with col_info1:
    st.info("🃏 Próximamente: Ruleta de la Fortuna y mesas en vivo.")
with col_info2:
    st.info("🚀 Próximamente: Crash game (Multiplicador de cohete).")
