
import matplotlib.pyplot as plt
generaciones=list(range(1,11))
maximos={
'Élite':[10.4502,11.305,12.8798,11.3123,12.8798,13.363,4.3799,1.509,2.1446,2.7659],
'Aleatorio':[10.4502,12.8798,12.3985,9.4208,3.5714,12.9321,5.6952,6.8686,12.8463,7.8983],
'Semental':[10.4502,11.774,12.5127,12.5127,12.5127,13.3615,13.9138,13.9138,13.9138,13.9138],
'Mejores contra peores':[10.4502,11.7188,9.8608,12.9424,9.8608,11.1765,7.2371,1.276,2.4889,1.7394],
'Torneo':[10.4502,10.4502,11.4542,11.7979,11.7979,13.8608,13.8608,13.9057,13.9057,13.9057],
'Ruleta':[10.4502,10.4502,10.7295,11.4922,11.4922,11.4922,11.4922,13.6367,13.6367,13.785]
}
promedios={
'Élite':[1.9908,2.4678,3.2157,3.0028,2.7898,2.3539,0.3435,0.3591,0.4685,0.5004],
'Aleatorio':[1.9908,2.2792,3.7305,3.5708,1.086,3.5221,1.1998,1.5596,1.7825,0.7262],
'Semental':[1.9908,8.3803,11.0499,8.13,7.5784,10.4837,9.1448,10.259,9.7348,7.7014],
'Mejores contra peores':[1.9908,2.5352,1.8953,2.7931,2.0323,2.8928,1.331,0.2315,0.1749,0.4021],
'Torneo':[1.9908,5.3099,7.6518,8.5792,9.1913,9.8122,12.1124,11.1127,11.5803,13.3889],
'Ruleta':[1.9908,2.5542,5.299,8.3519,6.5881,8.7448,5.3886,7.3833,6.2931,10.9501]
}
plt.figure(figsize=(11,6))
for metodo,valores in maximos.items():
    plt.plot(generaciones,valores,marker='o',label=metodo)
plt.title('Comparación de aptitud máxima')
plt.xlabel('Generación')
plt.ylabel('Aptitud máxima')
plt.xticks(generaciones)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('Comparacion_Aptitud_Maxima.png',dpi=300)
plt.show()
plt.figure(figsize=(11,6))
for metodo,valores in promedios.items():
    plt.plot(generaciones,valores,marker='o',label=metodo)
plt.title('Comparación de aptitud promedio')
plt.xlabel('Generación')
plt.ylabel('Aptitud promedio')
plt.xticks(generaciones)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('Comparacion_Aptitud_Promedio.png',dpi=300)
plt.show()
