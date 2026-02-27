import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2   # Funcion convexa

# Simulamos variable aleatoria
n = 100000
X = np.random.normal(loc=0, scale=2, size=n)

left_side = f(np.mean(X))        # f(E[X])
right_side = np.mean(f(X))       # E[f(X)]

print("f(E[X])  =", left_side)
print("E[f(X)]  =", right_side)

print("¿Se cumple Jensen?", left_side <= right_side)

x_vals = np.linspace(min(X), max(X), 1000)

plt.plot(x_vals, f(x_vals), label="f(x) = x²")
plt.scatter(np.mean(X), f(np.mean(X)), color="red", label="f(E[X])")
plt.axhline(right_side, color="green", linestyle="--", label="E[f(X)]")

plt.legend()
plt.title("Verificación Visual de la Desigualdad de Jensen")
plt.show()



# Parametros
S0 = 100        # Precio inicial del activo en t=0
mu = 0.10       # Tasa de crecimiento esperada anual
sigma = 0.30    # Volatilidad anual (30%)
T = 5           # Horizonte temporal en años

Z = np.random.normal(size=n)

# Precio final (GBM)
ST = S0 * np.exp((mu - 0.5*sigma**2)*T + sigma*np.sqrt(T)*Z)

# Retorno simple
R = (ST - S0) / S0

# Jensen aplicado
left = np.mean(np.log(ST / S0))      # E[log crecimiento]
right = np.log(np.mean(ST / S0))     # log(E[crecimiento])

print("E[log crecimiento] =", left)
print("log(E[crecimiento]) =", right)

print("¿Se cumple Jensen?", left <= right)
