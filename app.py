import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Configuração da página
st.set_page_config(
    page_title="Graficos",
    page_icon="🧮",
)

# Título da página
st.title("Graficos Streamlit")

# Generar datos
x = np.linspace(0, 10, 100)
y_seno = np.sin(x)
y_coseno = np.cos(x)


plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)  # (número de filas, número de columnas, índice)
plt.plot(x, y_seno, label='Seno', color='blue')
plt.title('Gráfico de la función seno')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()


plt.subplot(1, 2, 2)
plt.plot(x, y_coseno, label='Coseno', color='orange')
plt.title('Gráfico de la función coseno')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()


st.pyplot(plt)


st.subheader("Gráfico de Dispersão")
x_dispersion = np.random.rand(100)
y_dispersion = np.random.rand(100)

plt.figure(figsize=(8, 5))
plt.scatter(x_dispersion, y_dispersion, color='green', alpha=0.6)
plt.title('Gráfico de Dispersão')
plt.xlabel('Eje X (Aleatorio)')
plt.ylabel('Eje Y (Aleatorio)')

# Mostrar el gráfico de dispersión en Streamlit
st.pyplot(plt)