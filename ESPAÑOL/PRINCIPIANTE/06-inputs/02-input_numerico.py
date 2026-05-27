# ==========================================
# INPUTS EN PYTHON
# ==========================================


# ==========================================
# 📌 INPUT() → SOLICITA DATOS AL USUARIO
# ==========================================

# input() muestra un mensaje en pantalla y espera
# a que el usuario escriba un valor.

numero_usuario = input("Hey, dame un número\n\n")

print(numero_usuario)

# IMPORTANTE:
# input() siempre devuelve una cadena de texto (str).


# ==========================================
# 📌 INT() → CONVIERTE TEXTO A NÚMERO ENTERO
# ==========================================

# Como input() devuelve texto, debemos convertirlo
# a entero para poder realizar operaciones matemáticas.

numero_entero = int(numero_usuario)

print(numero_entero)


# ==========================================
# 📌 OPERACIONES CON EL VALOR INTRODUCIDO
# ==========================================

# Multiplicamos el número introducido por 4.

resultado = numero_entero * 4

print(resultado)


# ==========================================
# 📌 F-STRINGS → INSERTAR VARIABLES EN TEXTO
# ==========================================

# Las f-strings permiten incluir variables dentro
# de una cadena usando llaves {}.

print(f"¡Me encanta el {resultado}!")


# ==========================================
# 📌 VERSIÓN ABREVIADA
# ==========================================

# Todo el proceso puede hacerse en una sola línea:

resultado_directo = int(input("Introduce otro número: ")) * 4

print(f"El resultado es {resultado_directo}")


# ==========================================
# 📌 RECORDATORIO IMPORTANTE
# ==========================================

# input() → Devuelve texto (str)
# int()   → Convierte texto a entero (int)
# f""     → Permite insertar variables en cadenas
#
# Ejemplo:
# numero = int(input("Número: "))
# print(f"Resultado: {numero}")