import numpy as np

# Simulacion de retornos de dos activos financieros
# Cada vector representa retornos historicos de mercado
np.random.seed(42)

# Retornos del Activo A (por ejemplo una accion)
RA = np.random.normal(0.01, 0.05, 10000)

# Retornos del Activo B (por ejemplo otra accion)
RB = np.random.normal(0.015, 0.04, 10000)


# Retorno promedio esperado de cada activo
mean_A = np.mean(RA)
mean_B = np.mean(RB)

print("Retorno promedio A:", mean_A)
print("Retorno promedio B:", mean_B)


# Desviacion estandar = volatilidad = riesgo individual
sigma_A = np.std(RA, ddof=1)
sigma_B = np.std(RB, ddof=1)

print("Riesgo A:", sigma_A)
print("Riesgo B:", sigma_B)


# Matriz de covarianza
cov_matrix = np.cov(RA, RB)

# Covarianza entre A y B
cov_AB = cov_matrix[0, 1]

print("Covarianza A B:", cov_AB)


# CAUCHY BUNYAKOVSKY SCHWARZ
# Producto de riesgos individuales
sigma_product = sigma_A * sigma_B

print("Producto de riesgos:", sigma_product)

# Ratio de Cauchy Bunyakovsky Schwarz
# Esto es el valor absoluto de la correlacion
csb_ratio = abs(cov_AB) / sigma_product

print("Ratio Cauchy Schwarz:", csb_ratio)


# Si el ratio es cercano a 1
# Los activos se mueven casi igual
# Hay poca diversificacion

# Si el ratio es cercano a 0
# Los activos son casi independientes
# Hay mayor diversificacion

# Por teoria matematica
# Este valor nunca puede ser mayor que 1