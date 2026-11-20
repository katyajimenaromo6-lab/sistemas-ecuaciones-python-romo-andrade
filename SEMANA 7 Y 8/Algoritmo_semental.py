

def evaluar(x):
    return -2*x**2+150*x+75
def cruzar(semental,otro):
    semental=round(semental*4)
    otro=round(otro*4)
    hijo=(semental&896)|(otro&127)
    return hijo/4
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
            hijo=cruzar(semental,poblacion[i])
            nueva.append(hijo)
    poblacion=nueva
print('\nFIN DE LAS 10 GENERACIONES')
