# ============================================
# ITERACIÓN AVANZADA
# ============================================

animales = ["gato", "perro", "loro", "cocodrilo"]
numeros = [52, 84, 85]


# --------------------------------------------
# ITERACIÓN BÁSICA
# --------------------------------------------

"""
En cada vuelta del bucle, la variable 'animal'
tomará el valor del siguiente elemento.
"""

for animal in animales:
    print(f"Ahora la variable animal es igual a {animal}")


# --------------------------------------------
# ZIP()
# --------------------------------------------

"""
zip() combina múltiples colecciones.

En cada iteración:
- animal obtiene un valor de animales
- numero obtiene un valor de numeros

IMPORTANTE:
zip() se detiene cuando la colección más corta termina.
"""

for animal, numero in zip(animales, numeros):
    print(f"Animal: {animal}")
    print(f"Número: {numero}")


# --------------------------------------------
# ENUMERATE()
# --------------------------------------------

"""
enumerate() añade automáticamente un índice
a cada elemento de la colección.
"""

# --------------------------------------------
# VERSION PYTHON BASE
# --------------------------------------------

for datos in enumerate(numeros):
    indice = datos[0]
    valor = datos[1]

    print(f"{indice} ; {valor}")


# --------------------------------------------
# VERSION PYTHON PROFESIONAL
# --------------------------------------------

for indice, valor in enumerate(numeros):
    print(f"{indice} ; {valor}")