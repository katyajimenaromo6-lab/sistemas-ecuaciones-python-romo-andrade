import time

a = int(input('valor de a: '))
b = int(input('valor de b: '))
c = int(input('valor de c: '))
d = int(input('valor de d: '))
e = int(input('valor de e: '))
f = int(input('valor de f: '))

inicio = time.perf_counter()

y = (f*a-d*c)/(e*a-d*b)
x = (c/a)-(b/a)*y

fin = time.perf_counter()

tiempo = fin-inicio

print(f'El valor de x es: {x}')
print(f'El valor de y es: {y}')
print(f'El tiempo de ejecucion es: {tiempo} segundos')