import numpy as np

# ============================================================
# 1. PARAMETROS ECONOMICOS
# ============================================================

# λ_P : intensidad de default bajo la medida real (P)
# Representa la frecuencia historica observada de defaults.
# Si λ_P = 0.2 → tiempo promedio hasta default = 5 años.
lambda_P = 1/5

# λ_Q : intensidad de default bajo la medida neutral al riesgo (Q)
# Representa la percepcion de riesgo del mercado.
# Si λ_Q > λ_P → el mercado exige prima por riesgo.
lambda_Q = 1/2

# Horizonte temporal del bono (años)
T = 3

# Tasa libre de riesgo.
# Se usa para descontar flujos bajo ausencia de arbitraje.
r = 0.03

# Recovery rate.
# Porcentaje recuperado en caso de default.
# LGD (loss given default) = 1 - R
R = 0.4

# Numero de simulaciones Monte Carlo.
# Mus simulaciones → menor error estadstico.
n_sim = 1_000_000


# ============================================================
# 2. SIMULACION DEL TIEMPO DE DEFAULT BAJO P
# ============================================================

# τ representa el tiempo hasta default.
# Se modela como variable exponencial:
#   P(τ > t) = exp(-λ_P t)
# Esto implica hazard rate constante.
tau = np.random.exponential(scale=1/lambda_P, size=n_sim)

# Interpretacion financiera:
# Estamos generando posibles futuros "reales"
# segun la frecuencia historica de default.


# ============================================================
# 3. CAMBIO DE MEDIDA: RADON–NIKODYM
# ============================================================

# Z = dQ/dP
# Es el factor que repondera cada escenario real
# para convertirlo en escenario consistente con precios de mercado.
#
# Economicamente:
# - Escenarios con default temprano reciben mayor peso si λ_Q > λ_P
# - El mercado "sobrerrepresenta" estados adversos
Z = (lambda_Q / lambda_P) * np.exp(-(lambda_Q - lambda_P) * tau)

# Teoricamente debe cumplirse:
# E_P[Z] = 1  (condicion de no arbitraje)
print("Chequeo E_P[Z]:", np.mean(Z))


# ============================================================
# 4. SPREAD DE CREDITO IMPLICITO
# ============================================================

# En modelo reducido simple:
# Spread ≈ λ_Q × LGD
#
# Representa la prima anual que el mercado exige
# por asumir riesgo de default.
spread = lambda_Q * (1 - R)

print("Spread implcito:", spread)


# ============================================================
# 5. PRECIO DE BONO CERO CUPON RIESGOSO
# ============================================================

# El bono paga 1 en T si no ocurre default antes.
# Si ocurre default antes de T → payoff = 0.
payoff = (tau > T).astype(float)

# Precio bajo medida real (P)
# No es precio de mercado, sino expectativa estadstica historica.
precio_P = np.mean(np.exp(-r*T) * payoff)

# Precio bajo medida neutral al riesgo (Q)
# Este s es el precio consistente con ausencia de arbitraje.
precio_Q = np.mean(np.exp(-r*T) * payoff * Z)

print("Precio bajo P:", precio_P)
print("Precio bajo Q:", precio_Q)