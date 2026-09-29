import time
import matplotlib.pyplot as plt



R = [
    [0, 0, 1, 1, 0],
    [1, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [1, 1, 1, 0, 1],
    [0, 0, 1, 0, 0]
]


inicio = time.perf_counter()



cambios = []

for j in range(5):

    for i in range(5):

        if i != j:

            cambios.append([i, j])


encontrada = False



for x in range(len(cambios)):

    if encontrada == True:
        break

    for y in range(x + 1, len(cambios)):

        if encontrada == True:
            break

        for z in range(y + 1, len(cambios)):

            if encontrada == True:
                break

            for w in range(z + 1, len(cambios)):


                
                prueba = []

                for fila in R:
                    prueba.append(fila.copy())


                
                i = cambios[x][0]
                j = cambios[x][1]

                if prueba[i][j] == 0:
                    prueba[i][j] = 1
                else:
                    prueba[i][j] = 0


                
                i = cambios[y][0]
                j = cambios[y][1]

                if prueba[i][j] == 0:
                    prueba[i][j] = 1
                else:
                    prueba[i][j] = 0


                
                i = cambios[z][0]
                j = cambios[z][1]

                if prueba[i][j] == 0:
                    prueba[i][j] = 1
                else:
                    prueba[i][j] = 0


                
                i = cambios[w][0]
                j = cambios[w][1]

                if prueba[i][j] == 0:
                    prueba[i][j] = 1
                else:
                    prueba[i][j] = 0


        
                valido = True

                for j in range(5):

                    salidas = 0

                    for i in range(5):
                        salidas = salidas + prueba[i][j]

                    if salidas == 0:
                        valido = False


                if valido == True:


                    
                    M = []

                    for i in range(5):

                        M.append([])

                        for j in range(5):
                            M[i].append(0)


                
                    for j in range(5):

                        relaciones = 0

                        for i in range(5):
                            relaciones = relaciones + prueba[i][j]


                        for i in range(5):

                            if prueba[i][j] == 1:
                                M[i][j] = 1 / relaciones


                    
                    T = [
                        1/5,
                        1/5,
                        1/5,
                        1/5,
                        1/5
                    ]


                    T21 = []


                    
                    for t in range(1, 23):

                        nuevo = []

                        for i in range(5):

                            suma = 0

                            for j in range(5):
                                suma = suma + M[i][j] * T[j]

                            nuevo.append(suma)

                        T = nuevo


                        
                        if t == 21:
                            T21 = T.copy()


                
                    e_mayor = False

                    if T[4] > T[0] and T[4] > T[1] and T[4] > T[2] and T[4] > T[3]:
                        e_mayor = True


                    
                    estable = True

                    for i in range(5):

                        diferencia = T[i] - T21[i]

                        if diferencia < 0:
                            diferencia = diferencia * -1

                        if diferencia > 0.001:
                            estable = False


                    
                    if e_mayor == True and estable == True:

                        encontrada = True

                        matriz_encontrada = M
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
    print("E ES LA MAS POPULAR")


    
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
    plt.title("Matriz encontrada - E mas popular")

    plt.legend()
    plt.grid()

    plt.show()


else:

    print("No se encontro una matriz")


print()
print("Tiempo de ejecucion:", fin - inicio, "segundos")