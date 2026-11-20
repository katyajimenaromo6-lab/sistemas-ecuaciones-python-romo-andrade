
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,100,201)
y=np.linspace(0,100,201)
X,Y=np.meshgrid(x,y)
D=10*np.exp(-((X-20)**2+(Y-30)**2)/150)+14*np.exp(-((X-50)**2+(Y-70)**2)/180)+12*np.exp(-((X-80)**2+(Y-25)**2)/120)+9*np.exp(-((X-70)**2+(Y-85)**2)/100)+2*np.sin(X/8)*np.cos(Y/10)
fig=plt.figure(figsize=(11,7))
ax=fig.add_subplot(111,projection='3d')
superficie=ax.plot_surface(X,Y,D,cmap='viridis',edgecolor='none')
ax.set_title('Desempeño del ingeniero de manufactura aditiva')
ax.set_xlabel('Utilizacion de impresoras (x)')
ax.set_ylabel('Capacitacion tecnica (y)')
ax.set_zlabel('Desempeño D(x,y)')
fig.colorbar(superficie,ax=ax,shrink=0.6,label='Desempeño')
plt.savefig("Superficie_3D.png",dpi=300,bbox_inches="tight")
plt.show()
