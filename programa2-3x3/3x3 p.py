import time

a = int(input('valor de a: '))
b = int(input('valor de b: '))
c = int(input('valor de c: '))
d = int(input('valor de d: '))

e = int(input('valor de e: '))
f = int(input('valor de f: '))
g = int(input('valor de g: '))
h = int(input('valor de h: '))

i = int(input('valor de i: '))
j = int(input('valor de j: '))
k = int(input('valor de k: '))
lam = int(input('valor de lambda: '))

inicio = time.perf_counter()

z = ((a*lam-i*d)*(a*f-e*b)-(a*j-i*b)*(a*h-e*d))/((a*k-i*c)*(a*f-e*b)-(a*j-i*b)*(a*g-e*c))

y = (a*h-e*d-(a*g-e*c)*z)/(a*f-e*b)

x = (d-b*y-c*z)/a

fin = time.perf_counter()

tiempo = fin-inicio

print(f'El valor de x es: {x}')
print(f'El valor de y es: {y}')
print(f'El valor de z es: {z}')
print(f'El tiempo de ejecucion es: {tiempo} segundos')
