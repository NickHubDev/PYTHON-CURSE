# ============================================
# FUNCIONES Y ARGUMENTOS
# ============================================


# --------------------------------------------
# FUNCIÓN BÁSICA
# --------------------------------------------

"""
Una función permite reutilizar código.

Los parámetros:
- a
- b

reciben los valores enviados al llamar la función.
"""

def suma(a, b):
    return a + b


resultado = suma(5, 9)

print(resultado)


# --------------------------------------------
# SUMANDO UNA LISTA MANUALMENTE
# --------------------------------------------

"""
Aquí recorremos manualmente una lista
para sumar todos sus valores.
"""

def suma_lista(lista_numeros):

    numeros_sumados = 0

    for numero in lista_numeros:
        numeros_sumados = numeros_sumados + numero

    return numeros_sumados


resultado = suma_lista([3, 12, 45])

print(resultado)


# --------------------------------------------
# FORMA MÁS ÓPTIMA Y PYTHONIC
# --------------------------------------------

"""
El operador * permite recibir múltiples
argumentos y convertirlos en una tupla.

La función integrada sum() realiza
la suma automáticamente.
"""

def suma(*numeros):
    return sum(numeros)


resultado = suma(3, 12, 45)

print(resultado)