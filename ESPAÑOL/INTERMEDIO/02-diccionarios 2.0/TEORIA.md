# 🗂️ Diccionarios 2.0

## ¿Qué es un diccionario?

Un diccionario (`dict`) almacena pares `clave: valor`.

```python
persona = {
    "nombre": "Nicky",
    "edad": 20
}
```

---

# 🔍 Acceso seguro

```python
print(persona.get("nombre"))
print(persona.get("ciudad", "No especificada"))
```

---

# 🔄 Recorrido avanzado

```python
for clave, valor in persona.items():
    print(clave, valor)
```

---

# 🧱 Diccionarios anidados

```python
usuario = {
    "nombre": "Nicky",
    "direccion": {
        "ciudad": "Madrid",
        "pais": "España"
    }
}
```

---

# 📚 Comprensión de diccionarios

```python
cuadrados = {x: x**2 for x in range(5)}
```

Resultado:

```python
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

---

# 🔧 Métodos importantes

```python
persona.keys()
persona.values()
persona.items()
persona.update({"profesion": "Programador"})
persona.pop("edad")
```

---

# 🧠 Casos de uso reales

- JSON y APIs.
- Configuración de aplicaciones.
- Datos estructurados.
- Sistemas de caché.

---

# ⚡ Diccionarios vs Listas

| Estructura | Acceso |
|----------|----------|
| Lista | Por índice |
| Diccionario | Por clave |

Los diccionarios permiten búsquedas rápidas y semánticas.

---

# 📝 Ejercicio propuesto

Crear un diccionario con información personal y mostrar todos sus datos con un bucle `for`.

---

# 🎯 Resumen

Los diccionarios avanzados permiten modelar datos complejos de forma natural y son fundamentales en backend, APIs y desarrollo profesional con Python.

