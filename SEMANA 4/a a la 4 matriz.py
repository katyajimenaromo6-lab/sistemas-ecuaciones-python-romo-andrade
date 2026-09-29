import time

A = [
    [3, 2, 1, 0, 0, 0],
    [0, 2, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0],
    [0, 0, 0, 2, 2, 1],
    [0, 0, 0, 2, 2, 1],
    [0, 0, 0, 1, 1, 2]
]

n = 6

inicio = time.perf_counter()


resultado = A


for potencia in range(3):

    nueva = []

    for i in range(n):
        nueva.append([])

        for j in range(n):
            suma = 0

            for k in range(n):
                suma = suma + resultado[i][k] * A[k][j]

            nueva[i].append(suma)

    resultado = nueva

fin = time.perf_counter()

print("A^4 =")

for i in range(n):
    for j in range(n):
        print(resultado[i][j], end=" ")
    print()

print("Tiempo de ejecucion:", fin - inicio, "segundos")