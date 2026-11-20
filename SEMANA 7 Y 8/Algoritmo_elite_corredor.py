
def evaluar(x):
    return -x**4+84*x**3-2628*x**2+35336*x
poblacion=[81.5,57.75,65.25,78,0.5,127.75,57.5,85.25]
for generacion in range(1,11):
    print('\nGENERACION',generacion,'- ELITE')
    resultados=[]
    for i in range(8):
        x=poblacion[i]
        valor=evaluar(x)
        resultados.append((x,valor))
        print('C'+str(i+1),'| Decimal:',x,'| Evaluacion:',valor)
    mayor=max(resultados,key=lambda dato:dato[1])
    ganador=resultados.index(mayor)+1
    print('GANADOR: C'+str(ganador),'| Decimal:',mayor[0],'| Evaluacion:',mayor[1])
    if generacion==10:
        break
    ordenados=sorted(resultados,key=lambda dato:dato[1],reverse=True)
    nueva=[]
    for i in range(0,8,2):
        padre1=round(ordenados[i][0]*4)
        padre2=round(ordenados[i+1][0]*4)
        hijo1=(padre1&896)|(padre2&127)
        hijo2=(padre2&896)|(padre1&127)
        nueva.append(hijo1/4)
        nueva.append(hijo2/4)
    poblacion=nueva
print('\nFIN DE LAS 10 GENERACIONES')
