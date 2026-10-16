# Complemento de recuperacion: perceptron diabetes en Python.
# Reproduce la regla de entrenamiento usada en Arduino, con el CSV adjunto.
import pandas as pd
import numpy as np
from pathlib import Path
p = Path(__file__).with_name('Diabetes_102_registros.csv')
df = pd.read_csv(p)
print('Columnas:', list(df.columns))
# El CSV entregado tiene las columnas IMC, Glucosa, Diagnostico.
# Si sus encabezados cambian, adecuar estos nombres.
cols = list(df.columns)
if len(cols) < 3: raise ValueError('Se requieren IMC, glucosa y clase')
arr = df.iloc[:, :3].apply(pd.to_numeric, errors='coerce').dropna().to_numpy()
X = np.column_stack([np.ones(len(arr)), arr[:,0]/10, arr[:,1]/100])
y = arr[:,2].astype(int)
w = np.zeros(3); eta = 0.1
for epoca in range(1, 1001):
    errores = 0
    for xi, d in zip(X,y):
        e = d - int(np.dot(w,xi)>=0)
        if e: w += eta*e*xi; errores += 1
    print(f'Epoca {epoca}: errores de actualizacion={errores}')
    if errores == 0: break
pred = (X @ w >= 0).astype(int)
print('Pesos W0,W1,W2:', w)
print('Aciertos en entrenamiento:', int((pred==y).sum()), '/',len(y))
print('Exactitud:', round(100*np.mean(pred==y),2),'%')
print('Nota: validacion sobre entrenamiento, no diagnostico clinico.')
