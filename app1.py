import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image

# Título principal
st.title("📜 Taylor’s Secret Notes Scanner")

st.markdown("""
Convierte tu cámara en una herramienta que revela mensajes ocultos,  
como si estuvieras descifrando notas perdidas del diario de *Taylor Swift*. 💌  
Toma una foto, aplica un filtro y deja que la magia del OCR haga su trabajo ✨
""")

# Capturar imagen
img_file_buffer = st.camera_input("📸 Toma una foto de una nota, carta o texto manuscrito")

# Sidebar
with st.sidebar:
    st.subheader("🪞 Configuración del Filtro")
    filtro = st.radio("Aplicar Filtro", ('Con Filtro', 'Sin Filtro'))
    st.caption("El filtro invierte los colores para mejorar la lectura en fondos claros o manuscritos.")

# Procesamiento de imagen y OCR
if img_file_buffer is not None:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    
    if filtro == 'Con Filtro':
        cv2_img = cv2.bitwise_not(cv2_img)
        st.info("🔄 Filtro aplicado: Inversión de color")
    else:
        st.info("📷 Sin filtro aplicado")

    img_rgb = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    
    # Procesar texto con Tesseract
    with st.spinner("Analizando imagen y buscando letras ocultas... 🕵️‍♀️"):
        text = pytesseract.image_to_string(img_rgb)
    
    # Mostrar resultado
    st.subheader("🪶 Texto Detectado:")
    if text.strip():
        st.success("✨ Resultado del análisis:")
        st.write(text)
    else:
        st.warning("No se detectó texto. Intenta ajustar el filtro o mejorar la iluminación.")

st.caption("💫 Desarrollado por Migue — inspirado en las eras de Taylor Swift 💖")
