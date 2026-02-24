import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parametros
n = 30              # tamaño de cada muestra
num_samples = 10000 # numero de muestras

# Distribucion original (NO normal)
data = np.random.exponential(scale=2, size=(num_samples, n))

# Calcular medias muestrales
sample_means = np.mean(data, axis=1)

# Graficar histograma de las medias
plt.hist(sample_means, bins=50, density=True, alpha=0.6, color='skyblue')

# Parametros teoricos segun TLC
mu = 2                     # media exponencial
sigma = 2                  # desviacion exponencial
sigma_means = sigma / np.sqrt(n)

# Dominio para normal teorica
x = np.linspace(min(sample_means), max(sample_means), 1000)
plt.plot(x, norm.pdf(x, mu, sigma_means), 'r', lw=2)

plt.title("Teorema del Limite Central")
plt.show()