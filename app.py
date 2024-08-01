import streamlit as st
import requests
import json

def realizar_investigacion(tema):
    url = 'https://v2-api.respell.ai/spells/start'
    headers = {
        'Accept': 'application/json',
        'x-api-key': 'clxf3u99q003qweu1gn4o8321',
        'Content-Type': 'application/json'
    }
    data = {
        "spellId": "clzbq6xio01gwvv0ih1vejqb4",
        "wait": "true",
        "inputs": {
            "research_topic": tema
        }
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return None

st.title("Agente Investigador")

tema_investigacion = st.text_input("Ingrese el tema que desea investigar:")

if st.button("Investigar"):
    if tema_investigacion:
        with st.spinner("Investigando..."):
            resultado = realizar_investigacion(tema_investigacion)
        
        if resultado:
            st.success("Investigación completada")
            st.json(resultado)
        else:
            st.error("Hubo un error al realizar la investigación. Por favor, intente nuevamente.")
    else:
        st.warning("Por favor, ingrese un tema para investigar.")

st.sidebar.header("Acerca de")
st.sidebar.info("Esta aplicación utiliza la API de Respell.ai para realizar investigaciones sobre temas específicos.")
