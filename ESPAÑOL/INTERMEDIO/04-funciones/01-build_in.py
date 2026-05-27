# ============================================
# FUNCIONES INTEGRADAS DE PYTHON
# ============================================

numeros = [12, 34, 122, 87]


# --------------------------------------------
# MAX()
# --------------------------------------------

"""
max() devuelve el valor más alto
de una colección.
"""

max_numero = max(numeros)

print(max_numero)


# --------------------------------------------
# MIN()
# --------------------------------------------

"""
min() devuelve el valor más pequeño
de una colección.
"""

min_numero = min(numeros)

print(min_numero)


# --------------------------------------------
# ROUND()
# --------------------------------------------

"""
round() redondea un número decimal.

El segundo parámetro indica
la cantidad de decimales.
"""

numero_redondeado = round(15.67128, 3)

print(numero_redondeado)


# --------------------------------------------
# BOOL()
# --------------------------------------------

"""
bool() convierte un valor a True o False.

Python considera vacías como False:
- listas vacías
- strings vacíos
- diccionarios vacíos
- 0
- None
"""

check_resultado = bool([12, 43])

print(check_resultado)


# --------------------------------------------
# ALL()
# --------------------------------------------

"""
all() devuelve True únicamente
si TODOS los valores son verdaderos.
"""

check_all = all([23, 56])

print(check_all)


# --------------------------------------------
# SUM()
# --------------------------------------------

"""
sum() suma todos los elementos
de una colección numérica.
"""

suma_total = sum(numeros)

print(suma_total)