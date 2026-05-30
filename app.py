import streamlit as st
import random
import time

st.set_page_config(layout="wide", page_title="Fortuna MX - Casino")

# ---------------- ESTADO DE LA APP (PERSISTENCIA DE SALDO) ----------------
if "saldo" not in st.session_state:
    st.session_state.saldo = 5000.00

# ---------------- ESTILOS CSS PERSONALIZADOS ----------------
st.markdown("""
<style>
/* Fondo oscuro general */
.stApp {
    background-color: #0f172a;
}

/* Quitar espacios superiores de Streamlit */
.block-container {
    padding-top: 1rem !important;
    padding-bottom: 0rem;
}

/* HEADER EN LÍNEA EXCLUSIVO PARA MÓVILES Y WEB */
.custom-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #1e293b;
    padding: 10px 15px;
    border-radius: 10px;
    margin-bottom: 20px;
    border: 1px solid #334155;
}

.brand-title {
    color: #f59e0b; /* Color dorado */
    font-size: 20px;
    font-weight: bold;
    margin: 0;
    letter-spacing: 1px;
}

.header-right {
    display: flex;
    align-items: center;
    gap: 10px;
}

.balance-display {
    background-color: #0f172a;
    color: #4ade80; /* Verde brillante */
    padding: 6px 14px;
    border-radius: 6px;
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
    animation: bounce 0.5s infinite alternate;
}

/* Estilo para los títulos */
h2, h3 {
    color: #f8fafc !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER OPTIMIZADO (FIJO EN MÓVILES) ----------------
st.markdown(f"""
<div class="custom-header">
    <div class="brand-title">🎰 FORTUNA MX</div>
    <div class="header-right">
        <div class="balance-display">${st.session_state.saldo:,.2f} MXN</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Botones de interacción con el saldo
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

# Lista de símbolos disponibles en el casino
SIMBOLOS = ["🍒", "🍋", "🍉", "💎", "7️⃣", "👑"]

# Selección del monto de la apuesta
apuesta = st.number_input("Monto de tu apuesta ($):", min_value=10.0, max_value=1000.0, value=50.0, step=10.0)

# Contenedor visual del juego
slot_placeholder = st.empty()

# Estado inicial estático (antes de jugar)
slot_placeholder.markdown("""
<div class="slot-machine-container">
    <span class="slot-emoji">❓</span>
    <span class="slot-emoji">❓</span>
    <span class="slot-emoji">❓</span>
</div>
""", unsafe_allow_html=True)

# Botón principal para jugar
if st.button("¡JUGAR AHORA!", type="primary", use_container_width=True):
    if st.session_state.saldo < apuesta:
        st.error("❌ Saldo insuficiente. Por favor, recarga saldo arriba.")
    else:
        # 1. Descontar la apuesta inmediatamente
        st.session_state.saldo -= apuesta
        
        # 2. Efecto visual de giro (simulación)
        for _ in range(5):
            giro_temporal = [random.choice(SIMBOLOS) for _ in range(3)]
            slot_placeholder.markdown(f"""
            <div class="slot-machine-container">
                <span class="slot-emoji">{giro_temporal[0]}</span>
                <span class="slot-emoji">{giro_temporal[1]}</span>
                <span class="slot-emoji">{giro_temporal[2]}</span>
            </div>
            """, unsafe_allow_html=True)
            time.sleep(0.15) # Pausa rápida para dar sensación de movimiento
            
        # 3. Resultado definitivo
        resultado = [random.choice(SIMBOLOS) for _ in range(3)]
        
        # Mostrar el resultado final
        slot_placeholder.markdown(f"""
        <div class="slot-machine-container">
            <span class="slot-emoji">{resultado[0]}</span>
            <span class="slot-emoji">{resultado[1]}</span>
            <span class="slot-emoji">{resultado[2]}</span>
        </div>
        """, unsafe_allow_html=True)
        
        # 4. Lógica de Premios
        # Caso 1: Los 3 símbolos son iguales (Premio Mayor / Jackpot)
        if resultado[0] == resultado[1] == resultado[2]:
            multiplicador = 10 if resultado[0] == "7️⃣" or resultado[0] == "💎" else 5
            premio = apuesta * multiplicador
            st.session_state.saldo += premio
            st.success(f"🎉 ¡JACKPOT! Combinación perfecta. Ganaste ${premio:,.2f} MXN (x{multiplicador})")
            st.balloons()
            
        # Caso 2: 2 símbolos son iguales (Premio Menor)
        elif resultado[0] == resultado[1] or resultado[1] == resultado[2] or resultado[0] == resultado[2]:
            premio = apuesta * 1.5
            st.session_state.saldo += premio
            st.warning(f"✨ ¡Buen intento! 2 símbolos iguales. Recuperas tu apuesta y ganas ${premio:,.2f} MXN")
            
        # Caso 3: Todos diferentes (Pierde)
        else:
            st.error(f"😢 Suerte para la próxima. Perdiste tu apuesta de ${apuesta:,.2f} MXN")
            
        # Forzar recarga rápida de la interfaz para actualizar el saldo en la barra superior
        st.rerun()

# ---------------- SECCIÓN INFERIOR (CRAZY COMPONENT) ----------------
st.markdown("## 🔥 WINPOT POPULAR")
col_game1, col_game2 = st.columns(2)
with col_game1:
    st.info("🃏 Próximamente: Ruleta de la Fortuna en vivo.")
with col_game2:
    st.info("🚀 Próximamente: Juego Crash (Multiplicador de cohete).")
