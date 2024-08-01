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
            "research_topic": f"Investiga sobre '{tema}' y proporciona un resumen detallado en español."
        }
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def formatear_resultado_txt(resultado):
    if 'outputs' in resultado and 'research_result' in resultado['outputs']:
        contenido = resultado['outputs']['research_result']
        txt = f"""
Resultado de la Investigación
=============================

{contenido}
"""
        return txt
    return "No se pudo obtener un resultado formateado."

st.set_page_config(page_title="Agente Investigador", layout="wide")

st.title("Agente Investigador")

tema_investigacion = st.text_input("Ingrese el tema que desea investigar:")

if st.button("Investigar"):
    if tema_investigacion:
        with st.spinner("Investigando..."):
            resultado = realizar_investigacion(tema_investigacion)
        
        if resultado:
            st.success("Investigación completada")
            txt_resultado = formatear_resultado_txt(resultado)
            st.text_area("Resultado de la investigación:", value=txt_resultado, height=400)
            
            # Opción para descargar el resultado como archivo .txt
            st.download_button(
                label="Descargar resultado como .txt",
                data=txt_resultado,
                file_name="resultado_investigacion.txt",
                mime="text/plain"
            )
        else:
            st.error("Hubo un error al realizar la investigación. Por favor, intente nuevamente.")
    else:
        st.warning("Por favor, ingrese un tema para investigar.")

st.sidebar.header("Acerca de")
st.sidebar.info("Esta aplicación utiliza la API de Respell.ai para realizar investigaciones sobre temas específicos y presenta los resultados en español en formato de texto plano.")
