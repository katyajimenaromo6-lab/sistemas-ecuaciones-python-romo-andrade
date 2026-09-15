import time

n = int(input('Tamaño de la matriz: '))

A = []
B = []
C = []

for i in range(n):
    A.append([])
    B.append([])
    C.append([])

    for j in range(n):
        a = int(input(f'Valor de A[{i}][{j}]: '))
        b = int(input(f'Valor de B[{i}][{j}]: '))

        A[i].append(a)
        B[i].append(b)

inicio = time.perf_counter()

for i in range(n):
    for j in range(n):
        C[i].append(A[i][j] - B[i][j])

fin = time.perf_counter()

tiempo = fin - inicio

print('Matriz resultado:')

for i in range(n):
    for j in range(n):
        print(C[i][j], end=' ')
    print()

print(f'El tiempo de ejecucion es: {tiempo} segundos')