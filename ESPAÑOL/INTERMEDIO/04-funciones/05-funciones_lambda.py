# ============================================
# LAMBDAS Y FILTER()
# ============================================

numeros = [2, 4, 5, 6, 29, 385, 12]


# --------------------------------------------
# FUNCIONES LAMBDA
# --------------------------------------------

"""
Una lambda es una función anónima.

Se utiliza normalmente para operaciones
pequeñas y rápidas.
"""

multiplicar_por_doce = lambda numero: numero * 12

print(multiplicar_por_doce(2))


# --------------------------------------------
# FILTER()
# --------------------------------------------

"""
filter() filtra elementos de una colección.

Solo conservará los elementos donde
la función devuelva True.
"""

def es_par(numero):

    if numero % 2 == 0:
        return True

    return False


numeros_pares = filter(es_par, numeros)

print(list(numeros_pares))