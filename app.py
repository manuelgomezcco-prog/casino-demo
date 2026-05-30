import streamlit as st
import random
import time
import base64
import os

# Configuración de página optimizada para móviles
st.set_page_config(layout="wide", page_title="Fortuna MX - Casino Real", page_icon="🎰")

# ---------------- ESTADO DE LA APP (PERSISTENCIA DE DATOS) ----------------
if "saldo" not in st.session_state:
    st.session_state.saldo = 1000.00  # Saldo inicial de prueba

if "historial_transacciones" not in st.session_state:
    st.session_state.historial_transacciones = []

if "seccion_activa" not in st.session_state:
    st.session_state.seccion_activa = "slots"  # Secciones: slots, ruleta, cajero, soporte

# ---------------- FUNCIÓN DE CODIFICACIÓN PARA EL LOGOTIPO ----------------
def obtener_logo_base64():
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

# ---------------- ESTILOS CSS AVANZADOS (Casinos Premium) ----------------
st.markdown("""
<style>
/* --- OCULTAR DE MANERA ESTRICTA LA BARRA SUPERIOR DE GITHUB Y MENÚS DE STREAMLIT --- */
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
    background-color: #0b0f19;
}

/* Optimizar márgenes móviles */
.block-container {
    padding-top: 0.5rem !important;
    padding-bottom: 2rem !important;
}

/* HEADER RESPONSIVO (LOGO + SALDO EN UNA MISMA LÍNEA) */
.custom-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #161e2e;
    padding: 10px 15px;
    border-radius: 12px;
    margin-bottom: 15px;
    border: 1px solid #1f2937;
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
    background-color: #0b0f19;
    color: #10b981; /* Verde esmeralda */
    padding: 8px 16px;
    border-radius: 8px;
    font-size: 16px;
    font-weight: bold;
    border: 1px solid #059669;
    text-shadow: 0px 0px 5px rgba(16, 185, 129, 0.3);
}

/* BOTONES DE NAVEGACIÓN PRINCIPAL */
.nav-container {
    display: flex;
    gap: 8px;
    margin-bottom: 15px;
    overflow-x: auto;
    padding-bottom: 5px;
}

/* CONTENEDORES DEL JUEGO */
.slot-machine-display {
    background-color: #020617;
    padding: 35px 20px;
    border-radius: 16px;
    border: 3px solid #f59e0b;
    text-align: center;
    margin-bottom: 20px;
    box-shadow: 0px 0px 20px rgba(245, 158, 11, 0.2);
}

.slot-symbol {
    font-size: 70px;
    padding: 0 12px;
    display: inline-block;
}

/* DISEÑO DE CARTAS DE JUEGOS DE CASINO REALES */
.game-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 15px;
    margin-top: 15px;
}

.game-card {
    background-color: #161e2e;
    border: 1px solid #1f2937;
    border-radius: 12px;
    overflow: hidden;
    text-align: center;
    position: relative;
}

.game-img {
    width: 100%;
    height: 110px;
    object-fit: cover;
}

.game-title {
    color: #f8fafc;
    font-size: 13px;
    font-weight: bold;
    padding: 8px 5px;
    background-color: #161e2e;
    margin: 0;
}

.game-badge {
    position: absolute;
    top: 8px;
    right: 8px;
    background-color: #ef4444;
    color: white;
    font-size: 10px;
    padding: 2px 6px;
    border-radius: 4px;
    font-weight: bold;
}

/* Estilo general para títulos */
h1, h2, h3 {
    color: #f8fafc !important;
}

/* Tarjeta Cajero */
.cashier-card {
    background-color: #161e2e;
    border: 1px solid #1f2937;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 15px;
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

# ---------------- MENÚ DE NAVEGACIÓN SUPERIOR (TIPO APP) ----------------
col_nav1, col_nav2, col_nav3, col_nav4 = st.columns(4)
with col_nav1:
    if st.button("🍒 Tragamonedas", use_container_width=True, type="primary" if st.session_state.seccion_activa == "slots" else "secondary"):
        st.session_state.seccion_activa = "slots"
        st.rerun()
with col_nav2:
    if st.button("🎡 Ruleta Real", use_container_width=True, type="primary" if st.session_state.seccion_activa == "ruleta" else "secondary"):
        st.session_state.seccion_activa = "ruleta"
        st.rerun()
with col_nav3:
    if st.button("🏦 Cajero / Depósitos", use_container_width=True, type="primary" if st.session_state.seccion_activa == "cajero" else "secondary"):
        st.session_state.seccion_activa = "cajero"
        st.rerun()
with col_nav4:
    if st.button("💬 Proveedores / Soporte", use_container_width=True, type="primary" if st.session_state.seccion_activa == "soporte" else "secondary"):
        st.session_state.seccion_activa = "soporte"
        st.rerun()

st.markdown("---")

# ---------------- SECCIÓN 1: TRAGAMONEDAS ----------------
if st.session_state.seccion_activa == "slots":
    st.markdown("## 🎰 JUEGO DE TRAGAMONEDAS")
    
    SIMBOLOS_CASINO = ["🍒", "🍋", "🍉", "💎", "7️⃣", "👑"]
    apuesta_usuario = st.number_input("Monto de tu apuesta ($):", min_value=10.0, max_value=2000.0, value=50.0, step=10.0)
    
    carretes_placeholder = st.empty()
    carretes_placeholder.markdown("""
    <div class="slot-machine-display">
        <span class="slot-symbol">❓</span>
        <span class="slot-symbol">❓</span>
        <span class="slot-symbol">❓</span>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("¡GIRAR TRAGAMONEDAS!", type="primary", use_container_width=True):
        if st.session_state.saldo < apuesta_usuario:
            st.error("❌ Saldo insuficiente. Ve a la sección 'Cajero' para recargar fondos reales.")
        else:
            st.session_state.saldo -= apuesta_usuario
            for _ in range(6):
                giro_previo = [random.choice(SIMBOLOS_CASINO) for _ in range(3)]
                carretes_placeholder.markdown(f"""
                <div class="slot-machine-display">
                    <span class="slot-symbol">{giro_previo[0]}</span>
                    <span class="slot-symbol">{giro_previo[1]}</span>
                    <span class="slot-symbol">{giro_previo[2]}</span>
                </div>
                """, unsafe_allow_html=True)
                time.sleep(0.1)
                
            resultado_final = [random.choice(SIMBOLOS_CASINO) for _ in range(3)]
            carretes_placeholder.markdown(f"""
            <div class="slot-machine-display">
                <span class="slot-symbol">{resultado_final[0]}</span>
                <span class="slot-symbol">{resultado_final[1]}</span>
                <span class="slot-symbol">{resultado_final[2]}</span>
            </div>
            """, unsafe_allow_html=True)
            
            if resultado_final[0] == resultado_final[1] == resultado_final[2]:
                multiplicador = 12 if resultado_final[0] in ["7️⃣", "💎"] else 6
                premio = apuesta_usuario * multiplicador
                st.session_state.saldo += premio
                st.success(f"🎉 ¡JACKPOT! Ganaste ${premio:,.2f} MXN (x{multiplicador})")
                st.balloons()
            elif resultado_final[0] == resultado_final[1] or resultado_final[1] == resultado_final[2] or resultado_final[0] == resultado_final[2]:
                premio = apuesta_usuario * 1.5
                st.session_state.saldo += premio
                st.warning(f"✨ ¡Doble coincidencia! Ganaste ${premio:,.2f} MXN")
            else:
                st.error(f"😢 Suerte para la próxima. Perdiste tu apuesta de ${apuesta_usuario:,.2f} MXN")
            st.rerun()

# ---------------- SECCIÓN 2: RULETA EUROPEA INTERACTIVA (NUEVO JUEGO) ----------------
elif st.session_state.seccion_activa == "ruleta":
    st.markdown("## 🎡 RULETA EN VIVO INTERACTIVA")
    st.write("Realiza apuestas a números específicos (pago de 35 a 1) o selecciona por color (pago de 2 a 1).")
    
    col_r1, col_r2 = st.columns([1, 1])
    
    with col_r1:
        tipo_apuesta = st.radio("Tipo de apuesta:", ["Color (Rojo/Negro)", "Número Directo (0-36)"])
        apuesta_ruleta = st.number_input("Monto a apostar ($):", min_value=10.0, max_value=5000.0, value=100.0, step=50.0)
        
        if tipo_apuesta == "Color (Rojo/Negro)":
            seleccion_color = st.selectbox("Elige color:", ["Rojo 🔴", "Negro ⚫"])
        else:
            seleccion_numero = st.number_input("Elige número (0-36):", min_value=0, max_value=36, value=7, step=1)
            
    with col_r2:
        ruleta_animacion = st.empty()
        ruleta_animacion.markdown("""
        <div style="background-color: #020617; border: 3px solid #10b981; border-radius: 50%; width: 200px; height: 200px; margin: 0 auto; display: flex; align-items: center; justify-content: center; box-shadow: 0 0 15px rgba(16, 185, 129, 0.2);">
            <div style="font-size: 50px;">🎡</div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("¡GIRAR LA RULETA!", type="primary", use_container_width=True):
            if st.session_state.saldo < apuesta_ruleta:
                st.error("❌ Saldo insuficiente para realizar esta apuesta.")
            else:
                st.session_state.saldo -= apuesta_ruleta
                
                # Efecto visual de giros rápidos
                numeros_ruleta = list(range(37))
                rojos = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
                
                for i in range(12):
                    num_temp = random.choice(numeros_ruleta)
                    color_temp = "🔴 Rojo" if num_temp in rojos else ("🟢 Verde" if num_temp == 0 else "⚫ Negro")
                    ruleta_animacion.markdown(f"""
                    <div style="background-color: #020617; border: 3px solid #f59e0b; border-radius: 50%; width: 200px; height: 200px; margin: 0 auto; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                        <div style="font-size: 50px; animation: spin {0.1 + i*0.05}s linear infinite;">🎡</div>
                        <div style="color: white; font-weight: bold; margin-top: 10px;">{num_temp} ({color_temp})</div>
                    </div>
                    """, unsafe_allow_html=True)
                    time.sleep(0.15)
                
                # Resultado definitivo
                resultado_num = random.choice(numeros_ruleta)
                resultado_color = "Rojo" if resultado_num in rojos else ("Verde" if resultado_num == 0 else "Negro")
                resultado_color_emoji = "🔴" if resultado_color == "Rojo" else ("🟢" if resultado_color == "Verde" else "⚫")
                
                ruleta_animacion.markdown(f"""
                <div style="background-color: #020617; border: 3px solid #10b981; border-radius: 50%; width: 200px; height: 200px; margin: 0 auto; display: flex; flex-direction: column; align-items: center; justify-content: center; box-shadow: 0px 0px 20px rgba(16, 185, 129, 0.4);">
                    <div style="font-size: 60px;">🎯</div>
                    <div style="color: #f8fafc; font-size: 24px; font-weight: bold; margin-top: 5px;">{resultado_num}</div>
                    <div style="color: #cbd5e1; font-size: 14px;">{resultado_color_emoji} {resultado_color}</div>
                </div>
                """, unsafe_allow_html=True)
                
                # Lógica de cálculo de premios
                ganador = False
                pago_total = 0
                
                if tipo_apuesta == "Color (Rojo/Negro)":
                    apuesta_color_clean = "Rojo" if "Rojo" in seleccion_color else "Negro"
                    if resultado_color == apuesta_color_clean:
                        ganador = True
                        pago_total = apuesta_ruleta * 2
                else:
                    if resultado_num == seleccion_numero:
                        ganador = True
                        pago_total = apuesta_ruleta * 35
                
                if ganador:
                    st.session_state.saldo += pago_total
                    st.success(f"🎉 ¡Felicidades! Salió {resultado_num} ({resultado_color}). Has ganado ${pago_total:,.2f} MXN!")
                    st.balloons()
                else:
                    st.error(f"😢 Cayó el número {resultado_num} ({resultado_color}). Perdiste tu apuesta.")
                
                time.sleep(1.5)
                st.rerun()

# ---------------- SECCIÓN 3: CAJERO REAL (PASARELA DE PAGOS) ----------------
elif st.session_state.seccion_activa == "cajero":
    st.markdown("## 🏦 CAJERO CENTRAL - DEPOSITOS Y RETIROS")
    
    tab_deposito, tab_retiro, tab_historial = st.tabs(["📥 Realizar Depósito", "📤 Solicitar Retiro", "📋 Historial de Transacciones"])
    
    with tab_deposito:
        st.markdown('<div class="cashier-card">', unsafe_allow_html=True)
        st.subheader("Selecciona tu método de pago seguro")
        
        metodo = st.radio("Método de pago:", ["SPEI (Transferencia electrónica instantánea)", "OXXO Pay (Efectivo)", "Tarjeta de Crédito / Débito"])
        monto_deposito = st.number_input("Monto a depositar (MXN):", min_value=100.0, max_value=50000.0, value=500.0, step=100.0)
        
        st.info("💡 Todos nuestros depósitos se procesan a través de encriptación SSL de extremo a extremo de forma segura.")
        
        if st.button("GENERAR SOLICITUD DE PAGO", type="primary", use_container_width=True):
            st.warning("⚠️ Generando orden de pago segura...")
            time.sleep(1.5)
            
            # Flujos simulados listos para integrarse con SDK real de Conekta / Stripe
            if "SPEI" in metodo:
                st.success("📝 ORDEN DE PAGO SPEI GENERADA CON ÉXITO")
                st.markdown(f"""
                **Instrucciones para transferir:**
                1. Abre la aplicación de tu banco.
                2. Realiza una transferencia CLABE por **${monto_deposito:,.2f} MXN**.
                3. **Banco Destinatario:** Sistema de Transferencias y Pagos (STP) / Conekta
                4. **CLABE Interbancaria:** `6461 8012 3456 7890 12`
                5. **Beneficiario:** FORTUNA MX INTERACTIVE
                *Tu saldo se actualizará de manera automática al ser recibida la transferencia.*
                """)
            elif "OXXO" in metodo:
                codigo_barras = random.randint(10000000000000, 99999999999999)
                st.success("🏪 CÓDIGO DE BARRAS OXXO PAY")
                st.markdown(f"""
                **Instrucciones de pago en OXXO:**
                1. Acude a cualquier tienda OXXO de la República Mexicana.
                2. Dicta el siguiente número de referencia de pago al cajero:
                   ### **{codigo_barras}**
                3. Realiza el pago de **${monto_deposito:,.2f} MXN** en efectivo (+ comisión de tienda).
                """)
            else:
                # Flujo de Tarjeta (Simulado)
                st.success("💳 ENLACE DE PAGO CON TARJETA DE CRÉDITO/DÉBITO")
                st.markdown(f"""
                Hemos habilitado de forma segura tu pasarela para la tarjeta.
                * [Pagar de forma segura en stripe.com/fortunamx](https://stripe.com) (Enlace de pago de demostración)
                """)
                
            # Agregamos depósito ficticio inmediato al saldo para demostración
            st.session_state.saldo += monto_deposito
            st.session_state.historial_transacciones.append({
                "fecha": time.strftime("%Y-%m-%d %H:%M:%S"),
                "tipo": "Depósito",
                "monto": monto_deposito,
                "metodo": metodo,
                "estado": "Completado (Demo)"
            })
            st.toast(f"Se abonaron ${monto_deposito:,.2f} MXN a tu cuenta.", icon="✅")
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        
    with tab_retiro:
        st.markdown('<div class="cashier-card">', unsafe_allow_html=True)
        st.subheader("Retira tus fondos directamente a tu cuenta de banco")
        
        monto_retiro = st.number_input("Monto a retirar (MXN):", min_value=100.0, max_value=st.session_state.saldo, value=min(500.0, st.session_state.saldo), step=100.0)
        banco_destino = st.text_input("Banco Receptor:", placeholder="Ej. BBVA, Santander, Banamex")
        clabe_retiro = st.text_input("CLABE Interbancaria (18 dígitos):", max_chars=18, placeholder="012345678901234567")
        titular_cuenta = st.text_input("Nombre completo del titular de la cuenta:")
        
        if st.button("CONFIRMAR RETIRO DE FONDOS", type="primary", use_container_width=True):
            if len(clabe_retiro) != 18 or not clabe_retiro.isdigit():
                st.error("❌ La CLABE interbancaria debe tener exactamente 18 dígitos numéricos.")
            elif not titular_cuenta or not banco_destino:
                st.error("❌ Por favor completa todos los datos para procesar la transferencia de retiro.")
            else:
                st.session_state.saldo -= monto_retiro
                st.session_state.historial_transacciones.append({
                    "fecha": time.strftime("%Y-%m-%d %H:%M:%S"),
                    "tipo": "Retiro",
                    "monto": monto_retiro,
                    "metodo": f"SPEI a {banco_destino}",
                    "estado": "Pendiente de Procesamiento"
                })
                st.success("✅ SOLICITUD DE RETIRO ENVIADA CON ÉXITO")
                st.write(f"Tu pago de **${monto_retiro:,.2f} MXN** ha sido enviado al departamento de finanzas. El tiempo de procesamiento para el SPEI de retiro es de 1 a 24 horas hábiles.")
                time.sleep(1)
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        
    with tab_historial:
        st.markdown('<div class="cashier-card">', unsafe_allow_html=True)
        st.subheader("Últimas transacciones financieras")
        if len(st.session_state.historial_transacciones) == 0:
            st.info("No has realizado transacciones financieras recientes.")
        else:
            for t in reversed(st.session_state.historial_transacciones):
                st.markdown(f"""
                **{t['fecha']}** | **{t['tipo']}** | **Monto:** ${t['monto']:,.2f} | **Vía:** {t['metodo']} | *Estatus:* {t['estado']}
                ---
                """)
        st.markdown('</div>', unsafe_allow_html=True)

# ---------------- SECCIÓN 4: PROVEEDORES / SOPORTE ----------------
elif st.session_state.seccion_activa == "soporte":
    st.markdown("## 💬 SECTOR DE PROVEEDORES Y SOPORTE")
    st.write("¿Tienes dudas sobre los juegos de casino o quieres agregar nuevos sistemas de crédito de nuestros proveedores?")
    
    with st.form("form_proveedor_casino"):
        nombre = st.text_input("Nombre del Agente / Proveedor:")
        correo = st.text_input("Email de Contacto:")
        mensaje = st.text_area("Descríbenos tu propuesta o reporte sobre el casino:")
        enviar = st.form_submit_button("ENVIAR FORMULARIO DIRECTO")
        
        if enviar:
            if nombre and correo and mensaje:
                st.success("📬 Mensaje enviado con éxito a nuestro servidor. El área comercial de Fortuna MX se pondrá en contacto contigo.")
            else:
                st.error("Por favor completa los campos antes de enviar.")

st.markdown("---")

# ---------------- CAROUSEL VISUAL DE JUEGOS DISPONIBLES ----------------
st.markdown("## 🔥 JUEGOS RECOMENDADOS EN FORTUNA MX")
st.markdown("""
<div class="game-grid">
    <div class="game-card">
        <span class="game-badge">EN VIVO</span>
        <img src="https://images.unsplash.com/photo-1606167668584-78701c57f13d?auto=format&fit=crop&w=500&q=80" class="game-img" alt="Ruleta">
        <p class="game-title">RULETA EUROPEA REAL</p>
    </div>
    <div class="game-card">
        <span class="game-badge" style="background-color: #3b82f6;">PROXIMAMENTE</span>
        <img src="https://images.unsplash.com/photo-1518895949257-7621c3c786d7?auto=format&fit=crop&w=500&q=80" class="game-img" alt="Blackjack">
        <p class="game-title">BLACKJACK DECK</p>
    </div>
    <div class="game-card">
        <span class="game-badge" style="background-color: #10b981;">NUEVO</span>
        <img src="https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=500&q=80" class="game-img" alt="Crash">
        <p class="game-title">MULTIPLIER CRASH</p>
    </div>
    <div class="game-card">
        <span class="game-badge" style="background-color: #3b82f6;">PROXIMAMENTE</span>
        <img src="https://images.unsplash.com/photo-1541252260730-0412e8e2108e?auto=format&fit=crop&w=500&q=80" class="game-img" alt="Póker">
        <p class="game-title">POKER ROOM</p>
    </div>
</div>
""", unsafe_allow_html=True)
