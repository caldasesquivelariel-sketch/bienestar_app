import streamlit as st
import re

# Configuración de la página
st.set_page_config(
    page_title="Bienestar Joven",
    page_icon="🌱",
    layout="centered"
)

st.title("🌱 Bienestar Joven")
st.write("Evalúa tu bienestar integral y recibe recomendaciones y felicitaciones 💚")

st.divider()

# Validación del nombre
nombre = st.text_input("👤 Escribe tu nombre completo:")

def nombre_valido(texto):
    patron = r"^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$"
    return re.match(patron, texto)

if nombre == "":
    st.info("ℹ️ El nombre es obligatorio.")
    nombre_ok = False
elif not nombre_valido(nombre):
    st.error("❌ El nombre no debe contener números ni símbolos.")
    nombre_ok = False
else:
    nombre_ok = True

st.divider()

# Bienestar físico
st.subheader("💪 Bienestar Físico")
energia = st.slider("¿Cuánta energía tienes hoy?", 0, 10, 5)
sueno = st.slider("¿Cómo fue tu descanso?", 0, 10, 5)
actividad = st.slider("Nivel de actividad física", 0, 10, 5)

st.divider()

# Bienestar emocional
st.subheader("😊 Bienestar Emocional")
animo = st.slider("Estado de ánimo", 0, 10, 5)
estres = st.slider("Nivel de estrés", 0, 10, 5)
emociones = st.slider("Control de emociones", 0, 10, 5)

st.divider()

# Bienestar mental / académico
st.subheader("🧠 Bienestar Mental y Académico")
concentracion = st.slider("Nivel de concentración", 0, 10, 5)
motivacion = st.slider("Motivación para estudiar", 0, 10, 5)
presion = st.slider("Presión académica", 0, 10, 5)

st.divider()

# Bienestar social
st.subheader("🤝 Bienestar Social")
amistades = st.slider("Relación con amistades", 0, 10, 5)
familia = st.slider("Relación familiar", 0, 10, 5)
comunicacion = st.slider("Comunicación con otras personas", 0, 10, 5)

st.divider()

# Evaluación
if st.button("🔍 Evaluar mi Bienestar"):

    if not nombre_ok:
        st.warning("⚠️ Corrige tu nombre para continuar.")
    else:
        bienestar_total = (
            energia + sueno + actividad +
            animo + (10 - estres) + emociones +
            concentracion + motivacion + (10 - presion) +
            amistades + familia + comunicacion
        ) / 12

        st.subheader(f"📊 Resultado de {nombre}")

        # Resultado general
        if bienestar_total >= 7.5:
            st.success("🎉 ¡FELICITACIONES! Tu bienestar integral es ALTO 💚")
            st.balloons()
        elif bienestar_total >= 5:
            st.warning("🙂 Tu bienestar es MEDIO. Vas por buen camino.")
        else:
            st.error("💙 Tu bienestar es BAJO. Recuerda que pedir ayuda está bien.")

        st.write(f"**Puntaje final:** {bienestar_total:.1f} / 10")

        st.divider()
        st.subheader("🌟 Mensajes Positivos y Recomendaciones")

        # Felicitaciones físicas
        if sueno >= 7:
            st.success("🛌 ¡Excelente descanso! Dormir bien fortalece tu salud.")
        if actividad >= 7:
            st.success("🏃 ¡Muy bien! Mantenerte activo es clave para tu bienestar.")
        if energia >= 7:
            st.success("⚡ Tienes buena energía, sigue cuidándote.")

        # Felicitaciones emocionales
        if animo >= 7:
            st.success("😊 ¡Buen estado de ánimo! Eso ayuda a enfrentar retos.")
        if estres <= 3:
            st.success("🧘 ¡Manejas bien el estrés! Sigue así.")
        if emociones >= 7:
            st.success("💚 Sabes manejar tus emociones, ¡felicitaciones!")

        # Felicitaciones mentales / académicas
        if concentracion >= 7:
            st.success("🧠 Excelente concentración.")
        if motivacion >= 7:
            st.success("🎯 Tienes buena motivación para estudiar.")
        if presion <= 3:
            st.success("📘 Manejas bien la presión académica.")

        # Felicitaciones sociales
        if amistades >= 7:
            st.success("🤝 Tienes buenas relaciones con tus amistades.")
        if familia >= 7:
            st.success("🏠 Buen vínculo familiar, eso es muy importante.")
        if comunicacion >= 7:
            st.success("🗣️ Te comunicas muy bien con los demás.")

        st.divider()
        st.subheader("💡 Recomendaciones de Mejora")

        # Recomendaciones solo si están bajas
        if sueno < 5:
            st.write("🛌 Intenta dormir entre 7 y 9 horas.")
        if actividad < 5:
            st.write("🏃 Realiza actividad física regularmente.")
        if estres > 6:
            st.write("🧘 Practica técnicas de relajación.")
        if concentracion < 5:
            st.write("📵 Reduce distracciones al estudiar.")
        if comunicacion < 5:
            st.write("🗣️ Expresar lo que sientes mejora las relaciones.")

# Pie de página
st.divider()
st.caption("Prototipo educativo – Bienestar Integral Adolescente 🌱")


    st.write(f"⭐ Puntaje final: **{bienestar_total:.1f} / 10**")
    st.markdown('</div>', unsafe_allow_html=True)

# -------- PIE --------
st.markdown('<div class="footer">Prototipo educativo – Bienestar Integral Adolescente 🌱</div>', unsafe_allow_html=True)
