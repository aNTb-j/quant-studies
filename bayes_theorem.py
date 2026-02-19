import numpy as np
import matplotlib.pyplot as plt

def bayes(prior, likelihood, evidence):
    posterior = (likelihood * prior) / evidence
    return posterior

prior = 0.01
likelihood = 0.9
evidence = 0.05

print(bayes(prior, likelihood, evidence))

from scipy.stats import norm

# Dominio
x = np.linspace(-10, 10, 1000)

# Prior
mu_prior = 0
sigma_prior = 3
prior = norm.pdf(x, mu_prior, sigma_prior)

# Likelihood (dato observado en 2)
mu_likelihood = 2
sigma_likelihood = 1
likelihood = norm.pdf(x, mu_likelihood, sigma_likelihood)

# Posterior proporcional (sin normalizar)
posterior = prior * likelihood
posterior /= np.trapezoid(posterior, x)  # Normalización

# Gráfica
plt.plot(x, prior, label="Prior")
plt.plot(x, likelihood, label="Likelihood")
plt.plot(x, posterior, label="Posterior")
plt.legend()
plt.title("Actualización Bayesiana")
plt.show()