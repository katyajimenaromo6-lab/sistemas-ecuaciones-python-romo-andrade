
def evaluar(x):
    return -x**4+84*x**3-2628*x**2+35336*x
poblacion=[81.5,57.75,65.25,78,0.5,127.75,57.5,85.25]
for generacion in range(1,11):
    print('\nGENERACION',generacion,'- SEMENTAL')
    resultados=[]
    for i in range(8):
        x=poblacion[i]
        valor=evaluar(x)
        resultados.append(valor)
        print('C'+str(i+1),'| Decimal:',x,'| Evaluacion:',valor)
    mayor=max(resultados)
    ganador=resultados.index(mayor)
    semental=poblacion[ganador]
    print('GANADOR: C'+str(ganador+1),'| Decimal:',semental,'| Evaluacion:',mayor)
    if generacion==10:
        break
    nueva=[semental]
    for i in range(8):
        if i!=ganador:
            padre1=round(semental*4)
            padre2=round(poblacion[i]*4)
            hijo=(padre1&896)|(padre2&127)
            nueva.append(hijo/4)
    poblacion=nueva
print('\nFIN DE LAS 10 GENERACIONES')
