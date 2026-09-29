import time


A = [
    [0, 1, 1, 1, 0, 0],
    [1, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 1, 0]
]

n = 6

persona = int(input("Que persona quieres hacer mas popular (1-6): "))


p = persona - 1

inicio = time.perf_counter()

print()
print("RELACIONES AGREGADAS")


for i in range(n):

    if i != p:

        if A[p][i] == 0:

            A[p][i] = 1
            A[i][p] = 1

            print("Se agrego la relacion", persona, "con", i + 1)




resultado = []

for i in range(n):

    resultado.append([])

    for j in range(n):

        suma = 0

        for k in range(n):

            suma = suma + A[i][k] * A[k][j]

        resultado[i].append(suma)


fin = time.perf_counter()




print()
print("A^2 =")

for i in range(n):

    for j in range(n):

        print(resultado[i][j], end=" ")

    print()




print()
print("POPULARIDAD")

for i in range(n):

    print("Persona", i + 1, "=", resultado[i][i])


print()
print("La persona elegida fue:", persona)
print("Su popularidad es:", resultado[p][p])

print("Tiempo de ejecucion:", fin - inicio, "segundos")