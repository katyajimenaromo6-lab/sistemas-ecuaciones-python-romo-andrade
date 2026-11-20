
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
def programador(x):
    return -2*x**2+150*x+75
def corredor(x):
    return -x**4+84*x**3-2628*x**2+35336*x
def evaluar(x,y):
    return 10*np.exp(-((x-20)**2+(y-30)**2)/150)+14*np.exp(-((x-50)**2+(y-70)**2)/180)+12*np.exp(-((x-80)**2+(y-25)**2)/120)+9*np.exp(-((x-70)**2+(y-85)**2)/100)+2*np.sin(x/8)*np.cos(y/10)
carpeta=Path(__file__).resolve().parent/'DOS VARIABLES'
carpeta.mkdir(exist_ok=True)
x=np.linspace(0,130,2000)
max_programador=2887.5
max_corredor=max(corredor(x))
p_programador=[14,121.5,63.75,81.5,53.25,89.75,65.25,64.5]
p_corredor=[31.75,96.5,53.25,89.5,49.5,89.75,78,65.25]
ganador_programador=46
ganador_corredor=31.75
p_dos=[(81.5,57.75),(57.75,65.25),(65.25,78),(78,0.5),(0.5,85.25),(27.75,57.5),(57.5,25.25),(85.25,81.5)]
ganador_dos=(48.5,73.0)
fig=plt.figure(figsize=(17,7))
ax1=fig.add_subplot(121)
ax1.plot(x,programador(x)/max_programador*100,color='blue',label='Programador')
ax1.plot(x,corredor(x)/max_corredor*100,color='red',label='Corredor')
ax1.scatter(p_programador,programador(np.array(p_programador))/max_programador*100,color='blue',s=35,alpha=0.5,label='Cromosomas programador')
ax1.scatter(p_corredor,corredor(np.array(p_corredor))/max_corredor*100,color='red',s=35,alpha=0.5,label='Cromosomas corredor')
ax1.scatter(ganador_programador,programador(ganador_programador)/max_programador*100,color='blue',marker='*',s=250,edgecolor='black',label='Ganador programador',zorder=5)
ax1.scatter(ganador_corredor,corredor(ganador_corredor)/max_corredor*100,color='red',marker='*',s=250,edgecolor='black',label='Ganador corredor',zorder=5)
ax1.set_title('Metodo mejores contra peores - Programador y corredor')
ax1.set_xlabel('Valor decimal del cromosoma')
ax1.set_ylabel('Evaluacion respecto al maximo (%)')
ax1.set_xlim(0,130)
ax1.set_ylim(-50,110)
ax1.grid(True)
ax1.legend(fontsize=8)
valores=np.linspace(0,100,101)
X,Y=np.meshgrid(valores,valores)
Z=evaluar(X,Y)
ax2=fig.add_subplot(122,projection='3d')
ax2.plot_surface(X,Y,Z,cmap='viridis',alpha=0.65)
for punto in p_dos:
    ax2.scatter(punto[0],punto[1],evaluar(punto[0],punto[1]),color='blue',s=35)
ax2.scatter(ganador_dos[0],ganador_dos[1],evaluar(ganador_dos[0],ganador_dos[1]),color='red',marker='*',s=250,edgecolor='black',label='Ganador dos variables')
ax2.set_title('Metodo mejores contra peores - Manufactura aditiva')
ax2.set_xlabel('Utilizacion de impresoras (x)')
ax2.set_ylabel('Capacitacion tecnica (y)')
ax2.set_zlabel('Desempeno D(x,y)')
ax2.legend(fontsize=8)
plt.tight_layout()
plt.savefig(carpeta/'Mejores_Contra_Peores_Comparacion_Completa.png',dpi=300,bbox_inches='tight')
plt.show()
print('Imagen guardada en:',carpeta/'Mejores_Contra_Peores_Comparacion_Completa.png')
