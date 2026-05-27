# ==========================================
# TUPLAS (TUPLE) EN PYTHON
# ==========================================

# Las tuplas son estructuras de datos:
# - Ordenadas.
# - Inmutables (no pueden modificarse).
# - Capaces de almacenar distintos tipos de datos.


# ==========================================
# 📌 TUPLE() → CREAR UNA TUPLA DESDE UNA LISTA
# ==========================================

tupla = tuple(["dato1", "dato2"])

print(tupla)

# Resultado:
# ('dato1', 'dato2')


# ==========================================
# 📌 CREACIÓN DIRECTA DE UNA TUPLA
# ==========================================

# No es necesario usar tuple().
# Basta con separar los elementos con comas.

tupla = "dato1", "dato2"

print(tupla)

# Resultado:
# ('dato1', 'dato2')


# ==========================================
# 📌 UNA CADENA NO ES UNA TUPLA
# ==========================================

# Sin coma final, Python interpreta el valor
# como una cadena de texto normal.

texto = "dato"

print(texto)

# Resultado:
# dato


# ==========================================
# 📌 TUPLA DE UN SOLO ELEMENTO
# ==========================================

# Para crear una tupla con un único elemento,
# es obligatorio añadir una coma al final.

tupla_un_elemento = "dato",

print(tupla_un_elemento)

# Resultado:
# ('dato',)


# ==========================================
# 📌 REGLA IMPORTANTE
# ==========================================

# La coma es lo que realmente crea la tupla,
# no los paréntesis.

# Ejemplos:
#
# "dato"     -> str
# "dato",    -> tuple
# ("dato",)  -> tuple