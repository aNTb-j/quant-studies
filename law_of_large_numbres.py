import numpy as np
import matplotlib.pyplot as plt

# Leyes de los grandes numeros

import random

# Ley Debil
# La Ley Debil no habla de una trayectoria especifica. Habla de probabilidades:
# para cada n fijo, la probabilidad de estar lejos de μ se hace pequeña.

def weak_law_simulation(n, epsilon=0.1, trials=1000):
    mu = 0.5
    count = 0
    
    for _ in range(trials):
        samples = [random.random() for _ in range(n)]
        mean = sum(samples) / n
        
        if abs(mean - mu) > epsilon:
            count += 1
    
    return count / trials  # aproximación de la probabilidad

for n in [10, 50, 100, 500, 1000]:
    print(n, weak_law_simulation(n))

# Ley Fuerte
# La media muestral converge a μ casi seguramente.

def strong_law(n):
    samples = [random.random() for _ in range(n)]
    running_mean = np.cumsum(samples) / np.arange(1, n+1)
    return running_mean

n = 10000
means = strong_law(n)

plt.plot(means)
plt.axhline(0.5, color='red', linestyle='--', label="Esperanza = 0.5")
plt.legend()
plt.show()

