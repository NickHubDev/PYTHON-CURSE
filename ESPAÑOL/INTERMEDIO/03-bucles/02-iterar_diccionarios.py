# ============================================
# ITERACIÓN, CONTINUE, BREAK Y COMPREHENSIONS
# ============================================

# --------------------------------------------
# RECORRIENDO DICCIONARIOS
# --------------------------------------------

diccionario = {
    "nombre": "John",
    "apellido": "Doe",
    "edad": 34
}

"""
.items() devuelve cada clave y valor del diccionario.

La forma más limpia y recomendada de recorrerlo
es desempaquetando directamente los valores.
"""
# --------------------------------------------
# VERSION PYTHON BASE
# --------------------------------------------

for datos in diccionario.items():
    key = datos[0]
    valor = datos[1]

# --------------------------------------------
# VERSION PYTHON PROFESIONAL
# --------------------------------------------

for clave, valor in diccionario.items():
    print(f"{clave}: {valor}")


# --------------------------------------------
# CONTINUE
# --------------------------------------------

marcas = ["nissan", "nike", "pepsi", "google"]

"""
continue salta la iteración actual
y continúa con la siguiente.
"""

for marca in marcas:
    if marca == "google":
        continue

    print(f"Me encanta {marca}")


# --------------------------------------------
# BREAK
# --------------------------------------------

"""
break detiene completamente el bucle.
"""

for marca in marcas:
    if marca == "pepsi":
        break

    print(f"Uso {marca}")


# --------------------------------------------
# LIST COMPREHENSION
# --------------------------------------------

"""
Las comprehensions permiten crear listas
de forma más rápida y elegante.
"""

marcas_duplicadas = [marca * 2 for marca in marcas]

print(marcas_duplicadas)