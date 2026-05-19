# 📦 VARIABLES EN PYTHON

> Las variables permiten almacenar información para poder reutilizarla más adelante dentro de un programa.

---

# 📖 ¿Qué es una variable?

Una variable es un espacio donde guardamos datos.

Python utiliza el símbolo `=` para asignar valores a una variable.

## 📌 Ejemplo

```python
a = 8
b = 5
c = 10
```

En este caso:

- `a` almacena el valor `8`
- `b` almacena el valor `5`
- `c` almacena el valor `10`

---

# 🧠 Uso de variables

Una vez creadas, podemos utilizar las variables para realizar operaciones.

## 📌 Ejemplo

```python
a = 8
c = 10

print(a + c)
```

Resultado:

```python
18
```

---

# 🔄 Reasignación de variables

Las variables pueden cambiar su valor durante la ejecución del programa.

## 📌 Ejemplo

```python
a = 10
b = 14
c = 4

print(a + c)
```

---

# 🔗 CONCATENACIÓN

La concatenación consiste en unir textos o valores.

## 📌 Ejemplo

```python
nombre = "John Doe"

bienvenida = "Hola " + nombre

print(bienvenida)
```

Resultado:

```python
Hola John Doe
```

---

# ⚠️ Error común

No se puede concatenar directamente texto con números.

## ❌ Incorrecto

```python
suma = "Resultado: " + 10
```

Esto generará un error.

---

# 🚀 F-STRINGS

Los **f-strings** son una forma moderna y limpia de insertar variables dentro de textos.

## 📌 Ejemplo

```python
operacion_suma = 24

suma_alternativa = f"La suma es: {operacion_suma}"

print(suma_alternativa)
```

Resultado:

```python
La suma es: 24
```

---

# 🗑 FUNCIÓN `del`

La función `del` elimina variables.

## 📌 Ejemplo

```python
operacion_suma = 20

del operacion_suma
```

Si intentamos usar la variable después de eliminarla, Python generará un error.

---

# ✍️ ESTILOS DE VARIABLES

Existen diferentes formas de nombrar variables.

---

# 📌 camelCase

La primera palabra comienza en minúscula y las siguientes empiezan con mayúscula.

## 📌 Ejemplo

```python
nombreCompletoTuto = "Juan Antonio García"
```

---

# 📌 snake_case

Todas las palabras están separadas por guiones bajos.

## 📌 Ejemplo

```python
nombre_completo_tuto = "Juan Antonio García"
```

> ✅ En Python, el estilo más recomendado es `snake_case`.

---

# 🧠 Consejo importante

Elige nombres de variables claros y fáciles de entender.

## ❌ Malo

```python
x = "Juan"
```

## ✅ Mejor

```python
nombre_usuario = "Juan"
```

El código limpio y entendible es muchísimo más importante que escribir rápido 🚀