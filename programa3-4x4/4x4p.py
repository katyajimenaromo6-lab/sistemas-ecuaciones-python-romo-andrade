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
L = int(input('valor de l: '))
m = int(input('valor de m: '))
n = int(input('valor de n: '))
o = int(input('valor de o: '))

p = int(input('valor de p: '))
q = int(input('valor de q: '))
r = int(input('valor de r: '))
s = int(input('valor de s: '))
t = int(input('valor de t: '))

inicio = time.perf_counter()

w = (((a*t-p*e)*(a*g-f*b)-(a*q-p*b)*(a*j-f*e))*((a*m-k*c)*(a*g-f*b)-(a*L-k*b)*(a*h-f*c))-((a*r-p*c)*(a*g-f*b)-(a*q-p*b)*(a*h-f*c))*((a*o-k*e)*(a*g-f*b)-(a*L-k*b)*(a*j-f*e)))/(((a*s-p*d)*(a*g-f*b)-(a*q-p*b)*(a*i-f*d))*((a*m-k*c)*(a*g-f*b)-(a*L-k*b)*(a*h-f*c))-((a*r-p*c)*(a*g-f*b)-(a*q-p*b)*(a*h-f*c))*((a*n-k*d)*(a*g-f*b)-(a*L-k*b)*(a*i-f*d)))

z = ((a*o-k*e)*(a*g-f*b)-(a*L-k*b)*(a*j-f*e)-((a*n-k*d)*(a*g-f*b)-(a*L-k*b)*(a*i-f*d))*w)/((a*m-k*c)*(a*g-f*b)-(a*L-k*b)*(a*h-f*c))

y = (a*j-f*e-(a*h-f*c)*z-(a*i-f*d)*w)/(a*g-f*b)

x = (e-b*y-c*z-d*w)/a

fin = time.perf_counter()

tiempo = fin-inicio

print(f'El valor de x es: {x}')
print(f'El valor de y es: {y}')
print(f'El valor de z es: {z}')
print(f'El valor de w es: {w}')
print(f'El tiempo de ejecucion es: {tiempo} segundos')
