import time
import matplotlib.pyplot as plt

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

    # Inversa de B
    bi00 = h / det
    bi01 = -f / det
    bi10 = -g / det
    bi11 = e / det

    # A x B^-1
    r00 = a * bi00 + b * bi10
    r01 = a * bi01 + b * bi11
    r10 = c * bi00 + d * bi10
    r11 = c * bi01 + d * bi11

    # B^-1 x A
    s00 = bi00 * a + bi01 * c
    s01 = bi00 * b + bi01 * d
    s10 = bi10 * a + bi11 * c
    s11 = bi10 * b + bi11 * d

    fin = time.perf_counter()
    tiempo = fin - inicio

    print('Inversa de B:')
    print(bi00, bi01)
    print(bi10, bi11)

    print('Resultado de A x B^-1:')
    print(r00, r01)
    print(r10, r11)

    print('Resultado de B^-1 x A:')
    print(s00, s01)
    print(s10, s11)

    print(f'El tiempo de ejecucion es: {tiempo} segundos')

    # Grafica de A x B^-1
    x1 = [r00, r10]
    y1 = [r01, r11]

    # Grafica de B^-1 x A
    x2 = [s00, s10]
    y2 = [s01, s11]

    plt.plot(x1, y1, marker='o', label='A x B^-1')
    plt.plot(x2, y2, marker='o', label='B^-1 x A')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Comparacion de A x B^-1 y B^-1 x A')
    plt.grid()
    plt.legend()
    plt.show()

else:
    print('La matriz B no tiene inversa')