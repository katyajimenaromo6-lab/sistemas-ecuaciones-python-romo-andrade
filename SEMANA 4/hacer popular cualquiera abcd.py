import time
import matplotlib.pyplot as plt



R = [
    [0, 0, 1, 1],
    [1, 0, 0, 1],
    [0, 1, 0, 0],
    [0, 1, 1, 0]
]


persona = input("Cual quieres hacer mas popular (A, B, C o D): ")




if persona == "A":

    #  A hacia C
    R[2][0] = 1

    #  B hacia A
    R[0][1] = 1


if persona == "B":

    
    print("B ya es el mas popular en el ejercicio original")


if persona == "C":

    # Quitar  B hacia D
    # B  hacia C
    R[3][1] = 0


if persona == "D":

    #  A hacia D
    R[3][0] = 1




M = []

for i in range(4):

    M.append([])

    for j in range(4):

        M[i].append(0)



for j in range(4):

    relaciones = 0

    for i in range(4):

        relaciones = relaciones + R[i][j]


    
    for i in range(4):

        if R[i][j] == 1:

            M[i][j] = 1 / relaciones


print()
print("MATRIZ MODIFICADA")

for fila in M:
    print(fila)



T = [
    1/4,
    1/4,
    1/4,
    1/4
]



tiempos = [0]

A = [T[0]]
B = [T[1]]
C = [T[2]]
D = [T[3]]


inicio = time.perf_counter()


print()
print("T0 =", T)




for t in range(1, 23):

    nuevo = []

    for i in range(4):

        suma = 0

        for j in range(4):

            suma = suma + M[i][j] * T[j]

        nuevo.append(suma)


    T = nuevo


    tiempos.append(t)

    A.append(T[0])
    B.append(T[1])
    C.append(T[2])
    D.append(T[3])


    print("T", t, "=", T)


fin = time.perf_counter()


# RESULTADOS

print()
print("RESULTADO FINAL T22")

print("A =", T[0])
print("B =", T[1])
print("C =", T[2])
print("D =", T[3])


print()
print("PORCENTAJES T22")

print("A =", T[0] * 100, "%")
print("B =", T[1] * 100, "%")
print("C =", T[2] * 100, "%")
print("D =", T[3] * 100, "%")


print()
print("Se eligio hacer mas popular a:", persona)


print()
print("Tiempo de ejecucion:", fin - inicio, "segundos")




plt.plot(tiempos, A, marker="o", label="A")
plt.plot(tiempos, B, marker="o", label="B")
plt.plot(tiempos, C, marker="o", label="C")
plt.plot(tiempos, D, marker="o", label="D")

plt.xlabel("Tiempo")
plt.ylabel("Posicionamiento")
plt.title("Posicionamiento temporal")

plt.legend()
plt.grid()

plt.show()