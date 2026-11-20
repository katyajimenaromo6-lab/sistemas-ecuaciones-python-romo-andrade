
import random
import os
import matplotlib.pyplot as plt
def programador(x):
    return -2*x**2+150*x+75
def corredor(x):
    return -x**4+84*x**3-2628*x**2+35336*x
def cruzar(a,b):
    a=round(a*4)
    b=round(b*4)
    hijo1=((a&896)|(b&127))/4
    hijo2=((b&896)|(a&127))/4
    return hijo1,hijo2
def torneo(poblacion,evaluar):
    participantes=random.sample(poblacion,2)
    return max(participantes,key=evaluar)
def ruleta(poblacion,evaluar):
    valores=[evaluar(x) for x in poblacion]
    minimo=min(valores)
    pesos=[valor-minimo+1 for valor in valores]
    return random.choices(poblacion,weights=pesos,k=1)[0]
def ejecutar(metodo,evaluar):
    poblacion=[81.5,57.75,65.25,78,0.5,127.75,57.5,85.25]
    maximos=[]
    for generacion in range(1,11):
        mejor=max(poblacion,key=evaluar)
        maximos.append(evaluar(mejor))
        if generacion==10:
            break
        nueva=[]
        if metodo=="Elite":
            ordenados=sorted(poblacion,key=evaluar,reverse=True)
            for i in range(0,8,2):
                hijo1,hijo2=cruzar(ordenados[i],ordenados[i+1])
                nueva.extend([hijo1,hijo2])
        elif metodo=="Aleatorio":
            padres=poblacion.copy()
            random.shuffle(padres)
            for i in range(0,8,2):
                hijo1,hijo2=cruzar(padres[i],padres[i+1])
                nueva.extend([hijo1,hijo2])
        elif metodo=="Semental":
            nueva=[mejor]
            for i,x in enumerate(poblacion):
                if len(nueva)==8:
                    break
                if i==poblacion.index(mejor):
                    continue
                hijo1,hijo2=cruzar(mejor,x)
                nueva.append(hijo1)
        elif metodo=="Mejores vs peores":
            ordenados=sorted(poblacion,key=evaluar,reverse=True)
            for i in range(4):
                hijo1,hijo2=cruzar(ordenados[i],ordenados[7-i])
                nueva.extend([hijo1,hijo2])
        elif metodo=="Torneo":
            nueva=[mejor]
            while len(nueva)<8:
                padre1=torneo(poblacion,evaluar)
                padre2=torneo(poblacion,evaluar)
                hijo1,hijo2=cruzar(padre1,padre2)
                nueva.append(hijo1)
                if len(nueva)<8:
                    nueva.append(hijo2)
        elif metodo=="Ruleta":
            nueva=[mejor]
            while len(nueva)<8:
                padre1=ruleta(poblacion,evaluar)
                padre2=ruleta(poblacion,evaluar)
                hijo1,hijo2=cruzar(padre1,padre2)
                nueva.append(hijo1)
                if len(nueva)<8:
                    nueva.append(hijo2)
        poblacion=nueva
    return maximos
metodos=["Elite","Aleatorio","Semental","Mejores vs peores","Torneo","Ruleta"]
colores=["blue","orange","green","purple","red","brown"]
random.seed(42)
for nombre,evaluar in [("Programador",programador),("Corredor",corredor)]:
    carpeta="Graficas_"+nombre
    os.makedirs(carpeta,exist_ok=True)
    resultados={}
    for metodo in metodos:
        resultados[metodo]=ejecutar(metodo,evaluar)
    print("\nRESULTADOS DEL",nombre.upper())
    for generacion in range(10):
        print("\nGENERACION",generacion+1)
        for metodo in metodos:
            print(metodo,":",resultados[metodo][generacion])
    for generacion in range(10):
        valores=[resultados[metodo][generacion] for metodo in metodos]
        plt.figure(figsize=(11,6))
        barras=plt.bar(metodos,valores,color=colores)
        plt.title(nombre+" - Generacion "+str(generacion+1))
        plt.xlabel("Metodo de seleccion")
        plt.ylabel("Evaluacion maxima")
        plt.xticks(rotation=20,ha="right")
        plt.axhline(0,color="black",linewidth=0.8)
        plt.grid(axis="y",alpha=0.3)
        for barra,valor in zip(barras,valores):
            plt.annotate(f"{valor:,.1f}",(barra.get_x()+barra.get_width()/2,valor),xytext=(0,4 if valor>=0 else -12),textcoords="offset points",ha="center",fontsize=8)
        plt.tight_layout()
        plt.savefig(carpeta+"/Generacion_"+str(generacion+1)+".png",dpi=300)
        plt.close()
    plt.figure(figsize=(11,6))
    for metodo,color in zip(metodos,colores):
        plt.plot(range(1,11),resultados[metodo],marker="o",label=metodo,color=color)
    plt.title(nombre+" - Evolucion de los seis metodos")
    plt.xlabel("Generacion")
    plt.ylabel("Evaluacion maxima")
    plt.xticks(range(1,11))
    plt.legend()
    plt.grid(True,alpha=0.3)
    plt.tight_layout()
    plt.savefig(carpeta+"/Evolucion_general.png",dpi=300)
    plt.close()
    print("\nGRAFICAS GUARDADAS EN:",carpeta)
print("\nPROGRAMA FINALIZADO")
