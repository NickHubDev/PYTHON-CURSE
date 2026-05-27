# ==========================================
# MÉTODOS DE DICCIONARIOS (DICT) EN PYTHON
# ==========================================

persona = {
    "nombre": "John",
    "apellido": "Doe",
    "edad": 34
}


# ==========================================
# 📌 KEYS() → OBTIENE TODAS LAS CLAVES
# ==========================================

claves = persona.keys()

print(claves)

# Resultado:
# dict_keys(['nombre', 'apellido', 'edad'])


# ==========================================
# 📌 GET() → OBTIENE EL VALOR DE UNA CLAVE
# ==========================================

# Si la clave no existe, devuelve None
# en lugar de generar un error.

nombre = persona.get("nombre")

print(nombre)

# Resultado:
# John


# ==========================================
# 📌 POP() → ELIMINA UNA CLAVE Y DEVUELVE SU VALOR
# ==========================================

valor_eliminado = persona.pop("nombre")

print(valor_eliminado)
print(persona)

# Resultado:
# John
# {'apellido': 'Doe', 'edad': 34}


# ==========================================
# 📌 ITEMS() → OBTIENE CLAVES Y VALORES
# ==========================================

# Devuelve un objeto iterable con tuplas:
# (clave, valor)

elementos = persona.items()

print(elementos)

# Resultado:
# dict_items([('apellido', 'Doe'), ('edad', 34)])


# ==========================================
# 📌 CLEAR() → ELIMINA TODO EL DICCIONARIO
# ==========================================

persona.clear()

print(persona)

# Resultado:
# {}


# ==========================================
# 📌 RECORDATORIO IMPORTANTE
# ==========================================

# Estructura de un diccionario:
#
# {
#     "clave": valor
# }
#
# Estructura de un método:
#
# dato.metodo()
#
# Ejemplo:
# persona.keys()