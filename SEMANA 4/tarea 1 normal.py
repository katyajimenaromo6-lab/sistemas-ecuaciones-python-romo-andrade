import time
import matplotlib.pyplot as plt



M = [
    [0, 0, 1/3, 1/2, 0],
    [1, 0, 0, 1/2, 0],
    [0, 1/2, 0, 0, 1],
    [0, 1/2, 1/3, 0, 0],
    [0, 0, 1/3, 0, 0]
]



T = [
    1/5,
    1/5,
    1/5,
    1/5,
    1/5
]



tiempos = [0]

A = [T[0]]
B = [T[1]]
C = [T[2]]
D = [T[3]]
E = [T[4]]


inicio = time.perf_counter()


print("T0 =", T)



for t in range(1, 23):

    nuevo = []

    for i in range(5):

        suma = 0

        for j in range(5):

            suma = suma + M[i][j] * T[j]

        nuevo.append(suma)

    T = nuevo


    tiempos.append(t)

    A.append(T[0])
    B.append(T[1])
    C.append(T[2])
    D.append(T[3])
    E.append(T[4])


    print("T", t, "=", T)


fin = time.perf_counter()



print()
print("RESULTADO FINAL T22")

print("A =", T[0])
print("B =", T[1])
print("C =", T[2])
print("D =", T[3])
print("E =", T[4])



print()
print("PORCENTAJES T22")

print("A =", T[0] * 100, "%")
print("B =", T[1] * 100, "%")
print("C =", T[2] * 100, "%")
print("D =", T[3] * 100, "%")
print("E =", T[4] * 100, "%")


print()
print("Tiempo de ejecucion:", fin - inicio, "segundos")



plt.plot(tiempos, A, marker="o", label="A")
plt.plot(tiempos, B, marker="o", label="B")
plt.plot(tiempos, C, marker="o", label="C")
plt.plot(tiempos, D, marker="o", label="D")
plt.plot(tiempos, E, marker="o", label="E")

plt.xlabel("Tiempo")
plt.ylabel("Posicionamiento")
plt.title("Posicionamiento temporal - Grafo 1")

plt.legend()
plt.grid()

plt.show()