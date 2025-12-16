import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Bienestar Joven",
    page_icon="🌱",
    layout="centered"
)

# Título principal
st.title("🌱 Bienestar Joven")
st.write("Una app para conocer cómo te sientes hoy 💚")

st.divider()

# Sección física
st.subheader("💪 Bienestar Físico")
energia = st.slider("¿Cuánta energía tienes hoy?", 0, 10, 5)
sueno = st.slider("¿Cómo fue tu descanso?", 0, 10, 5)
actividad = st.slider("Nivel de actividad física", 0, 10, 5)

st.divider()

# Sección emocional
st.subheader("😊 Bienestar Emocional")
animo = st.slider("Estado de ánimo", 0, 10, 5)
estres = st.slider("Nivel de estrés", 0, 10, 5)
emociones = st.slider("Control de emociones", 0, 10, 5)

st.divider()

# Sección mental / académica
st.subheader("🧠 Bienestar Mental y Académico")
concentracion = st.slider("Nivel de concentración", 0, 10, 5)
motivacion = st.slider("Motivación para estudiar", 0, 10, 5)
presion = st.slider("Presión académica", 0, 10, 5)

st.divider()

# Sección social
st.subheader("🤝 Bienestar Social")
amistades = st.slider("Relación con amistades", 0, 10, 5)
familia = st.slider("Relación familiar", 0, 10, 5)
comunicacion = st.slider("Comunicación con otros", 0, 10, 5)

st.divider()

# Botón de evaluación
if st.button("🔍 Evaluar mi Bienestar"):
    
    # Ajustes (menos estrés y presión = mejor)
    bienestar_total = (
        energia + sueno + actividad +
        animo + (10 - estres) + emociones +
        concentracion + motivacion + (10 - presion) +
        amistades + familia + comunicacion
    ) / 12

    st.subheader("📊 Resultado General")

    if bienestar_total >= 7.5:
        st.success("🌟 Tu bienestar es ALTO. ¡Sigue así!")
        st.balloons()

    elif bienestar_total >= 5:
        st.warning("🙂 Tu bienestar es MEDIO. Puedes mejorar algunos aspectos.")

    else:
        st.error("💙 Tu bienestar es BAJO. Hablar con alguien puede ayudarte.")

    st.write(f"**Puntaje final:** {bienestar_total:.1f} / 10")

    st.divider()

    st.subheader("💡 Recomendaciones")

    if sueno < 5:
        st.write("🛌 Intenta dormir más y mejorar tus horarios.")
    if estres > 6:
        st.write("🧘 Practica respiración o toma descansos.")
    if actividad < 5:
        st.write("🏃 Moverte un poco cada día ayuda mucho.")
    if animo < 5:
        st.write("💬 Habla con alguien de confianza.")
    if motivacion < 5:
        st.write("📚 Organiza tus tareas en partes pequeñas.")

# Pie de página
st.divider()
st.caption("App prototipo – Bienestar Integral Adolescente 🌱")
