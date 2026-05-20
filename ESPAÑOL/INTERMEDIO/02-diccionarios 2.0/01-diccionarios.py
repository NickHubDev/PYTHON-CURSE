# ==========================================
# CREACIÓN AVANZADA DE DICCIONARIOS
# ==========================================


# ==========================================
# 📌 DICT() → CREAR UN DICCIONARIO CON ARGUMENTOS
# ==========================================

# Podemos crear un diccionario indicando las
# claves y valores directamente.

diccionario = dict(
    nombre="John",
    apellido="Doe"
)

print(diccionario)

# Resultado:
# {'nombre': 'John', 'apellido': 'Doe'}


# ==========================================
# 📌 USAR TUPLAS COMO CLAVES
# ==========================================

# Las tuplas pueden utilizarse como claves
# porque son inmutables.

diccionario = {
    ("John", "Doe"): "nombre_apellidos"
}

print(diccionario)

# Resultado:
# {('John', 'Doe'): 'nombre_apellidos'}


# ==========================================
# 📌 FROMKEYS() → CREAR CLAVES CON VALOR NONE
# ==========================================

# fromkeys() recibe un iterable con las claves
# y asigna None como valor por defecto.

diccionario = dict.fromkeys(
    ["nombre", "apellido", "edad", "deporte_favorito"]
)

print(diccionario)

# Resultado:
# {
#     'nombre': None,
#     'apellido': None,
#     'edad': None,
#     'deporte_favorito': None
# }


# ==========================================
# 📌 CLEAR() → ELIMINAR TODO EL CONTENIDO
# ==========================================

# clear() modifica el diccionario directamente.
# No devuelve ningún valor (retorna None).

diccionario.clear()

print(diccionario)

# Resultado:
# {}


# ==========================================
# 📌 FROMKEYS() CON VALOR PERSONALIZADO
# ==========================================

# También podemos indicar un valor inicial
# para todas las claves.

diccionario = dict.fromkeys(
    ["nombre", "apellido", "edad", "deporte_favorito"],
    "Unknown"
)

print(diccionario)

# Resultado:
# {
#     'nombre': 'Unknown',
#     'apellido': 'Unknown',
#     'edad': 'Unknown',
#     'deporte_favorito': 'Unknown'
# }


# ==========================================
# 📌 RECORDATORIO IMPORTANTE
# ==========================================

# dict()           → Crea un diccionario.
# dict.fromkeys()  → Crea varias claves de una vez.
# clear()          → Vacía el diccionario.
#
# Las tuplas pueden utilizarse como claves
# porque son inmutables.