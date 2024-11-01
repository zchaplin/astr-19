import numpy as np
import matplotlib.pyplot as plt

# Create some data
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) + np.cos(Y)

# Create a filled contour plot
plt.contourf(X, Y, Z, 20, cmap='RdGy')
plt.colorbar()
plt.title('Filled Contour Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()