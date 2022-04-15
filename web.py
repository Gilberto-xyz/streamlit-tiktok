# Librerias 
import pandas as pd 
import numpy as np
# 📊 con Matplotlib 
import matplotlib.pyplot as plt
import streamlit as st

st.header('Hola Tiktok')


# Cargamos el dataset
dataset = pd.read_csv('Tech_sector_diversity_demographics_2016.csv')
# Porcentaje de mujeres en el sector tecnologico
genero = dataset.groupby('gender')['count'].sum().sort_values(ascending=False)


fig, ax = plt.subplots(figsize=(10,10))
plt.style.use('dark_background')
ax.bar(genero.index, genero.values)
plt.show()

# Mostramos la primer grafica
st.pyplot(fig)


fig, ax = plt.subplots(figsize=(10,10))
ax.pie(genero.values, labels=genero.index, autopct='%1.1f%%')
plt.show()

# Mostramos la siguiente
st.pyplot(fig)