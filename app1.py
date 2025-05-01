import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image

# Estilo de la página
st.set_page_config(page_title="OCR con Cámara", page_icon="📸", layout="centered")

# Encabezado
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>📷 Reconocimiento Óptico de Caracteres</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Toma una foto con texto y conviértelo automáticamente a caracteres digitales usando OCR.</p>", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("Opciones de visualización")
    filtro = st.radio("¿Aplicar filtro visual a la imagen?", ('🔍 Con Filtro', '🖼️ Sin Filtro'))

# Entrada de imagen desde la cámara
img_file_buffer = st.camera_input("Toma una foto con texto claro y legible:")

# Procesamiento de imagen y OCR
if img_file_buffer is not None:
    st.markdown("### Resultado:")
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    # Aplicar filtro (inverso de color)
    if filtro == '🔍 Con Filtro':
        cv2_img = cv2.bitwise_not(cv2_img)

    # Convertir a RGB y mostrar imagen procesada
    img_rgb = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    st.image(img_rgb, caption="Imagen procesada", use_column_width=True)

    # OCR
    text = pytesseract.image_to_string(img_rgb)
    
    # Mostrar resultado
    st.markdown("#### Texto Detectado:")
    st.code(text, language='markdown')
else:
    st.info("📸 Esperando que tomes una foto para procesarla.")



    


