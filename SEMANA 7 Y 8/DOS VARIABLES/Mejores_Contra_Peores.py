
import random
import math
def evaluar(x,y):
    return 10*math.exp(-((x-20)**2+(y-30)**2)/150)+14*math.exp(-((x-50)**2+(y-70)**2)/180)+12*math.exp(-((x-80)**2+(y-25)**2)/120)+9*math.exp(-((x-70)**2+(y-85)**2)/100)+2*math.sin(x/8)*math.cos(y/10)
def cruzar(a,b):
    a=round(a*4)
    b=round(b*4)
    hijo1=(a&448)|(b&63)
    hijo2=(b&448)|(a&63)
    return hijo1/4,hijo2/4
def mutar(valor):
    bits=round(valor*4)
    for i in range(9):
        if random.random()<0.05:
            bits=bits^(1<<i)
    return min(bits/4,100)
poblacion=[(81.5,57.75),(57.75,65.25),(65.25,78),(78,0.5),(0.5,85.25),(27.75,57.5),(57.5,25.25),(85.25,81.5)]
maximos=[]
promedios=[]
mejores=[]
random.seed(42)
for generacion in range(1,11):
    print('\nGENERACION',generacion,'- MEJORES CONTRA PEORES')
    resultados=[]
    for i in range(8):
        x,y=poblacion[i]
        valor=evaluar(x,y)
        resultados.append(valor)
        print('C'+str(i+1),'| x:',x,'| y:',y,'| Evaluacion:',round(valor,4))
    mayor=max(resultados)
    promedio=sum(resultados)/8
    ganador=resultados.index(mayor)
    mejor=poblacion[ganador]
    maximos.append(mayor)
    promedios.append(promedio)
    mejores.append(mejor)
    print('GANADOR: C'+str(ganador+1),'| x:',mejor[0],'| y:',mejor[1],'| Evaluacion:',round(mayor,4))
    print('PROMEDIO:',round(promedio,4))
    if generacion==10:
        break
    ordenados=sorted(poblacion,key=lambda p:evaluar(p[0],p[1]),reverse=True)
    nueva=[]
    for i in range(4):
        padre1=ordenados[i]
        padre2=ordenados[7-i]
        x1,x2=cruzar(padre1[0],padre2[0])
        y1,y2=cruzar(padre1[1],padre2[1])
        hijo1=(mutar(x1),mutar(y1))
        hijo2=(mutar(x2),mutar(y2))
        nueva.extend([hijo1,hijo2])
    poblacion=nueva
print('\nFIN DE LAS 10 GENERACIONES')
print('\nMAXIMOS Y PROMEDIOS POR GENERACION')
for i in range(10):
    print('Generacion',i+1,'| Maximo:',round(maximos[i],4),'| Promedio:',round(promedios[i],4))
ganador_general=maximos.index(max(maximos))
print('\nMEJOR RESULTADO GENERAL')
print('Generacion:',ganador_general+1)
print('x:',mejores[ganador_general][0])
print('y:',mejores[ganador_general][1])
print('Aptitud maxima:',round(max(maximos),4))
