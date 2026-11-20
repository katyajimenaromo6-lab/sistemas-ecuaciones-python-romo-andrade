
import random
def evaluar(x):
    return -x**4+84*x**3-2628*x**2+35336*x
def torneo(poblacion):
    participantes=random.sample(poblacion,2)
    ganador=max(participantes,key=evaluar)
    return ganador
poblacion=[81.5,57.75,65.25,78,0.5,127.75,57.5,85.25]
mejor_total=None
for generacion in range(1,11):
    print('\nGENERACION',generacion,'- TORNEO CORREDOR')
    resultados=[]
    for i in range(8):
        x=poblacion[i]
        valor=evaluar(x)
        resultados.append(valor)
        print('C'+str(i+1),'| Decimal:',x,'| Evaluacion:',valor)
    mayor=max(resultados)
    ganador=resultados.index(mayor)
    mejor=poblacion[ganador]
    print('GANADOR: C'+str(ganador+1),'| Decimal:',mejor,'| Evaluacion:',mayor)
    if mejor_total is None or evaluar(mejor)>evaluar(mejor_total):
        mejor_total=mejor
    if generacion==10:
        break
    nueva=[mejor]
    while len(nueva)<8:
        padre1=round(torneo(poblacion)*4)
        padre2=round(torneo(poblacion)*4)
        hijo1=(padre1&896)|(padre2&127)
        hijo2=(padre2&896)|(padre1&127)
        nueva.append(hijo1/4)
        if len(nueva)<8:
            nueva.append(hijo2/4)
    poblacion=nueva
print('\nFIN DE LAS 10 GENERACIONES')
print('MEJOR RESULTADO GENERAL')
print('Decimal:',mejor_total)
print('Evaluacion:',evaluar(mejor_total))
