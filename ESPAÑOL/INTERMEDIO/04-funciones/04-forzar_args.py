# ============================================
# ARGUMENTOS Y PARÁMETROS
# ============================================


# --------------------------------------------
# ARGUMENTOS NOMBRADOS
# --------------------------------------------

"""
Python permite enviar argumentos
indicando directamente el nombre
del parámetro.

Esto mejora la legibilidad del código.
"""

def presentar(nombre, adjetivo):

    print(
        f"Hola {nombre}, gracias por estar en nuestro repositorio.\n"
        f"¡Eres un {adjetivo}!"
    )


presentar_resultado = presentar(
    nombre="Juan",
    adjetivo="grande"
)


# --------------------------------------------
# PARÁMETROS POR DEFECTO
# --------------------------------------------

"""
Los parámetros pueden tener
valores predeterminados.

Si no enviamos un valor,
Python utilizará el valor por defecto.
"""

def presentar_usuario(nombre, adjetivo="listo"):

    print(
        f"Hola {nombre}, gracias por estar en nuestro repositorio.\n"
        f"¡Eres un {adjetivo}!"
    )


presentar_resultado = presentar_usuario("Juan", "grande")