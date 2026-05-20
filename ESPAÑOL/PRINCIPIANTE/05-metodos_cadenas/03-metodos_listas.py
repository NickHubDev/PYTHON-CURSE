# ==========================================
# MÉTODOS DE LISTAS (LIST) EN PYTHON
# ==========================================

lista = [True, 34]
cadena = "hola"


# ==========================================
# 📌 LEN() → CUENTA EL NÚMERO DE ELEMENTOS
# ==========================================

# len() es una FUNCIÓN, no un método.
# Cuenta la cantidad de caracteres de una cadena
# o la cantidad de elementos de una lista.

longitud_cadena = len(cadena)
longitud_lista = len(lista)

print(longitud_cadena)  # 4
print(longitud_lista)   # 2


# ==========================================
# 📌 APPEND() → AGREGA UN ELEMENTO AL FINAL
# ==========================================

# append() modifica la lista directamente.
# No devuelve ningún valor (retorna None).

lista.append("UYUYUY")

print(lista)


# ==========================================
# 📌 INSERT() → INSERTA EN UNA POSICIÓN ESPECÍFICA
# ==========================================

# insert(indice, valor)

lista.insert(2, "TOMA MAMA")

print(lista)


# ==========================================
# 📌 EXTEND() → AGREGA VARIOS ELEMENTOS
# ==========================================

# Añade todos los elementos de otra lista.

lista.extend([True, 2026])

print(lista)


# ==========================================
# 📌 POP() → ELIMINA POR ÍNDICE
# ==========================================

# Si no se indica un índice, elimina el último elemento.
# También devuelve el elemento eliminado.

lista.pop(0)

print(lista)


# ==========================================
# 📌 REMOVE() → ELIMINA POR VALOR
# ==========================================

# Elimina la primera coincidencia del valor indicado.

lista.remove("UYUYUY")

print(lista)


# ==========================================
# 📌 POP() → ELIMINA OTRO ELEMENTO
# ==========================================

lista.pop(1)

print(lista)


# ==========================================
# 📌 SORT() → ORDENA LA LISTA
# ==========================================

# Solo funciona si todos los elementos son comparables
# entre sí (por ejemplo, todos números o todos textos).

lista_numerica = [34, 2026, 7, 100]

lista_numerica.sort()

print(lista_numerica)


# ==========================================
# 📌 SORT(REVERSE=True) → ORDENA DESCENDENTE
# ==========================================

lista_numerica.sort(reverse=True)

print(lista_numerica)


# ==========================================
# 📌 REVERSE() → INVIERTE EL ORDEN ACTUAL
# ==========================================

lista_numerica.reverse()

print(lista_numerica)


# ==========================================
# 📌 RECORDATORIO IMPORTANTE
# ==========================================

# MÉTODO:
# dato.metodo()
#
# FUNCIÓN:
# funcion(dato)
#
# Ejemplos:
# lista.append("nuevo")
# len(lista)