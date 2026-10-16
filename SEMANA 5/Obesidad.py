
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
datos = pd.read_csv('Obesidad (1).csv')
print(datos.head())
print('Total de registros:',len(datos))

sin_obesidad = datos[datos['Obesidad'] == 0]
con_obesidad = datos[datos['Obesidad'] == 1]
plt.scatter(sin_obesidad['IMC'],sin_obesidad['Calorias'],label='Sin obesidad (0)')
plt.scatter(con_obesidad['IMC'],con_obesidad['Calorias'],label='Con obesidad (1)')
plt.xlabel('IMC')
plt.ylabel('Calorias por dia')
plt.title('Grafica de dispersion - Obesidad')
plt.legend()
plt.grid()
plt.savefig('Obesidad_Dispersion.png')
plt.show()
