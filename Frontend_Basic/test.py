import numpy as np
import matplotlib.pyplot as plt

F = np.linspace(0, 1, 1000)
n = 100

amdahl = 1 / ((1 - F) + F / n)
gustafson = (1 - F) + n * F

plt.title("Comparing Amdahl's Law vs Gustafson's Law")
plt.plot(F, amdahl, label="Amdahl's Law")
plt.plot(F, gustafson, label="Gustafson's Law")
plt.xlabel("Parallel fraction F")
plt.ylabel("Speedup")
plt.legend()
plt.grid(True)
plt.show()