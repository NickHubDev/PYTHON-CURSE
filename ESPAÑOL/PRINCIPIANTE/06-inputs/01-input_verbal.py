# ==========================================
# PRÁCTICA DE INPUTS EN PYTHON
# ==========================================

# En este ejemplo utilizaremos input() para pedir
# el nombre del usuario y después mostraremos
# un mensaje personalizado.


# ==========================================
# 📌 GUARDAR EL TEXTO INTRODUCIDO POR EL USUARIO
# ==========================================

nombre_usuario = input("Hey, dime tu nombre!\n")


# ==========================================
# 📌 F-STRINGS → INSERTAR VARIABLES EN TEXTO
# ==========================================

# Las f-strings permiten incluir el valor de una
# variable dentro de una cadena usando llaves {}.

print(f"\n¡Genial! Un placer conocerte {nombre_usuario}")


# ==========================================
# 📌 EJEMPLO DE SALIDA
# ==========================================

# Si el usuario escribe:
# John
#
# El programa mostrará:
#
# ¡Genial! Un placer conocerte John