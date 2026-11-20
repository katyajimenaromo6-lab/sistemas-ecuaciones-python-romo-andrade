import random
def evaluar(x):
    return -2*x**2+150*x+75
poblacion=[78,65.25,63.75,85.5,89.75,53.25,1.5,81.5]
for generacion in range(1,11):
    print('\nGENERACION',generacion,'- ALEATORIO')
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
    padres=poblacion.copy()
    random.shuffle(padres)
    nueva=[]
    for i in range(0,8,2):
        padre1=round(padres[i]*4)
        padre2=round(padres[i+1]*4)
        hijo1=(padre1&896)|(padre2&127)
        hijo2=(padre2&896)|(padre1&127)
        nueva.append(hijo1/4)
        nueva.append(hijo2/4)
    poblacion=nueva
print('\nFIN DE LAS 10 GENERACIONES')