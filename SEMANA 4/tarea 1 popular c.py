import time
import matplotlib.pyplot as plt



R = [
    [0, 0, 1, 1, 0],
    [1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0]
]


inicio = time.perf_counter()

encontrada = False



for j in range(5):

    if encontrada == True:
        break

    for i in range(5):

        if i != j:

            
            prueba = []

            for fila in R:
                prueba.append(fila.copy())


            
            
            if prueba[i][j] == 0:
                prueba[i][j] = 1

            else:
                prueba[i][j] = 0


            
            salidas = 0

            for k in range(5):
                salidas = salidas + prueba[k][j]


            
            if salidas > 0:


                
                M = []

                for a in range(5):

                    M.append([])

                    for b in range(5):
                        M[a].append(0)


                
                for b in range(5):

                    relaciones = 0

                    for a in range(5):
                        relaciones = relaciones + prueba[a][b]


                    for a in range(5):

                        if prueba[a][b] == 1:
                            M[a][b] = 1 / relaciones


                # T0
                T = [
                    1/5,
                    1/5,
                    1/5,
                    1/5,
                    1/5
                ]


                
                for t in range(1, 23):

                    nuevo = []

                    for a in range(5):

                        suma = 0

                        for b in range(5):

                            suma = suma + M[a][b] * T[b]

                        nuevo.append(suma)

                    T = nuevo


                
                if T[2] > T[0] and T[2] > T[1] and T[2] > T[3] and T[2] > T[4]:

                    encontrada = True

                    matriz_encontrada = M

                    relaciones_encontradas = prueba

                    resultado = T

                    break


fin = time.perf_counter()



if encontrada == True:

    print()
    print("MATRIZ ENCONTRADA")

    for fila in matriz_encontrada:
        print(fila)


    print()
    print("PORCENTAJES T22")

    print("A =", resultado[0] * 100, "%")
    print("B =", resultado[1] * 100, "%")
    print("C =", resultado[2] * 100, "%")
    print("D =", resultado[3] * 100, "%")
    print("E =", resultado[4] * 100, "%")


    print()
    print("C ES LA MAS POPULAR")


    
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


    for t in range(1, 23):

        nuevo = []

        for i in range(5):

            suma = 0

            for j in range(5):

                suma = suma + matriz_encontrada[i][j] * T[j]

            nuevo.append(suma)

        T = nuevo


        tiempos.append(t)

        A.append(T[0])
        B.append(T[1])
        C.append(T[2])
        D.append(T[3])
        E.append(T[4])


    
    plt.plot(tiempos, A, marker="o", label="A")
    plt.plot(tiempos, B, marker="o", label="B")
    plt.plot(tiempos, C, marker="o", label="C")
    plt.plot(tiempos, D, marker="o", label="D")
    plt.plot(tiempos, E, marker="o", label="E")

    plt.xlabel("Tiempo")
    plt.ylabel("Posicionamiento")
    plt.title("Matriz encontrada - C mas popular")

    plt.legend()
    plt.grid()

    plt.show()


else:

    print("No se encontro una matriz")


print()
print("Tiempo de ejecucion:", fin - inicio, "segundos")