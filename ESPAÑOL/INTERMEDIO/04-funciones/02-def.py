# ============================================
# FUNCIONES Y PARÁMETROS
# ============================================


# --------------------------------------------
# FUNCIÓN SIN PARÁMETROS
# --------------------------------------------

"""
Esta función no recibe datos externos.

Simplemente ejecuta el código definido
dentro de ella.
"""

def presentar():
    print("Bienvenidos a este punto de nuestro tutorial.")


presentar()


# --------------------------------------------
# FUNCIÓN CON PARÁMETROS
# --------------------------------------------

"""
Los parámetros permiten que una función
trabaje con datos diferentes cada vez
que se ejecuta.
"""

def presentar_usuario(nombre):

    print(
        f"Hola {nombre}, gracias por estar en nuestro repositorio.\n"
        "¡Eres un grande!"
    )


presentar_usuario("John Doe")


# --------------------------------------------
# FUNCIÓN CON RETURN
# --------------------------------------------

"""
return permite devolver un valor
fuera de la función.

Ese valor puede guardarse en una variable.
"""

def contraseña_de_numeros(contraseña):
    return contraseña


password = contraseña_de_numeros(2354)

print(password)