# ⌨️ Inputs en Python

## ¿Qué es `input()`?

La función `input()` permite leer información escrita por el usuario.

```python
nombre = input("Introduce tu nombre: ")
print("Hola,", nombre)
```

El valor devuelto siempre es de tipo `str`.

---

# 🔢 Convertir a otros tipos

## Enteros

```python
edad = int(input("Edad: "))
```

## Decimales

```python
altura = float(input("Altura: "))
```

## Booleanos (manual)

```python
respuesta = input("¿Continuar? (si/no): ").lower()
continuar = respuesta == "si"
```

---

# ➕ Uso en operaciones

```python
a = int(input("Primer número: "))
b = int(input("Segundo número: "))

print(a + b)
```

---

# 🧹 Limpiar entradas

```python
nombre = input("Nombre: ").strip().title()
```

---

# ⚠️ Errores comunes

## Olvidar la conversión

```python
# "2" + "3" = "23"
```

## Entrada inválida

```python
# int("hola") -> ValueError
```

---

# 🛡️ Manejo básico de errores

```python
try:
    numero = int(input("Número: "))
except ValueError:
    print("Debes introducir un número entero.")
```

---

# 🧠 Casos de uso

- Formularios.
- Calculadoras.
- Juegos.
- Scripts interactivos.
- Herramientas de consola.

---

# 📝 Ejercicio propuesto

Crear un programa que pida:

1. Nombre.
2. Edad.
3. Ciudad.

Y muestre un mensaje formateado con esos datos.

---

# 🎯 Resumen

`input()` es la puerta de entrada de datos en programas interactivos. Combinado con conversiones y validación, permite construir aplicaciones útiles y robustas.


