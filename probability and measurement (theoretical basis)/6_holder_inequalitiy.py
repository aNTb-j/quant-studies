import numpy as np

S0 = 100        # Precio inicial del activo en t=0
mu = 0.1        # Drift bajo la medida real P (retorno esperado anual 10%)
r = 0.05        # Tasa libre de riesgo (usada para cambio a medida neutral Q)
sigma = 0.25    # Volatilidad anual del activo
T = 1           # Horizonte temporal en años
K = 100         # Strike de la opción call
n = 200000

# Simulación bajo P
Z_normal = np.random.normal(size=n)

# Precio final del activo bajo Geometric Brownian Motion:
ST = S0 * np.exp((mu - 0.5*sigma**2)*T + sigma*np.sqrt(T)*Z_normal)
# Garantiza ST > 0 (distribución lognormal)

# Payoff
X = np.maximum(ST - K, 0)

# Densidad de cambio de medida simplificada
theta = (mu - r)/sigma
# Parámetro de Girsanov
# Ajusta el drift de mu (medida P) a r (medida Q)

Z = np.exp(-theta*Z_normal*np.sqrt(T) - 0.5*theta**2*T)
# Derivada de Radon–Nikodym:
# Z = dQ/dP
# Permite calcular E_Q[X] como E_P[XZ]


p = 2
q = 2   # porque 1/2 + 1/2 = 1

# Es la esperanza del producto bajo medida P
left = np.mean(np.abs(X * Z))

# Norma L^2 de X multiplicada por norma L^2 de Z
right = (np.mean(np.abs(X)**p)**(1/p)) * \
        (np.mean(np.abs(Z)**q)**(1/q))

print("E[|XZ|] =", left)
print("Cota Hölder =", right)
print("¿Se cumple?", left <= right)