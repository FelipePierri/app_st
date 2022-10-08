import streamlit as st
import pandas as pd

st.write("# Grafico interativo")
l_numeros = []

if "lista" not in st.session_state:
    st.session_state["lista"] = []

# Usuario digita um numero
numero_digitado = st.number_input('Digite dois numeros')

# Quando o botão é pressionado
if st.button('adiciona numero') == True:
    st.session_state["lista"].append(numero_digitado)

# Plota o gráfico
st.line_chart(st.session_state["lista"])

st.session_state