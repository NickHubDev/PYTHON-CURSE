# ==========================================
# DESEMPAQUETADO DE VARIABLES
# ==========================================

# El desempaquetado permite asignar varios valores
# de una lista (o tupla) a diferentes variables
# en una sola línea.

datos = ["John", "Doe", 34]


# ==========================================
# 📌 DESEMPAQUETADO
# ==========================================

# Cada elemento de la lista se asigna en orden
# a la variable correspondiente.

nombre, apellido, edad = datos


# ==========================================
# 📌 MOSTRAR LOS VALORES
# ==========================================

print(nombre, apellido, edad)


# ==========================================
# 📌 EQUIVALENTE SIN DESEMPAQUETADO
# ==========================================

# nombre = datos[0]
# apellido = datos[1]
# edad = datos[2]


# ==========================================
# 📌 REGLA IMPORTANTE
# ==========================================

# El número de variables debe coincidir exactamente
# con el número de elementos de la lista.

# Correcto:
# nombre, apellido, edad = datos

# Incorrecto:
# nombre, apellido = datos
# ValueError: too many values to unpack