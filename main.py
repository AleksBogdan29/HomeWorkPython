import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-3, 7)
y = np.sin(x) * np.cos(x) 
plt.plot(x, y)
plt.title('График sin(x) * cos(x)')
plt.xlabel('x')
plt.ylabel('y')

plt.show()