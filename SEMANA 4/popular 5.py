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




# 5 con 1
A[4][0] = 1
A[0][4] = 1

#  5 con 3
A[4][2] = 1
A[2][4] = 1

# 5 con 4
A[4][3] = 1
A[3][4] = 1


inicio = time.perf_counter()



# 5 con 1
A[4][0] = 1
A[0][4] = 1

# 5 con 3
A[4][2] = 1
A[2][4] = 1

# 5 con 4
A[4][3] = 1
A[3][4] = 1




# - 1 con 2
A[0][1] = 0
A[1][0] = 0

# - 1 con 3
A[0][2] = 0
A[2][0] = 0

# - 1 con 4
A[0][3] = 0
A[3][0] = 0

# -2 con 4
A[1][3] = 0
A[3][1] = 0

# - 4 con 6
A[3][5] = 0
A[5][3] = 0


inicio = time.perf_counter()


resultado = []

for i in range(n):

    resultado.append([])

    for j in range(n):

        suma = 0

        for k in range(n):

            suma = suma + A[i][k] * A[k][j]

        resultado[i].append(suma)


fin = time.perf_counter()




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
print("La persona 5 tiene una popularidad de:", resultado[4][4])

print("Tiempo de ejecucion:", fin - inicio, "segundos")