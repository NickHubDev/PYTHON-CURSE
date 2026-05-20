# 🧵 Métodos de Cadenas y Colecciones

## ¿Qué es un método?

Un método es una función que pertenece a un objeto y se ejecuta usando la sintaxis:

```python
objeto.metodo()
```

En Python, las cadenas (`str`), listas (`list`) y diccionarios (`dict`) incluyen muchos métodos útiles.

---

# 🔤 Métodos de Cadenas (`str`)

Las cadenas son inmutables, por lo que los métodos devuelven una nueva cadena.

## Transformación

```python
texto = "hola mundo"

print(texto.upper())      # HOLA MUNDO
print(texto.lower())      # hola mundo
print(texto.capitalize()) # Hola mundo
print(texto.title())      # Hola Mundo
```

## Búsqueda

```python
texto = "Python es increíble"

print(texto.find("es"))      # 7
print(texto.startswith("Py")) # True
print(texto.endswith("ble"))  # True
```

## Reemplazo

```python
print(texto.replace("increíble", "potente"))
```

## División y unión

```python
palabras = texto.split(" ")
print("-".join(palabras))
```

## Eliminación de espacios

```python
nombre = "   Nicky   "
print(nombre.strip())
```

---

# 📋 Métodos de Listas (`list`)

```python
numeros = [1, 2, 3]
```

```python
numeros.append(4)
numeros.extend([5, 6])
numeros.insert(0, 0)
numeros.remove(3)
ultimo = numeros.pop()
numeros.sort()
numeros.reverse()
```

---

# 📚 Métodos de Diccionarios (`dict`)

```python
persona = {"nombre": "Nicky", "edad": 20}
```

```python
print(persona.keys())
print(persona.values())
print(persona.items())
print(persona.get("nombre"))
persona.update({"ciudad": "Madrid"})
edad = persona.pop("edad")
```

---

# 🧠 Cuándo usar métodos

- Limpiar texto.
- Manipular listas dinámicas.
- Consultar y actualizar diccionarios.
- Preparar datos para APIs y bases de datos.

---

# ⚠️ Buenas prácticas

- Usa `get()` para evitar errores con claves inexistentes.
- Usa `strip()` al procesar entradas del usuario.
- Recuerda que las cadenas no se modifican en sitio.

---

# 📝 Ejercicio propuesto

Pide un texto al usuario y muestra:

1. En mayúsculas.
2. Número de palabras.
3. Primera palabra.
4. Palabras unidas con `-`.

---

# 🎯 Resumen

Los métodos permiten trabajar de forma eficiente con datos. Dominar los métodos de `str`, `list` y `dict` es esencial para escribir código limpio y profesional.

