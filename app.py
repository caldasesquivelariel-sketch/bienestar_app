import streamlit as st
import re

# -------- ESTILOS DECORATIVOS --------
st.set_page_config(
    page_title="Bienestar Joven",
    page_icon="🌱",
    layout="centered"
)

st.markdown("""
<style>
body {
    background-color: #f0fdf4;
}
.titulo {
    text-align: center;
    font-size: 42px;
    color: #16a34a;
    font-weight: bold;
}
.subtitulo {
    text-align: center;
    font-size: 18px;
    color: #065f46;
}
.card {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}
.footer {
    text-align: center;
    color: #6b7280;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# -------- ENCABEZADO --------
st.markdown('<div class="titulo">🌱 Bienestar Joven</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitulo">Cuida tu salud física, emocional y social 💚</div>', unsafe_allow_html=True)

st.divider()

# -------- NOMBRE --------
st.markdown('<div class="card">', unsafe_allow_html=True)

nombre = st.text_input("👤 Escribe tu nombre completo:")

def nombre_valido(texto):
    patron = r"^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$"
    return re.match(patron, texto)

if nombre == "":
    st.info("ℹ️ El nombre es obligatorio.")
    nombre_ok = False
elif not nombre_valido(nombre):
    st.error("❌ No se permiten números ni símbolos.")
    nombre_ok = False
else:
    nombre_ok = True

st.markdown('</div>', unsafe_allow_html=True)

# -------- BIENESTAR FÍSICO --------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("💪 Bienestar Físico")
energia = st.slider("⚡ Energía", 0, 10, 5)
sueno = st.slider("🛌 Descanso", 0, 10, 5)
actividad = st.slider("🏃 Actividad física", 0, 10, 5)
st.markdown('</div>', unsafe_allow_html=True)

# -------- BIENESTAR EMOCIONAL --------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("😊 Bienestar Emocional")
animo = st.slider("😀 Estado de ánimo", 0, 10, 5)
estres = st.slider("😵 Estrés", 0, 10, 5)
emociones = st.slider("💭 Control emocional", 0, 10, 5)
st.markdown('</div>', unsafe_allow_html=True)

# -------- BIENESTAR MENTAL --------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("🧠 Bienestar Mental y Académico")
concentracion = st.slider("📚 Concentración", 0, 10, 5)
motivacion = st.slider("🎯 Motivación", 0, 10, 5)
presion = st.slider("⏰ Presión académica", 0, 10, 5)
st.markdown('</div>', unsafe_allow_html=True)

# -------- BIENESTAR SOCIAL --------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("🤝 Bienestar Social")
amistades = st.slider("👫 Amistades", 0, 10, 5)
familia = st.slider("🏠 Familia", 0, 10, 5)
comunicacion = st.slider("🗣️ Comunicación", 0, 10, 5)
st.markdown('</div>', unsafe_allow_html=True)

# -------- EVALUACIÓN --------
if st.button("✨ Evaluar mi Bienestar") and nombre_ok:

    bienestar_total = (
        energia + sueno + actividad +
        animo + (10 - estres) + emociones +
        concentracion + motivacion + (10 - presion) +
        amistades + familia + comunicacion
    ) / 12

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader(f"📊 Resultado de {nombre}")

    if bienestar_total >= 7.5:
        st.success("🎉 ¡Excelente bienestar! Sigue así 💚")
        st.balloons()
    elif bienestar_total >= 5:
        st.warning("🙂 Buen avance, puedes mejorar algunos puntos.")
    else:
        st.error("💙 Necesitas apoyo, no estás solo/a.")

    st.write(f"⭐ Puntaje final: **{bienestar_total:.1f} / 10**")
    st.markdown('</div>', unsafe_allow_html=True)

# -------- PIE --------
st.markdown('<div class="footer">Prototipo educativo – Bienestar Integral Adolescente 🌱</div>', unsafe_allow_html=True)
