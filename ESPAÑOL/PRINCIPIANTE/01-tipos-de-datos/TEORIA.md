# 📦 TIPOS DE DATOS EN PYTHON

> Los tipos de datos son la base de cualquier programa.  
> Gracias a ellos, Python puede entender qué tipo de información estás utilizando.

---

# 📖 ¿Qué es un tipo de dato?

Un tipo de dato define el tipo de valor que almacena una variable.

Por ejemplo:

- Texto
- Números
- Valores verdaderos o falsos
- Conjuntos de datos
- Estructuras organizadas

Python identifica automáticamente el tipo de dato dependiendo del valor que escribas.

---

# 🧵 STRINGS (CADENAS DE TEXTO)

Los **strings** se utilizan para almacenar texto.

## 📌 Ejemplos

```python
"Hola"
'Python'
```

También pueden escribirse en múltiples líneas:

```python
"""
Hola
Mundo
"""

'''
Python
Curse
'''
```

---

# 🔢 DATOS NUMÉRICOS

Python permite trabajar con números enteros y decimales.

---

## 📌 ENTEROS (`int`)

Son números sin decimales.

```python
1
25
400
-12
```

---

## 📌 FLOTANTES (`float`)

Son números con decimales.

```python
4.2
10.5
99.99
-3.14
```

>**Es importante entender que los números decimales en python se escriben con punto (.) en lugar de coma (,).**

---

# ✅ BOOLEANOS (`bool`)

Los booleanos solo pueden tener dos valores:

```python
True
False
```

Se utilizan muchísimo en:

- condiciones
- comparaciones
- lógica
- validaciones

---

# 📋 LISTAS (`list`)

Las listas permiten almacenar múltiples datos en una sola variable.

## 📌 Ejemplo

```python
lista = ["John Doe", "Estudiar", True, 34, 15]

print(lista)
print(lista[0])
print(lista[2])
```

---

## 📌 Modificar datos de una lista

Las listas pueden modificarse.

```python
lista[2] = "Limpiar"

print(lista[2])
```

---

# 📌 TUPLAS (`tuple`)

Las tuplas son similares a las listas, pero no pueden modificarse después de crearse.

## 📌 Ejemplo

```python
tupla = ("John Doe", "Estudiar", True, 34, 15)

print(tupla)
print(tupla[0])
```

---

## ❌ Ejemplo de error

```python
tupla[1] = "Feliz"
```

Las tuplas son estructuras inmutables.

---

# 🧩 SETS / CONJUNTOS (`set`)

Los conjuntos almacenan datos sin un orden específico.

## 📌 Ejemplo

```python
conjunto = {"John Doe", "Estudiar", True, 34, 15}
```

---

## ⚠️ Características importantes

Los sets:

- No usan índices
- No mantienen orden fijo
- No permiten datos duplicados

---

# 🗂 DICCIONARIOS (`dict`)

Los diccionarios almacenan información usando una estructura de:

```python
clave : valor
```

---

## 📌 Ejemplo

```python
diccionario = {
    "nombre": "John Doe",
    "accion": "Estudiar",
    "edad": 34
}

print(diccionario["nombre"])
```

---

# 🧠 Resumen rápido

| Tipo de dato | Ejemplo |
|---|---|
| String | `"Hola"` |
| Integer | `10` |
| Float | `4.5` |
| Boolean | `True` |
| Lista | `[1, 2, 3]` |
| Tupla | `(1, 2, 3)` |
| Set | `{1, 2, 3}` |
| Diccionario | `{"nombre": "Juan"}` |

---

# 💡 Consejo

No intentes memorizar todos los tipos de datos inmediatamente.

Lo importante es:

- entender para qué sirve cada uno
- practicar
- experimentar
- cometer errores
- aprender poco a poco

Con la práctica terminarás utilizándolos de forma natural 🚀