# FUNCIONES EN PYTHON

> Las funciones permiten reutilizar código, organizar programas y crear lógica modular.
>
> Son una de las herramientas más importantes en programación profesional.

---

# ¿QUÉ ES UNA FUNCIÓN?

Una función es un bloque de código reutilizable.

En lugar de repetir código muchas veces:

```python
print("Hola")
print("Hola")
print("Hola")
```

Podemos crear una función:

```python
def saludar():
    print("Hola")
```

Y ejecutarla cuando queramos.

---

# CREANDO FUNCIONES

## Sintaxis

```python
def nombre_funcion():
    # código
```

---

# EJECUTANDO FUNCIONES

Crear una función NO la ejecuta automáticamente.

Debemos llamarla.

## Ejemplo

```python
def presentar():
    print("Bienvenido")

presentar()
```

---

# FUNCIONES SIN PARÁMETROS

Las funciones pueden no recibir datos externos.

## Ejemplo

```python
def presentar():
    print("Bienvenidos a este tutorial")
```

---

# PARÁMETROS

Los parámetros permiten que una función trabaje con diferentes datos.

## Ejemplo

```python
def saludar(nombre):
    print(f"Hola {nombre}")
```

---

# ARGUMENTOS

Los argumentos son los valores enviados a la función.

## Ejemplo

```python
saludar("Juan")
```

En este caso:

* parámetro → `nombre`
* argumento → `"Juan"`

---

# FUNCIONES CON MÚLTIPLES PARÁMETROS

## Ejemplo

```python
def presentar(nombre, adjetivo):
    print(f"Hola {nombre}")
    print(f"Eres un {adjetivo}")
```

---

# RETURN

`return` devuelve un valor fuera de la función.

## Ejemplo

```python
def suma(a, b):
    return a + b
```

---

# DIFERENCIA ENTRE PRINT Y RETURN

## PRINT

```python
print("Hola")
```

Solo muestra información.

---

## RETURN

```python
return "Hola"
```

Devuelve información para reutilizarla.

---

# GUARDANDO RESULTADOS

Los valores retornados pueden guardarse.

## Ejemplo

```python
def suma(a, b):
    return a + b

resultado = suma(5, 10)
```

---

# PARÁMETROS POR DEFECTO

Python permite asignar valores predeterminados.

## Ejemplo

```python
def presentar(nombre, adjetivo="listo"):
    print(nombre)
```

---

# ¿CÓMO FUNCIONA?

Si no enviamos un valor:

```python
presentar("Juan")
```

Python utilizará:

```python
"listo"
```

como valor automático.

---

# ARGUMENTOS NOMBRADOS

Python permite indicar el nombre del parámetro.

## Ejemplo

```python
presentar(
    nombre="Juan",
    adjetivo="grande"
)
```

Esto mejora mucho la legibilidad.

---

# FUNCIONES Y LISTAS

Las funciones también pueden recibir listas.

## Ejemplo

```python
def suma_lista(lista_numeros):

    resultado = 0

    for numero in lista_numeros:
        resultado += numero

    return resultado
```

---

# FUNCIONES VARIABLES

Python permite recibir múltiples argumentos dinámicamente.

## Ejemplo

```python
def suma(*numeros):
    return sum(numeros)
```

---

# ¿QUÉ HACE EL *?

El operador `*` agrupa múltiples argumentos dentro de una tupla.

## Ejemplo

```python
suma(1, 2, 3, 4)
```

Python internamente crea:

```python
(1, 2, 3, 4)
```

---

# FUNCIONES LAMBDA

Las lambdas son funciones anónimas.

Se utilizan normalmente para operaciones pequeñas y rápidas.

## Sintaxis

```python
lambda parametros: resultado
```

---

# EJEMPLO DE LAMBDA

```python
multiplicar_por_doce = lambda numero: numero * 12
```

---

# FILTER()

`filter()` permite filtrar elementos.

Solo conserva los elementos donde la función devuelve `True`.

---

# EJEMPLO DE FILTER

```python
numeros = [2, 4, 5, 7]


def es_par(numero):
    return numero % 2 == 0


numeros_pares = filter(es_par, numeros)
```

---

# DETALLE IMPORTANTE DE FILTER()

`filter()` NO devuelve una lista.

Devuelve un objeto iterable.

Por eso normalmente usamos:

```python
list(numeros_pares)
```

---

# FUNCIONES INTEGRADAS

Python incluye muchas funciones ya creadas.

## Algunas importantes

```python
max()
min()
sum()
round()
all()
bool()
```

---

# MAX()

Devuelve el valor más alto.

## Ejemplo

```python
max([1, 5, 20])
```

Resultado:

```python
20
```

---

# MIN()

Devuelve el valor más pequeño.

## Ejemplo

```python
min([1, 5, 20])
```

Resultado:

```python
1
```

---

# SUM()

Suma todos los valores.

## Ejemplo

```python
sum([1, 2, 3])
```

Resultado:

```python
6
```

---

# ROUND()

Redondea números decimales.

## Ejemplo

```python
round(15.67128, 2)
```

Resultado:

```python
15.67
```

---

# BOOL()

Convierte valores a:

* `True`
* `False`

---

# TRUTHY Y FALSY

Python interpreta algunos valores como falsos.

## Ejemplos falsy

```python
False
0
None
[]
{}
""
```

---

# ALL()

`all()` devuelve `True` únicamente si TODOS los valores son verdaderos.

## Ejemplo

```python
all([1, True, "Hola"])
```

Resultado:

```python
True
```

---

# BUENAS PRÁCTICAS

✅ Usa nombres descriptivos.

✅ Divide problemas grandes en funciones pequeñas.

✅ Usa `return` cuando necesites reutilizar datos.

✅ Evita funciones gigantes.

✅ Mantén cada función con una responsabilidad clara.

✅ Usa parámetros por defecto cuando tenga sentido.

---

# ERRORES COMUNES

## 1. Sobrescribir funciones

```python
def saludar():
    pass


def saludar(nombre):
    pass
```

La segunda reemplaza completamente la primera.

---

## 2. Confundir print con return

```python
return print("Hola")
```

No suele tener sentido.

---

## 3. Nombres poco descriptivos

Evita:

```python
def x(a):
```

Mejor:

```python
def calcular_total(precios):
```

---

# ¿POR QUÉ SON TAN IMPORTANTES?

Las funciones son la base de:

* backend
* APIs
* frameworks
* inteligencia artificial
* automatización
* videojuegos
* aplicaciones web
* scripts profesionales

Prácticamente cualquier proyecto serio utiliza funciones constantemente.

---

# RESUMEN

En esta carpeta aprendiste:

* creación de funciones
* parámetros
* argumentos
* `return`
* parámetros por defecto
* argumentos nombrados
* `*args`
* funciones lambda
* `filter()`
* funciones integradas

Estos conceptos son fundamentales para avanzar hacia:

* programación modular
* backend
* orientación a objetos
* FastAPI
* automatización
* desarrollo profesional en Python
