# ==========================================
# MÉTODOS DE CADENAS (STRINGS) EN PYTHON
# ==========================================

cadena_1 = "Buenas, soy John Doe."
cadena_2 = "Estoy aprendiendo Python."


# ==========================================
# 📌 DIR() → MUESTRA TODOS LOS MÉTODOS
# ==========================================

# dir() es una FUNCIÓN, no un método.
# Nos muestra todas las funciones y atributos
# disponibles para un objeto.

metodos_disponibles = dir(cadena_1)

print(metodos_disponibles)


# ==========================================
# 📌 UPPER() → CONVIERTE A MAYÚSCULAS
# ==========================================

mayusculas = cadena_1.upper()

print(mayusculas)


# ==========================================
# 📌 LOWER() → CONVIERTE A MINÚSCULAS
# ==========================================

minusculas = cadena_1.lower()

print(minusculas)


# ==========================================
# 📌 CAPITALIZE() → PRIMERA LETRA EN MAYÚSCULA
# ==========================================

capitalizada = cadena_1.capitalize()

print(capitalizada)


# ==========================================
# 📌 FIND() → BUSCA UNA COINCIDENCIA
# ==========================================

# Si encuentra el texto, devuelve su posición.
# Si no lo encuentra, devuelve -1.

posicion_j = cadena_1.find("J")

print(posicion_j)


# ==========================================
# 📌 INDEX() → BUSCA UNA COINCIDENCIA
# ==========================================

# Funciona igual que find(), pero si no encuentra
# el texto, genera un error.

posicion_a = cadena_1.index("a")

print(posicion_a)


# ==========================================
# 📌 ISNUMERIC() → ¿SOLO CONTIENE NÚMEROS?
# ==========================================

es_numerico = cadena_1.isnumeric()

print(es_numerico)


# ==========================================
# 📌 ISALPHA() → ¿SOLO CONTIENE LETRAS?
# ==========================================

# Espacios, signos de puntuación y números
# hacen que devuelva False.

es_alfabetico = cadena_1.isalpha()

print(es_alfabetico)


# ==========================================
# 📌 COUNT() → CUENTA COINCIDENCIAS
# ==========================================

cantidad_b = cadena_1.count("B")

print(cantidad_b)


# ==========================================
# 📌 LEN() → CUENTA EL TOTAL DE CARACTERES
# ==========================================

# len() es una FUNCIÓN, no un método.

longitud = len(cadena_1)

print(longitud)


# ==========================================
# 📌 STARTSWITH() → ¿EMPIEZA CON...?
# ==========================================

empieza_con_b = cadena_1.startswith("B")

print(empieza_con_b)


# ==========================================
# 📌 ENDSWITH() → ¿TERMINA CON...?
# ==========================================

termina_con_punto = cadena_1.endswith(".")

print(termina_con_punto)


# ==========================================
# 📌 REPLACE() → REEMPLAZA TEXTO
# ==========================================

cadena_reemplazada = cadena_1.replace("Buenas", "Hola")

print(cadena_reemplazada)


# ==========================================
# 📌 SPLIT() → DIVIDE LA CADENA EN UNA LISTA
# ==========================================

partes = cadena_1.split(",")

print(partes)


# ==========================================
# 📌 RECORDATORIO IMPORTANTE
# ==========================================

# MÉTODO:
# dato.metodo()

# FUNCIÓN:
# funcion(dato)