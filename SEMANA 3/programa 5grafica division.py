import matplotlib.pyplot as plt

# Resultado de A x B^-1
x = [2, -1]
y = [-1, 1]

plt.plot(x, y, marker='o')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Gráfica de A x B^-1')
plt.grid()

plt.show()