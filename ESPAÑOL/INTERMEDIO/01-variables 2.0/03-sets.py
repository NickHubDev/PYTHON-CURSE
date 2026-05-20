# ==========================================
# SETS Y FROZENSETS EN PYTHON
# ==========================================


# ==========================================
# 📌 SET() → CREA UN CONJUNTO
# ==========================================

# Los sets:
# - No permiten elementos duplicados.
# - No mantienen un orden fijo.
# - Son muy útiles para operaciones matemáticas.

conjunto = set(["dato1", "dato2"])

print(conjunto)


# ==========================================
# 📌 FROZENSET() → CREA UN CONJUNTO INMUTABLE
# ==========================================

# Un frozenset no puede modificarse después de crearse.
# Gracias a esto, puede almacenarse dentro de otros sets.

conjunto_inmutable = frozenset(["dato1", "dato2"])

conjunto_con_anidacion = {
    conjunto_inmutable,
    "dato3"
}

print(conjunto_con_anidacion)


# ==========================================
# 📌 CONJUNTOS PARA COMPARACIÓN
# ==========================================

conjunto_principal = {1, 3, 5, 8}
conjunto_secundario = {1, 3, 8}


# ==========================================
# 📌 ISSUBSET() → ¿ES UN SUBCONJUNTO?
# ==========================================

# Devuelve True si todos los elementos del
# conjunto_secundario están dentro del conjunto_principal.

es_subconjunto = conjunto_secundario.issubset(conjunto_principal)

print(es_subconjunto)


# ==========================================
# 📌 ISSUPERSET() → ¿ES UN SUPERCONJUNTO?
# ==========================================

# Devuelve True si el conjunto_secundario contiene
# todos los elementos del conjunto_principal.

es_superconjunto = conjunto_secundario.issuperset(conjunto_principal)

print(es_superconjunto)


# ==========================================
# 📌 ISDISJOINT() → ¿NO COMPARTEN ELEMENTOS?
# ==========================================

# Devuelve True si ambos conjuntos no tienen
# ningún elemento en común.

son_disjuntos = conjunto_secundario.isdisjoint(conjunto_principal)

print(son_disjuntos)