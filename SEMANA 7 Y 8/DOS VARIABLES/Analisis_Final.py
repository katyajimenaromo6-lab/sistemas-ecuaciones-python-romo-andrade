
import numpy as np
import matplotlib.pyplot as plt
def evaluar(x,y):
    return 10*np.exp(-((x-20)**2+(y-30)**2)/150)+14*np.exp(-((x-50)**2+(y-70)**2)/180)+12*np.exp(-((x-80)**2+(y-25)**2)/120)+9*np.exp(-((x-70)**2+(y-85)**2)/100)+2*np.sin(x/8)*np.cos(y/10)
x=np.linspace(0,100,401)
y=np.linspace(0,100,401)
X,Y=np.meshgrid(x,y)
Z=evaluar(X,Y)
maximos=[]
minimos=[]
for i in range(1,len(y)-1):
    for j in range(1,len(x)-1):
        centro=Z[i,j]
        vecinos=Z[i-1:i+2,j-1:j+2].copy()
        vecinos[1,1]=np.nan
        if centro>np.nanmax(vecinos):
            maximos.append((X[i,j],Y[i,j],centro))
        if centro<np.nanmin(vecinos):
            minimos.append((X[i,j],Y[i,j],centro))
x_mejor=49.75
y_mejor=70.0
z_mejor=evaluar(x_mejor,y_mejor)
indice=np.unravel_index(np.argmax(Z),Z.shape)
x_global=X[indice]
y_global=Y[indice]
z_global=Z[indice]
print('MAXIMOS LOCALES APROXIMADOS')
for punto in maximos:
    print('x:',round(punto[0],2),'| y:',round(punto[1],2),'| D:',round(punto[2],4))
print('\nMINIMOS LOCALES APROXIMADOS')
for punto in minimos:
    print('x:',round(punto[0],2),'| y:',round(punto[1],2),'| D:',round(punto[2],4))
print('\nMEJOR SOLUCION DEL ALGORITMO GENETICO')
print('Metodo: Semental')
print('x:',x_mejor,'| y:',y_mejor,'| D:',round(z_mejor,4))
print('\nMAXIMO ENCONTRADO EN LA CUADRICULA')
print('x:',round(x_global,2),'| y:',round(y_global,2),'| D:',round(z_global,4))
print('Diferencia de aptitud:',round(z_global-z_mejor,4))
fig=plt.figure(figsize=(12,8))
ax=fig.add_subplot(111,projection='3d')
ax.plot_surface(X,Y,Z,cmap='viridis',alpha=0.65,rstride=4,cstride=4)
for i,punto in enumerate(maximos):
    if i==0:
        ax.scatter(punto[0],punto[1],punto[2],color='orange',s=65,label='Maximos locales')
    else:
        ax.scatter(punto[0],punto[1],punto[2],color='orange',s=65)
for i,punto in enumerate(minimos):
    if i==0:
        ax.scatter(punto[0],punto[1],punto[2],color='blue',s=65,label='Minimos locales')
    else:
        ax.scatter(punto[0],punto[1],punto[2],color='blue',s=65)
ax.scatter(x_mejor,y_mejor,z_mejor,color='red',s=110,label='Mejor solucion genetica')
ax.set_title('Analisis final de la superficie de desempeno')
ax.set_xlabel('Utilizacion de impresoras (x)')
ax.set_ylabel('Capacitacion tecnica (y)')
ax.set_zlabel('Desempeno D(x,y)')
ax.legend()
plt.tight_layout()
plt.savefig('Analisis_Final_3D.png',dpi=300,bbox_inches='tight')
plt.show()
print('\nINTERPRETACION')
print('La mejor solucion genetica representa una combinacion de utilizacion de impresoras y capacitacion tecnica que produce un desempeno elevado.')
print('El modelo permite comparar combinaciones y apoyar decisiones de mejora del desempeno laboral.')
print('\nPREGUNTAS DE REFLEXION')
print('1. Una busqueda local puede quedar atrapada en un maximo local porque solo explora soluciones cercanas y puede no encontrar una montana mas alta.')
print('2. El algoritmo genetico trabaja con varias soluciones, combina sus caracteristicas y utiliza mutacion para explorar otras regiones.')
print('3. Aumentar la mutacion genera mayor variedad, pero una tasa demasiado alta puede dificultar la conservacion de buenas soluciones.')
print('4. Una empresa podria utilizar el modelo para evaluar escenarios de uso de equipos y capacitacion, antes de tomar decisiones operativas.')
