# Perceptron: cuatro compuertas logicas (AND, OR, NAND, NOR)
import numpy as np
import matplotlib.pyplot as plt

PATRONES = np.array([[0,0],[0,1],[1,0],[1,1]], dtype=float)
SALIDAS = {
    'AND':  [0,0,0,1],
    'OR':   [0,1,1,1],
    'NAND': [1,1,1,0],
    'NOR':  [1,0,0,0],
}
TASA = 0.1
MAX_EPOCAS = 100

def entrenar(nombre):
    d = np.array(SALIDAS[nombre], dtype=int)
    rng = np.random.RandomState(1)
    # W0 = sesgo, W1 y W2 = pesos de entradas
    w = rng.uniform(-0.5, 0.5, size=3)
    x = np.column_stack((np.ones(4), PATRONES))
    historia = []
    for epoca in range(1, MAX_EPOCAS + 1):
        errores = 0
        for xi, objetivo in zip(x, d):
            y = int(np.dot(w, xi) >= 0)
            e = objetivo - y
            w += TASA * e * xi
            errores += e * e
        pred = (x @ w >= 0).astype(int)
        aciertos = int(np.sum(pred == d))
        historia.append(errores / 4)
        print(f'{nombre}: epoca {epoca}, MSE={historia[-1]:.3f}, aciertos={aciertos}/4')
        if aciertos == 4:
            break
    print('Pesos finales [W0,W1,W2]:', w)
    print('X1 X2 | Deseada | Obtenida')
    for patron, esperado, obtenido in zip(PATRONES, d, pred):
        print(int(patron[0]), int(patron[1]), '|', esperado, '|', obtenido)
    return historia

if __name__ == '__main__':
    fig, ax = plt.subplots(figsize=(8, 5))
    for nombre in SALIDAS:
        historia = entrenar(nombre)
        ax.plot(range(1, len(historia)+1), historia, marker='o', label=nombre)
    ax.set(xlabel='Epoca', ylabel='MSE durante entrenamiento',
           title='Aprendizaje de las cuatro compuertas')
    ax.legend(); ax.grid(alpha=0.3); fig.tight_layout()
    fig.savefig('compuertas_entrenamiento.png', dpi=180)
    plt.show()
