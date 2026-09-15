import matplotlib.pyplot as plt

# Primera matriz
x1 = [1, 3]
y1 = [2, 4]

plt.plot(x1, y1, marker='o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Primera matriz')
plt.grid()
plt.show()


# Segunda matriz
x2 = [5, 7]
y2 = [6, 8]

plt.plot(x2, y2, marker='o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Segunda matriz')
plt.grid()
plt.show()


# Matriz suma
x3 = [6, 10]
y3 = [8, 12]

plt.plot(x3, y3, marker='o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Matriz suma')
plt.grid()
plt.show()


# Las tres matrices juntas
plt.plot(x1, y1, marker='o', label='Primera matriz')
plt.plot(x2, y2, marker='o', label='Segunda matriz')
plt.plot(x3, y3, marker='o', label='Matriz suma')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Comparación de las tres matrices')
plt.grid()
plt.legend()

plt.show()