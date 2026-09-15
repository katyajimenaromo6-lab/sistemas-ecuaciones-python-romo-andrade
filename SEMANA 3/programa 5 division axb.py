import time

print('MATRIZ A')

a = float(input('Valor de A[0][0]: '))
b = float(input('Valor de A[0][1]: '))
c = float(input('Valor de A[1][0]: '))
d = float(input('Valor de A[1][1]: '))

print('MATRIZ B')

e = float(input('Valor de B[0][0]: '))
f = float(input('Valor de B[0][1]: '))
g = float(input('Valor de B[1][0]: '))
h = float(input('Valor de B[1][1]: '))

inicio = time.perf_counter()

det = e * h - f * g

if det != 0:

    bi00 = h / det
    bi01 = -f / det
    bi10 = -g / det
    bi11 = e / det

    r00 = a * bi00 + b * bi10
    r01 = a * bi01 + b * bi11
    r10 = c * bi00 + d * bi10
    r11 = c * bi01 + d * bi11

    fin = time.perf_counter()
    tiempo = fin - inicio

    print('Inversa de B:')
    print(bi00, bi01)
    print(bi10, bi11)

    print('Resultado de A x B^-1:')
    print(r00, r01)
    print(r10, r11)

    print(f'El tiempo de ejecucion es: {tiempo} segundos')

else:
    print('La matriz B no tiene inversa')