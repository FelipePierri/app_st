import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
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

df = pd.read_csv(r"C:\Users\Usuario\Desktop\All\PythonDSA\Dataset2\Datasets\producao_grega.csv", delimiter= ";")
df

X = df.iloc[:,1:]
Y = df.iloc[:,0:1]
print(X,Y)

from sklearn import tree
modelo = tree.DecisionTreeClassifier()
modelo.fit(X,Y)

texto = tree.export_text(modelo)
print(texto)

fig, ax = plt.subplots(1,1)
im = tree.plot_tree(modelo, filled = True)
fig.savefig("ArvoreAula.pdf")

from sklearn.model_selection import train_test_split
X_treino, X_teste, Y_treino, Y_teste = train_test_split(X, Y, test_size = 0.3)

print("Total dos dados: ", len(X))
print("Total dos dados no treino: ", len(X_treino))
print("Total dos dados no teste: ", len(X_teste))
print("Total dos dados: ", len(X))