import streamlit as st
import re

# Configuración de la página
st.set_page_config(
    page_title="Bienestar Joven",
    page_icon="🌱",
    layout="centered"
)

st.title("🌱 Bienestar Joven")
st.write("Evalúa tu bienestar integral de forma segura y personalizada 💚")

st.divider()

# 👉 Nombre obligatorio con validación
nombre = st.text_input("👤 Escribe tu nombre completo:")

def nombre_valido(texto):
    # Permite solo letras y espacios (incluye tildes)
    patron = r"^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$"
    return re.match(patron, texto)

if nombre == "":
    st.info("ℹ️ El nombre es obligatorio para continuar.")
    nombre_ok = False
elif not nombre_valido(nombre):
    st.error("❌ El nombre no debe contener números ni símbolos. Corrígelo.")
    nombre_ok = False
else:
    nombre_ok = True

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
comunicacion = st.slider("Comunicación con otras personas", 0, 10, 5)

st.divider()

# Botón de evaluación (bloqueado si el nombre es inválido)
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

        if bienestar_total >= 7.5:
            st.success("🌟 Tu bienestar es ALTO. ¡Sigue así!")
            st.balloons()
        elif bienestar_total >= 5:
            st.warning("🙂 Tu bienestar es MEDIO. Puedes mejorar algunos aspectos.")
        else:
            st.error("💙 Tu bienestar es BAJO. No estás solo/a.")

        st.write(f"**Puntaje final:** {bienestar_total:.1f} / 10")

        st.divider()

        st.subheader("💡 Recomendaciones")

        if sueno < 5:
            st.write("🛌 Mejora tus horarios de sueño.")
        if estres > 6:
            st.write("🧘 Practica respiración y descanso.")
        if actividad < 5:
            st.write("🏃 Realiza actividad física regularmente.")
        if animo < 5:
            st.write("💬 Habla con alguien de confianza.")
        if motivacion < 5:
            st.write("📚 Organiza tus tareas paso a paso.")

# Pie de página
st.divider()
st.caption("Prototipo educativo – Bienestar Integral Adolescente 🌱")
