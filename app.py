import streamlit as st
import requests
import json

# Leer la API key desde los secretos
api_key = st.secrets["api"]["key"]

# Título de la aplicación
st.title("Agente Investigador")

# Instrucciones
st.write("Ingrese un tema de investigación y obtenga información relevante.")

# Input del usuario
research_topic = st.text_input("Tema de Investigación")

# Botón para iniciar la búsqueda
if st.button("Buscar"):
    if research_topic:
        # Configurar la solicitud a la API
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

        # Enviar la solicitud
        response = requests.post(url, headers=headers, data=json.dumps(data))

        # Procesar la respuesta
        if response.status_code == 200:
            result = response.json()
            st.write("Resultados de la investigación:")
            st.json(result)
        else:
            st.error(f"Error en la solicitud: {response.status_code}")
    else:
        st.warning("Por favor, ingrese un tema de investigación.")

# Ejecutar la aplicación de Streamlit con el siguiente comando en la terminal:
# streamlit run agente_investigador.py
