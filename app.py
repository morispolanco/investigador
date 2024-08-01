import streamlit as st
import requests
import json
from apscheduler.schedulers.background import BackgroundScheduler

# Configuración de la página
st.set_page_config(page_title="Agente Investigador", page_icon="🔍")

# Título de la aplicación
st.title("Agente Investigador")

# Obtener la API key de los secretos de Streamlit
api_key = st.secrets["api"]["key"]

# Función para hacer la solicitud a la API
def consultar_api(research_topic):
    url = 'https://v2-api.respell.ai/spells/start'
    headers = {
        'Accept': 'application/json',
        'x-api-key': api_key,
        'Content-Type': 'application/json'
    }
    data = {
        "spellId": "clzbq6xio01gwvv0ih1vejqb4",
        "wait": "true",
        "inputs": {
            "research_topic": research_topic
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error en la solicitud: {response.status_code}"

# Área de entrada de texto para el tema de investigación del usuario
research_topic = st.text_area("Escribe tu tema de investigación:", height=100)

# Botón para enviar la consulta
if st.button("Consultar"):
    if research_topic:
        with st.spinner("Consultando al agente..."):
            respuesta = consultar_api(research_topic)
        st.subheader("Resultados de la Investigación:")
        st.json(respuesta)
    else:
        st.warning("Por favor, escribe un tema de investigación antes de consultar.")

# Información adicional
st.sidebar.header("Acerca de esta aplicación")
st.sidebar.write("""
Esta aplicación utiliza un modelo avanzado para investigar y proporcionar información relevante sobre un tema dado. 
Simplemente ingresa tu tema de investigación y obtendrás respuestas detalladas.

Puedes investigar sobre:
- Ciencia
- Tecnología
- Historia
- Cultura
- Y mucho más...

¡No dudes en explorar cualquier tema de tu interés!
""")

# Pie de página
st.sidebar.markdown("---")
st.sidebar.markdown("Desarrollado con ❤️ para curiosos e investigadores")

# Función para mantener la app activa
def keep_alive():
    print("App still alive!")

# Configuración del scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(keep_alive, 'interval', minutes=30)
scheduler.start()
