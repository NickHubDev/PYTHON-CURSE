# BUCLES EN PYTHON

> Los bucles permiten repetir código automáticamente.
>
> Son una de las bases más importantes de la programación, ya que permiten recorrer datos, automatizar tareas y ejecutar lógica repetitiva sin escribir el mismo código múltiples veces.

---

# ¿QUÉ ES UN BUCLE?

Un bucle es una estructura que ejecuta un bloque de código varias veces.

Python tiene principalmente dos tipos:

* `while`
* `for`

Cada uno tiene objetivos distintos.

---

# BUCLE WHILE

El bucle `while` ejecuta código mientras una condición sea verdadera.

## Sintaxis

```python
while condicion:
    # código
```

## Ejemplo

```python
numero = 0

while numero < 5:
    print(numero)
    numero += 1
```

## Resultado

```python
0
1
2
3
4
```

---

# ¿CÓMO FUNCIONA?

1. Python revisa la condición.
2. Si es `True`, ejecuta el bloque.
3. Vuelve a revisar la condición.
4. El proceso se repite hasta que la condición sea `False`.

---

# BUCLES INFINITOS

Uno de los errores más comunes es olvidar modificar la condición.

## Ejemplo peligroso

```python
numero = 0

while numero < 5:
    print(numero)
```

Este código nunca termina porque `numero` nunca cambia.

---

# OPERADOR +=

Muy utilizado dentro de bucles.

## Ejemplo

```python
numero += 1
```

Es equivalente a:

```python
numero = numero + 1
```

---

# BUCLE FOR

El bucle `for` se utiliza para recorrer colecciones.

Por ejemplo:

* listas
* tuplas
* conjuntos
* diccionarios
* strings

## Sintaxis

```python
for elemento in coleccion:
    # código
```

---

# ITERANDO LISTAS

## Ejemplo

```python
animales = ["gato", "perro", "loro"]

for animal in animales:
    print(animal)
```

## Resultado

```python
gato
perro
loro
```

---

# VARIABLES TEMPORALES EN FOR

En cada vuelta del bucle:

```python
for animal in animales:
```

La variable `animal` toma automáticamente el valor del siguiente elemento.

---

# LISTAS, TUPLAS Y CONJUNTOS

Las listas, tuplas y conjuntos se recorren exactamente igual.

## Ejemplo

```python
for elemento in coleccion:
    print(elemento)
```

La diferencia entre ellas NO está en cómo se iteran.

La diferencia está en:

* si pueden modificarse,
* si mantienen el orden,
* si permiten duplicados.

---

# RECORRIENDO DICCIONARIOS

Los diccionarios tienen:

* claves
* valores

## Ejemplo

```python
diccionario = {
    "nombre": "John",
    "edad": 34
}
```

---

# .items()

`.items()` devuelve una tupla con:

```python
(clave, valor)
```

---

# VERSIÓN PYTHON BASE

```python
for datos in diccionario.items():
    clave = datos[0]
    valor = datos[1]

    print(clave, valor)
```

---

# VERSIÓN PYTHON PROFESIONAL

```python
for clave, valor in diccionario.items():
    print(clave, valor)
```

Esto se llama:

* desempaquetado
* unpacking

Y es la forma más utilizada en Python moderno.

---

# ZIP()

`zip()` combina múltiples colecciones.

## Ejemplo

```python
animales = ["gato", "perro", "loro"]
numeros = [1, 2, 3]

for animal, numero in zip(animales, numeros):
    print(animal, numero)
```

## Resultado

```python
gato 1
perro 2
loro 3
```

---

# DETALLE IMPORTANTE DE ZIP()

`zip()` se detiene cuando la colección más corta termina.

## Ejemplo

```python
animales = ["gato", "perro", "loro"]
numeros = [1]
```

Resultado:

```python
gato 1
```

---

# ENUMERATE()

`enumerate()` añade automáticamente un índice.

## Ejemplo

```python
numeros = [10, 20, 30]

for indice, valor in enumerate(numeros):
    print(indice, valor)
```

## Resultado

```python
0 10
1 20
2 30
```

---

# CONTINUE

`continue` salta la iteración actual.

## Ejemplo

```python
marcas = ["nike", "google", "pepsi"]

for marca in marcas:

    if marca == "google":
        continue

    print(marca)
```

## Resultado

```python
nike
pepsi
```

---

# BREAK

`break` detiene completamente el bucle.

## Ejemplo

```python
marcas = ["nike", "google", "pepsi"]

for marca in marcas:

    if marca == "google":
        break

    print(marca)
```

## Resultado

```python
nike
```

---

# LIST COMPREHENSIONS

Las comprehensions permiten crear listas de forma rápida y limpia.

## Ejemplo

```python
numeros = [1, 2, 3]

numeros_doblados = [numero * 2 for numero in numeros]
```

## Resultado

```python
[2, 4, 6]
```

---

# ¿POR QUÉ SON IMPORTANTES?

Los bucles son utilizados constantemente en:

* backend
* APIs
* automatización
* inteligencia artificial
* videojuegos
* análisis de datos
* scripts
* desarrollo web

Prácticamente cualquier programa real utiliza bucles.

---

# ERRORES COMUNES

## 1. Crear bucles infinitos

```python
while True:
    print("Hola")
```

---

## 2. Modificar colecciones incorrectamente

Modificar listas mientras se recorren puede provocar errores difíciles de detectar.

---

## 3. Usar nombres poco descriptivos

Evita:

```python
for x in lista:
```

Mejor:

```python
for usuario in usuarios:
```

---

# BUENAS PRÁCTICAS

✅ Usa nombres descriptivos.

✅ Mantén los bucles simples.

✅ Evita lógica extremadamente larga dentro de un `for`.

✅ Usa `enumerate()` cuando necesites índices.

✅ Usa `zip()` para recorrer múltiples colecciones.

✅ Usa comprehensions cuando hagan el código más limpio.

---

# RESUMEN

En esta carpeta aprendiste:

* `while`
* `for`
* iteración de colecciones
* diccionarios
* `zip()`
* `enumerate()`
* `continue`
* `break`
* list comprehensions

Estos conceptos son fundamentales para avanzar hacia:

* funciones avanzadas
* manipulación de datos
* backend
* automatización
* programación profesional en Python
