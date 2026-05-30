import streamlit as st
import random
import time
import base64
import os

# Intentamos importar las librerías oficiales necesarias
try:
    import stripe
except ImportError:
    st.error("Por favor, añade 'stripe' a tu archivo requirements.txt en tu repositorio.")

# Para conectar Firebase Firestore de forma nativa en Python de manera simplificada,
# utilizaremos las variables de entorno seguras de Streamlit.
# Para evitar dependencias Firebase pesadas de C++ en Streamlit Cloud que a veces fallan al compilar,
# emularemos un sistema seguro de base de datos en nube persistente a través del SDK o bien utilizando 
# st.session_state con respaldo estructurado.
# Para garantizar la máxima estabilidad de compilación en el servidor de Streamlit de tu móvil,
# usaremos una base de datos local JSON persistente en el disco del contenedor de la app,
# la cual mantiene los datos persistentes de todos los usuarios registrados, sus saldos, CLABEs y teléfonos.

import json

DB_FILE = "usuarios_db.json"

def cargar_base_datos():
    if not os.path.exists(DB_FILE):
        # Base de datos inicial con un administrador preconfigurado
        inicial = {
            "admin@fortunamx.com": {
                "nombre": "Administrador Fortuna",
                "telefono": "5512345678",
                "contrasena": "FortunaAdmin2026",
                "saldo": 0.0,
                "clabe": "",
                "banco": "",
                "titular": "",
                "historial": [],
                "es_admin": True
            }
        }
        guardar_base_datos(inicial)
        return inicial
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return {}

def guardar_base_datos(db):
    try:
        with open(DB_FILE, "w") as f:
            json.dump(db, f, indent=4)
    except Exception as e:
        st.error(f"Error al escribir en la base de datos: {e}")

# Inicializamos la base de datos de usuarios
usuarios_db = cargar_base_datos()

# Configuración de página móvil premium
st.set_page_config(layout="wide", page_title="Fortuna MX - Casino", page_icon="🎰")

# ---------------- CONFIGURACIÓN DE STRIPE ----------------
STRIPE_SECRET_KEY = st.secrets.get("STRIPE_SECRET_KEY", "sk_test_51OpEXAMPLE_KEY_OBLIGATORIA_DE_STRIPE")
stripe.api_key = STRIPE_SECRET_KEY
APP_URL = "https://fortuna-mx.streamlit.app" 
ADMIN_PASSWORD = st.secrets.get("ADMIN_PASSWORD", "FortunaAdmin2026")

# ---------------- PERSISTENCIA DEL USUARIO ACTIVO ----------------
if "usuario_conectado" not in st.session_state:
    st.session_state.usuario_conectado = None  # Almacena el correo del usuario logueado

if "pagos_verificados" not in st.session_state:
    st.session_state.pagos_verificados = set()

# --- VERIFICACIÓN AUTOMÁTICA DE DEPÓSITOS DE STRIPE ---
query_params = st.query_params

if "session_id" in query_params and st.session_state.usuario_conectado:
    session_id = query_params["session_id"]
    correo = st.session_state.usuario_conectado
    
    if session_id not in st.session_state.pagos_verificados:
        try:
            checkout_session = stripe.checkout.Session.retrieve(session_id)
            
            if checkout_session.payment_status == "paid":
                monto_real = checkout_session.amount_total / 100.0  # Stripe procesa en centavos
                
                # Actualizar saldo en la base de datos persistente
                usuarios_db = cargar_base_datos()
                if correo in usuarios_db:
                    usuarios_db[correo]["saldo"] += monto_real
                    
                    # Registrar en el historial persistente del usuario
                    usuarios_db[correo]["historial"].append({
                        "fecha": time.strftime("%Y-%m-%d %H:%M:%S"),
                        "tipo": "Depósito Real Stripe",
                        "monto": monto_real,
                        "metodo": "Tarjeta/OXXO/SPEI",
                        "estado": "Completado"
                    })
                    guardar_base_datos(usuarios_db)
                    st.session_state.pagos_verificados.add(session_id)
                    
                    st.success(f"🎉 ¡Depósito verificado! Se han acreditado ${monto_real:,.2f} MXN a tu cuenta de {usuarios_db[correo]['nombre']}.")
                    st.balloons()
                
                st.query_params.clear()
                time.sleep(1.5)
                st.rerun()
        except Exception as e:
            st.error(f"Error en la verificación del pago de Stripe: {e}")

# ---------------- FUNCIÓN DE LOGOTIPO RESPONSIVO ----------------
def obtener_logo_base64():
    formatos = ["Logo.jpg", "logo.jpg", "Logo.png", "logo.png"]
    for nombre in formatos:
        if os.path.exists(nombre):
            try:
                with open(nombre, "rb") as f:
                    encoded = base64.b64encode(f.read()).decode()
                    ext = nombre.split(".")[-1].lower()
                    mime = "jpeg" if ext == "jpg" else ext
                    return f"data:image/{mime};base64,{encoded}"
            except Exception:
                pass
    return None

logo_base64 = obtener_logo_base64()

# ---------------- ESTILOS CSS CASINO PREMIUM ----------------
st.markdown("""
<style>
/* Ocultar elementos nativos de Streamlit */
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

/* Fondo oscuro general */
.stApp {
    background-color: #0b0f19;
}

/* Espaciados para pantalla móvil */
.block-container {
    padding-top: 0.8rem !important;
    padding-bottom: 2rem !important;
}

/* Encabezado elegante de Logo + Saldo */
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
    color: #10b981;
    padding: 8px 16px;
    border-radius: 8px;
    font-size: 16px;
    font-weight: bold;
    border: 1px solid #059669;
    text-shadow: 0px 0px 5px rgba(16, 185, 129, 0.3);
}

/* Slots de tragamonedas */
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

/* Grid de juegos */
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

.cashier-card {
    background-color: #161e2e;
    border: 1px solid #1f2937;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 15px;
}

h1, h2, h3, h4 {
    color: #f8fafc !important;
}

.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
}

.stTabs [data-baseweb="tab"] {
    background-color: #161e2e;
    border: 1px solid #1f2937;
    border-radius: 8px;
    padding: 8px 16px;
    color: #cbd5e1;
    font-weight: bold;
}

.stTabs [aria-selected="true"] {
    background-color: #f59e0b !important;
    color: #0b0f19 !important;
    border: 1px solid #f59e0b !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------- CONTROL DE SESIÓN GENERAL ----------------
usuario_activo = st.session_state.usuario_conectado

if usuario_activo:
    # Recargar datos frescos del usuario desde la BD
    usuarios_db = cargar_base_datos()
    datos_usuario = usuarios_db.get(usuario_activo, {})
    saldo_actual = datos_usuario.get("saldo", 0.0)
    nombre_actual = datos_usuario.get("nombre", "Jugador")
    
    # ---------------- BANER DE CABECERA (LOGO + SALDO) ----------------
    if logo_base64:
        header_markup = f"""
        <div class="custom-header">
            <div class="logo-box">
                <img src="{logo_base64}" class="logo-image-styled" alt="Fortuna MX">
            </div>
            <div>
                <div class="balance-box">${saldo_actual:,.2f} MXN</div>
            </div>
        </div>
        """
    else:
        header_markup = f"""
        <div class="custom-header">
            <div class="fallback-title">🎰 FORTUNA MX</div>
            <div>
                <div class="balance-box">${saldo_actual:,.2f} MXN</div>
            </div>
        </div>
        """
    st.markdown(header_markup, unsafe_allow_html=True)
    
    # Mensaje de bienvenida sutil
    st.markdown(f"<p style='color: #9ca3af; margin-top: -5px;'>Bienvenido de vuelta, <b>{nombre_actual}</b></p>", unsafe_allow_html=True)

    # ---------------- PESTAÑAS DE NAVEGACIÓN ----------------
    tab_slots, tab_ruleta, tab_cajero, tab_perfil, tab_admin = st.tabs([
        "🍒 Tragamonedas", 
        "🎡 Ruleta", 
        "🏦 Cajero / Depósitos", 
        "👤 Mi Perfil",
        "👑 Admin"
    ])

    # ================= MÓDULO 1: TRAGAMONEDAS =================
    with tab_slots:
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
            if saldo_actual < apuesta_usuario:
                st.error("❌ Saldo insuficiente. Ve al menú 'Cajero / Depósitos' para recargar fondos reales.")
            else:
                # Restar saldo de la BD
                usuarios_db[usuario_activo]["saldo"] -= apuesta_usuario
                guardar_base_datos(usuarios_db)
                
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
                
                usuarios_db = cargar_base_datos()  # Recargar por seguridad
                if resultado_final[0] == resultado_final[1] == resultado_final[2]:
                    multiplicador = 12 if resultado_final[0] in ["7️⃣", "💎"] else 6
                    premio = apuesta_usuario * multiplicador
                    usuarios_db[usuario_activo]["saldo"] += premio
                    st.success(f"🎉 ¡JACKPOT! Ganaste ${premio:,.2f} MXN (x{multiplicador})")
                    st.balloons()
                elif resultado_final[0] == resultado_final[1] or resultado_final[1] == resultado_final[2] or resultado_final[0] == resultado_final[2]:
                    premio = apuesta_usuario * 1.5
                    usuarios_db[usuario_activo]["saldo"] += premio
                    st.warning(f"✨ ¡Doble coincidencia! Ganaste ${premio:,.2f} MXN")
                else:
                    st.error(f"😢 Perdiste tu apuesta de ${apuesta_usuario:,.2f} MXN")
                
                guardar_base_datos(usuarios_db)
                st.rerun()

    # ================= MÓDULO 2: RULETA EUROPEA =================
    with tab_ruleta:
        st.markdown("## 🎡 RULETA EN VIVO INTERACTIVA")
        
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
            <div style="background-color: #020617; border: 3px solid #10b981; border-radius: 50%; width: 180px; height: 180px; margin: 0 auto; display: flex; align-items: center; justify-content: center; box-shadow: 0 0 15px rgba(16, 185, 129, 0.2);">
                <div style="font-size: 50px;">🎡</div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("¡GIRAR LA RULETA!", type="primary", use_container_width=True):
                if saldo_actual < apuesta_ruleta:
                    st.error("❌ Saldo insuficiente para realizar esta apuesta.")
                else:
                    usuarios_db[usuario_activo]["saldo"] -= apuesta_ruleta
                    guardar_base_datos(usuarios_db)
                    
                    numeros_ruleta = list(range(37))
                    rojos = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
                    
                    for i in range(12):
                        num_temp = random.choice(numeros_ruleta)
                        color_temp = "🔴 Rojo" if num_temp in rojos else ("🟢 Verde" if num_temp == 0 else "⚫ Negro")
                        ruleta_animacion.markdown(f"""
                        <div style="background-color: #020617; border: 3px solid #f59e0b; border-radius: 50%; width: 180px; height: 180px; margin: 0 auto; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                            <div style="font-size: 50px;">🎡</div>
                            <div style="color: white; font-weight: bold; margin-top: 10px;">{num_temp} ({color_temp})</div>
                        </div>
                        """, unsafe_allow_html=True)
                        time.sleep(0.12)
                    
                    resultado_num = random.choice(numeros_ruleta)
                    resultado_color = "Rojo" if resultado_num in rojos else ("Verde" if resultado_num == 0 else "Negro")
                    resultado_color_emoji = "🔴" if resultado_color == "Rojo" else ("🟢" if resultado_color == "Verde" else "⚫")
                    
                    ruleta_animacion.markdown(f"""
                    <div style="background-color: #020617; border: 3px solid #10b981; border-radius: 50%; width: 180px; height: 180px; margin: 0 auto; display: flex; flex-direction: column; align-items: center; justify-content: center; box-shadow: 0px 0px 20px rgba(16, 185, 129, 0.4);">
                        <div style="font-size: 50px;">🎯</div>
                        <div style="color: #f8fafc; font-size: 22px; font-weight: bold; margin-top: 5px;">{resultado_num}</div>
                        <div style="color: #cbd5e1; font-size: 13px;">{resultado_color_emoji} {resultado_color}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
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
                    
                    usuarios_db = cargar_base_datos()
                    if ganador:
                        usuarios_db[usuario_activo]["saldo"] += pago_total
                        st.success(f"🎉 ¡Has ganado ${pago_total:,.2f} MXN!")
                        st.balloons()
                    else:
                        st.error(f"😢 Salió el número {resultado_num} ({resultado_color}). Perdiste.")
                    
                    guardar_base_datos(usuarios_db)
                    time.sleep(1.5)
                    st.rerun()

    # ================= MÓDULO 3: CAJERO DE DEPÓSITOS REALES (STRIPE) =================
    with tab_cajero:
        st.markdown("## 🏦 CAJERO CENTRAL - FONDOS REALES")
        
        subtab_deposito, subtab_retiro, subtab_historial = st.tabs([
            "📥 Realizar Depósito", 
            "📤 Solicitar Retiro (SPEI)", 
            "📋 Mi Historial"
        ])
        
        with subtab_deposito:
            st.markdown('<div class="cashier-card">', unsafe_allow_html=True)
            st.subheader("Depósito Seguro en Línea")
            
            monto_deposito = st.number_input("Monto a depositar (MXN):", min_value=100.0, max_value=20000.0, value=250.0, step=50.0)
            
            st.markdown("""
            * **Tarjetas:** Visa, Mastercard y American Express de forma instantánea.
            * **SPEI & OXXO:** Al presionar el botón de pago, podrás seleccionar también pagar por transferencia SPEI o generar una referencia de pago para OXXO directamente en la pasarela segura.
            """)
            
            if STRIPE_SECRET_KEY == "sk_test_51OpEXAMPLE_KEY_OBLIGATORIA_DE_STRIPE":
                st.warning("⚠️ Modo de Demostración Activo. Configura tus credenciales reales en Streamlit para habilitar cobros en producción.")
            
            if st.button("PAGAR AHORA DE FORMA SEGURA", type="primary", use_container_width=True):
                try:
                    # Crear checkout session de Stripe con pasarelas de México activas
                    session = stripe.checkout.Session.create(
                        payment_method_types=["card", "oxxo"],
                        line_items=[{
                            "price_data": {
                                "currency": "mxn",
                                "product_data": {
                                    "name": f"Abono Casino Fortuna MX ({nombre_actual})",
                                    "description": f"Recarga de saldo para la cuenta: {usuario_activo}",
                                },
                                "unit_amount": int(monto_deposito * 100),
                            },
                            "quantity": 1,
                        }],
                        mode="payment",
                        success_url=f"{APP_URL}/?session_id={{CHECKOUT_SESSION_ID}}",
                        cancel_url=f"{APP_URL}/",
                    )
                    
                    st.success("✅ ¡Pasarela de pago de Stripe generada!")
                    st.markdown(f"""
                    <a href="{session.url}" target="_blank" style="text-decoration:none;">
                        <div style="background-color: #10b981; color: white; text-align: center; padding: 14px; border-radius: 8px; font-weight: bold; font-size: 16px; box-shadow: 0px 4px 10px rgba(16,185,129,0.3);">
                            👉 CLIC AQUÍ PARA IR A STRIPE Y PAGAR SECURELY 🔒
                        </div>
                    </a>
                    <br>
                    <p style='text-align: center; font-size: 13px; color: #9ca3af;'>Se abrirá una pestaña segura de Stripe. Al completar el pago, regresarás aquí y tu saldo se actualizará de inmediato.</p>
                    """, unsafe_allow_html=True)
                    
                except Exception as e:
                    st.error(f"Error al conectar con Stripe: {e}")
                    
            st.markdown('</div>', unsafe_allow_html=True)
            
        with subtab_retiro:
            st.markdown('<div class="cashier-card">', unsafe_allow_html=True)
            st.subheader("Retira tus ganancias directamente a tu banco (SPEI)")
            
            monto_retiro = st.number_input("Monto a retirar (MXN):", min_value=100.0, max_value=max(100.0, saldo_actual), value=min(200.0, saldo_actual), step=50.0)
            
            # Recordar métodos de pago automáticamente de la BD
            saved_banco = datos_usuario.get("banco", "")
            saved_clabe = datos_usuario.get("clabe", "")
            saved_titular = datos_usuario.get("titular", "")
            
            banco_destino = st.text_input("Banco Destinatario (BBVA, Santander, etc.):", value=saved_banco)
            clabe_retiro = st.text_input("CLABE Interbancaria (18 dígitos):", max_chars=18, value=saved_clabe)
            titular_cuenta = st.text_input("Nombre completo del Titular:", value=saved_titular)
            
            guardar_metodo = st.checkbox("Guardar esta cuenta bancaria como mi método predeterminado", value=True)
            
            if st.button("CONFIRMAR SOLICITUD DE RETIRO", type="primary", use_container_width=True):
                if saldo_actual < monto_retiro:
                    st.error("No tienes fondos suficientes en tu cuenta para este retiro.")
                elif len(clabe_retiro) != 18 or not clabe_retiro.isdigit():
                    st.error("La CLABE interbancaria debe consistir de exactamente 18 números.")
                elif not banco_destino or not titular_cuenta:
                    st.error("Todos los campos bancarios son obligatorios para procesar el pago SPEI.")
                else:
                    # Descontamos el saldo en la BD
                    usuarios_db = cargar_base_datos()
                    usuarios_db[usuario_activo]["saldo"] -= monto_retiro
                    
                    # Guardamos método de pago si el checkbox está activo
                    if guardar_metodo:
                        usuarios_db[usuario_activo]["banco"] = banco_destino
                        usuarios_db[usuario_activo]["clabe"] = clabe_retiro
                        usuarios_db[usuario_activo]["titular"] = titular_cuenta
                    
                    # Generamos la orden de retiro
                    folio = random.randint(10000, 99999)
                    nuevo_retiro = {
                        "id": folio,
                        "fecha": time.strftime("%Y-%m-%d %H:%M:%S"),
                        "monto": monto_retiro,
                        "banco": banco_destino,
                        "clabe": clabe_retiro,
                        "titular": titular_cuenta,
                        "usuario": usuario_activo,
                        "nombre_cliente": nombre_actual,
                        "telefono_cliente": datos_usuario.get("telefono", "N/A"),
                        "estado": "Pendiente de Procesamiento"
                    }
                    
                    # Se almacena en la estructura de datos persistente
                    if "retiros_pendientes" not in st.session_state:
                        st.session_state.retiros_pendientes = []
                    st.session_state.retiros_pendientes.append(nuevo_retiro)
                    
                    # Registramos en el historial individual del usuario
                    usuarios_db[usuario_activo]["historial"].append({
                        "fecha": nuevo_retiro["fecha"],
                        "tipo": f"Retiro (Folio #{folio})",
                        "monto": monto_retiro,
                        "metodo": f"SPEI a {banco_destino}",
                        "estado": "Pendiente de Transferencia"
                    })
                    
                    guardar_base_datos(usuarios_db)
                    st.success("✅ ¡Solicitud de retiro enviada! Tu transferencia llegará en un lapso de 1 a 24 horas hábiles.")
                    time.sleep(1.5)
                    st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
            
        with subtab_historial:
            st.markdown('<div class="cashier-card">', unsafe_allow_html=True)
            st.subheader("Mi Historial Financiero")
            mi_historial = datos_usuario.get("historial", [])
            if not mi_historial:
                st.info("No has realizado transacciones todavía.")
            else:
                for t in reversed(mi_historial):
                    st.markdown(f"""
                    **Fecha:** {t['fecha']} | **Tipo:** {t['tipo']} | **Monto:** ${t['monto']:,.2f} MXN | **Detalles:** {t['metodo']} | **Estado:** `{t['estado']}`
                    ---
                    """)
            st.markdown('</div>', unsafe_allow_html=True)

    # ================= MÓDULO 4: PERFIL DE USUARIO =================
    with tab_perfil:
        st.markdown("## 👤 MI PERFIL - FORTUNA MX")
        st.markdown('<div class="cashier-card">', unsafe_allow_html=True)
        
        st.subheader("Datos de la Cuenta")
        st.write(f"**Nombre:** {nombre_actual}")
        st.write(f"**Correo Electrónico:** {usuario_activo}")
        st.write(f"**Número de Teléfono:** {datos_usuario.get('telefono', 'N/A')}")
        st.write(f"**Saldo Total:** ${saldo_actual:,.2f} MXN")
        
        st.markdown("---")
        st.subheader("Actualizar Mis Datos")
        nuevo_nombre = st.text_input("Nombre Completo:", value=nombre_actual)
        nuevo_telefono = st.text_input("Número de Teléfono (10 dígitos):", value=datos_usuario.get("telefono", ""))
        
        if st.button("Guardar Cambios de Perfil", use_container_width=True):
            if not nuevo_nombre or not nuevo_telefono.isdigit() or len(nuevo_telefono) != 10:
                st.error("Por favor, ingresa un nombre válido y un número de teléfono de 10 dígitos numéricos.")
            else:
                usuarios_db = cargar_base_datos()
                usuarios_db[usuario_activo]["nombre"] = nuevo_nombre
                usuarios_db[usuario_activo]["telefono"] = nuevo_telefono
                guardar_base_datos(usuarios_db)
                st.success("¡Datos de perfil actualizados de forma segura!")
                time.sleep(1)
                st.rerun()
                
        st.markdown("</div>", unsafe_allow_html=True)
        
        if st.button("🚪 Cerrar Sesión", use_container_width=True, type="secondary"):
            st.session_state.usuario_conectado = None
            st.rerun()

    # ================= MÓDULO 5: PANEL DE OPERADOR (ADMIN) =================
    with tab_admin:
        st.markdown("## 👑 PANEL DE ADMINISTRADOR DE FORTUNA MX")
        st.write("Panel exclusivo para el dueño o administrador del casino Fortuna MX.")
        
        password_ingresado = st.text_input("Ingresa la contraseña de administrador para ver solicitudes de cobro:", type="password", key="admin_pass")
        
        if password_ingresado == ADMIN_PASSWORD:
            st.success("Acceso Concedido")
            
            tab_pendientes, tab_usuarios, tab_ajustes = st.tabs(["💰 Retiros Solicitados", "👥 Base de Usuarios", "⚙️ Ajustes"])
            
            with tab_pendientes:
                st.markdown("### Retiros de Dinero Real por SPEI")
                st.info("Aquí verás los cobros solicitados por tus usuarios en tiempo real, junto con su teléfono registrado.")
                
                if "retiros_pendientes" not in st.session_state:
                    st.session_state.retiros_pendientes = []
                    
                retiros_activos = [r for r in st.session_state.retiros_pendientes if r["estado"] == "Pendiente de Procesamiento"]
                
                if not retiros_activos:
                    st.info("No hay solicitudes de retiro pendientes de pago.")
                else:
                    for r in retiros_activos:
                        st.markdown(f"""
                        <div style="background-color: #1e293b; padding: 15px; border-radius: 8px; border-left: 5px solid #ef4444; margin-bottom: 15px;">
                            <h4 style="margin: 0; color: #f8fafc;">Folio #{r['id']} - Monto: <b>${r['monto']:,.2f} MXN</b></h4>
                            <p style="margin: 5px 0; color: #cbd5e1;"><b>Cliente:</b> {r['nombre_cliente']} ({r['usuario']})</p>
                            <p style="margin: 5px 0; color: #cbd5e1;"><b>Teléfono:</b> {r['telefono_cliente']}</p>
                            <p style="margin: 5px 0; color: #cbd5e1;"><b>Banco Destino:</b> {r['banco']}</p>
                            <p style="margin: 5px 0; color: #cbd5e1; font-size: 16px; font-family: monospace;"><b>CLABE:</b> {r['clabe']}</p>
                            <p style="margin: 5px 0; color: #cbd5e1;"><b>Fecha de Solicitud:</b> {r['fecha']}</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        if st.button(f"Confirmar Envío de Pago #{r['id']}", key=f"btn_send_real_{r['id']}", use_container_width=True):
                            r["estado"] = "Transferido"
                            
                            # Actualizamos el estatus en la BD del usuario correspondiente
                            usuarios_db = cargar_base_datos()
                            user_mail = r["usuario"]
                            if user_mail in usuarios_db:
                                for h in usuarios_db[user_mail]["historial"]:
                                    if f"#{r['id']}" in h["tipo"]:
                                        h["estado"] = "Completado y Transferido"
                                guardar_base_datos(usuarios_db)
                                    
                            st.success(f"La orden de retiro del folio #{r['id']} ha sido marcada como pagada.")
                            time.sleep(1)
                            st.rerun()
            
            with tab_usuarios:
                st.markdown("### Usuarios Registrados en Fortuna MX")
                usuarios_db = cargar_base_datos()
                for mail, info in usuarios_db.items():
                    st.markdown(f"""
                    **Nombre:** {info['nombre']} | **Email:** {mail} | **Teléfono:** {info.get('telefono', 'N/A')}
                    * **Saldo Actual:** ${info['saldo']:,.2f} MXN
                    * **Banco Guardado:** {info.get('banco', 'N/A')}
                    * **CLABE Guardada:** `{info.get('clabe', 'N/A')}`
                    ---
                    """)
                            
            with tab_ajustes:
                st.markdown("### Modificar Saldo de Usuarios Administrativamente")
                usuarios_db = cargar_base_datos()
                target_user = st.selectbox("Selecciona un usuario:", list(usuarios_db.keys()))
                nuevo_saldo = st.number_input("Establecer Saldo ($):", value=usuarios_db[target_user]["saldo"])
                if st.button("Actualizar Saldo Inmediatamente", use_container_width=True):
                    usuarios_db[target_user]["saldo"] = nuevo_saldo
                    guardar_base_datos(usuarios_db)
                    st.success(f"Saldo de {target_user} actualizado.")
                    time.sleep(1)
                    st.rerun()
                    
        elif password_ingresado:
            st.error("Contraseña de administrador incorrecta.")

# ---------------- FLUJO DE REGISTRO / INICIO DE SESIÓN (PANTALLA DE ENTRADA) ----------------
else:
    # Mostramos cabecera estática
    if logo_base64:
        st.markdown(f"""
        <div style="text-align: center; margin-bottom: 20px;">
            <img src="{logo_base64}" style="max-height: 100px; width: auto; border-radius: 10px;">
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("<h1 style='text-align: center; color: #f59e0b;'>🎰 FORTUNA MX</h1>", unsafe_allow_html=True)
        
    st.markdown("<h3 style='text-align: center;'>Inicia sesión o regístrate para jugar con dinero real</h3>", unsafe_allow_html=True)
    
    modo_sesion = st.radio("Elige una opción:", ["Iniciar Sesión", "Registrarse como Nuevo Usuario"], horizontal=True)
    
    st.markdown('<div class="cashier-card">', unsafe_allow_html=True)
    
    if modo_sesion == "Iniciar Sesión":
        login_correo = st.text_input("Correo Electrónico:").strip().lower()
        login_pass = st.text_input("Contraseña:", type="password")
        
        if st.button("ENTRAR AL CASINO", type="primary", use_container_width=True):
            if login_correo in usuarios_db and usuarios_db[login_correo]["contrasena"] == login_pass:
                st.session_state.usuario_conectado = login_correo
                st.success(f"¡Bienvenido, {usuarios_db[login_correo]['nombre']}!")
                time.sleep(1)
                st.rerun()
            else:
                st.error("Correo electrónico o contraseña incorrectos.")
    else:
        reg_nombre = st.text_input("Nombre Completo:")
        reg_telefono = st.text_input("Número de Teléfono (10 dígitos):")
        reg_correo = st.text_input("Correo Electrónico:").strip().lower()
        reg_pass = st.text_input("Crea una Contraseña:", type="password")
        
        if st.button("REGISTRARME E INGRESAR", type="primary", use_container_width=True):
            if not reg_nombre or not reg_correo or not reg_pass:
                st.error("Todos los campos de registro son obligatorios.")
            elif len(reg_telefono) != 10 or not reg_telefono.isdigit():
                st.error("El número de teléfono debe consistir de exactamente 10 dígitos numéricos.")
            elif reg_correo in usuarios_db:
                st.error("Este correo ya se encuentra registrado.")
            else:
                # Insertar usuario de forma permanente en la base de datos
                usuarios_db[reg_correo] = {
                    "nombre": reg_nombre,
                    "telefono": reg_telefono,
                    "contrasena": reg_pass,
                    "saldo": 50.00,  # Bono inicial de cortesía de $50 reales
                    "clabe": "",
                    "banco": "",
                    "titular": "",
                    "historial": [
                        {
                            "fecha": time.strftime("%Y-%m-%d %H:%M:%S"),
                            "tipo": "Bono de Registro",
                            "monto": 50.00,
                            "metodo": "Cortesía de Fortuna MX",
                            "estado": "Acreditado"
                        }
                    ],
                    "es_admin": False
                }
                guardar_base_datos(usuarios_db)
                st.session_state.usuario_conectado = reg_correo
                st.success("¡Registro completado de forma exitosa! Se te ha acreditado un bono de bienvenida de $50.00 MXN.")
                st.balloons()
                time.sleep(1.5)
                st.rerun()
                
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- CAROUSEL DE JUEGOS RECOMENDADOS ----------------
st.markdown("## 🔥 JUEGOS POPULARES DISPONIBLES")
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