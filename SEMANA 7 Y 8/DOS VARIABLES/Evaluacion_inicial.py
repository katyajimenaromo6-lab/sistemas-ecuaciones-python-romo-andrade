
import math
def evaluar(x,y):
    return 10*math.exp(-((x-20)**2+(y-30)**2)/150)+14*math.exp(-((x-50)**2+(y-70)**2)/180)+12*math.exp(-((x-80)**2+(y-25)**2)/120)+9*math.exp(-((x-70)**2+(y-85)**2)/100)+2*math.sin(x/8)*math.cos(y/10)
poblacion=[(81.5,57.75),(57.75,65.25),(65.25,78),(78,0.5),(0.5,85.25),(27.75,57.5),(57.5,25.25),(85.25,81.5)]
resultados=[]
print("EVALUACION DE LOS 8 CROMOSOMAS")
for i in range(8):
    x,y=poblacion[i]
    valor=evaluar(x,y)
    resultados.append(valor)
    print("C"+str(i+1),"| x:",x,"| y:",y,"| Evaluacion:",round(valor,4))
mayor=max(resultados)
ganador=resultados.index(mayor)
print("\nMEJOR CROMOSOMA")
print("C"+str(ganador+1))
print("x:",poblacion[ganador][0])
print("y:",poblacion[ganador][1])
print("Evaluacion:",round(mayor,4))
print("PROMEDIO:",round(sum(resultados)/8,4))
