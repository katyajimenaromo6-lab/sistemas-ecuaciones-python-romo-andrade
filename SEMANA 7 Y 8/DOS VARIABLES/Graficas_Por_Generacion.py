
import matplotlib.pyplot as plt
from pathlib import Path
carpeta=Path(__file__).resolve().parent
metodos=['Élite','Aleatorio','Semental','Mejores vs Peores','Torneo','Ruleta']
datos={
'Élite':[10.4502,11.305,12.8798,11.3123,12.8798,13.363,4.3799,1.509,2.1446,2.7659],
'Aleatorio':[10.4502,12.8798,12.3985,9.4208,3.5714,12.9321,5.6952,6.8686,12.8463,7.8983],
'Semental':[10.4502,11.774,12.5127,12.5127,12.5127,13.3615,13.9138,13.9138,13.9138,13.9138],
'Mejores vs Peores':[10.4502,11.7188,9.8608,12.9424,9.8608,11.1765,7.2371,1.276,2.4889,1.7394],
'Torneo':[10.4502,10.4502,11.4542,11.7979,11.7979,13.8608,13.8608,13.9057,13.9057,13.9057],
'Ruleta':[10.4502,10.4502,10.7295,11.4922,11.4922,11.4922,11.4922,13.6367,13.6367,13.785]
}
colores=['blue','orange','green','purple','red','brown']
for generacion in range(10):
    valores=[]
    for metodo in metodos:
        valores.append(datos[metodo][generacion])
    plt.figure(figsize=(11,6))
    barras=plt.bar(metodos,valores,color=colores)
    plt.title('Manufactura Aditiva - Generación '+str(generacion+1))
    plt.xlabel('Método de selección')
    plt.ylabel('Aptitud máxima')
    plt.ylim(0,16)
    plt.xticks(rotation=20)
    for barra in barras:
        altura=barra.get_height()
        plt.text(barra.get_x()+barra.get_width()/2,altura+0.2,str(round(altura,4)),ha='center',fontsize=9)
    plt.tight_layout()
    plt.savefig(carpeta/('Generacion_'+str(generacion+1)+'.png'),dpi=300,bbox_inches='tight')
    plt.close()
generaciones=list(range(1,11))
plt.figure(figsize=(11,6))
for i in range(6):
    metodo=metodos[i]
    plt.plot(generaciones,datos[metodo],marker='o',color=colores[i],label=metodo)
plt.title('Manufactura Aditiva - Evolución general')
plt.xlabel('Generación')
plt.ylabel('Aptitud máxima')
plt.xticks(generaciones)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(carpeta/'Evolucion_general.png',dpi=300,bbox_inches='tight')
plt.show()
print('Se guardaron 11 gráficas en:',carpeta)
