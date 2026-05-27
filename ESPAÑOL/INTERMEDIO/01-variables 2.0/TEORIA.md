# 📦 Variables 2.0: Tuplas, Sets y Desempaquetado

## 🎯 Objetivo

En esta sección se introducen estructuras y técnicas más avanzadas para trabajar con variables y colecciones.

---

# 🔒 Tuplas (`tuple`)

Las tuplas son colecciones ordenadas e inmutables.

```python
coordenadas = (10, 20)
```

## Características

- Mantienen el orden.
- Permiten elementos repetidos.
- No pueden modificarse.

## Uso típico

- Coordenadas.
- Configuraciones.
- Valores constantes.

---

# 🧩 Desempaquetado

Permite asignar múltiples valores en una sola línea.

```python
datos = ["John", "Doe", 34]

nombre, apellido, edad = datos
```

Muy útil al trabajar con funciones y estructuras complejas.

---

# 🧮 Sets (`set`)

Los sets son colecciones desordenadas de elementos únicos.

```python
numeros = {1, 2, 3}
```

## Características

- No permiten duplicados.
- Muy rápidos para búsquedas.
- Soportan operaciones matemáticas de conjuntos.

---

# ❄️ `frozenset`

Versión inmutable de un set.

```python
fs = frozenset(["dato1", "dato2"])
```

Puede utilizarse como elemento dentro de otros sets.

---

# ➗ Operaciones de conjuntos

```python
a = {1, 2, 3}
b = {2, 3}

print(b.issubset(a))    # True
print(a.issuperset(b))  # True
print(a | b)            # Unión
print(a & b)            # Intersección
print(a - b)            # Diferencia
```

---

# 🧠 Casos de uso

- Eliminar duplicados.
- Verificar pertenencia.
- Comparar colecciones.
- Procesar datos eficientemente.

---

# 📝 Ejercicio propuesto

Crear dos sets y mostrar:

1. Unión.
2. Intersección.
3. Diferencia.
4. Si uno es subconjunto del otro.

---

# 🎯 Resumen

Esta sección introduce herramientas muy potentes:

- `tuple` para datos inmutables.
- `set` para elementos únicos.
- `frozenset` para conjuntos inmutables.
- Desempaquetado para código más limpio.


