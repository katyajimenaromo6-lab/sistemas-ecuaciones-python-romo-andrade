import time

tamano = int(input('Tamaño de la matriz: '))
n = int(input('Potencia de la matriz: '))

A = []
resultado = []

for i in range(tamano):
    A.append([])

    for j in range(tamano):
        a = int(input(f'Valor de A[{i}][{j}]: '))
        A[i].append(a)

inicio = time.perf_counter()

for i in range(tamano):
    resultado.append([])

    for j in range(tamano):
        resultado[i].append(A[i][j])

for potencia in range(1, n):

    C = []

    for i in range(tamano):
        C.append([])

        for j in range(tamano):
            suma = 0

            for k in range(tamano):
                suma = suma + resultado[i][k] * A[k][j]

            C[i].append(suma)

    resultado = C

fin = time.perf_counter()
tiempo = fin - inicio

print(f'Matriz A elevada a la potencia {n}:')

for i in range(tamano):
    for j in range(tamano):
        print(resultado[i][j], end=' ')
    print()

print(f'El tiempo de ejecucion es: {tiempo} segundos')
