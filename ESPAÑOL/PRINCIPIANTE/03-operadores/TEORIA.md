# ⚙️ OPERADORES EN PYTHON

> Los operadores son símbolos que permiten manipular datos, compararlos y construir lógica dentro de un programa.

En Python no solo sirven para calcular, también para **tomar decisiones**.

---

# 🔢 OPERADORES ARITMÉTICOS

Los operadores aritméticos se usan para realizar operaciones matemáticas básicas.

---

## ➕ SUMA (`+`)

Suma dos valores.

```python
suma = 12 + 8
print(suma)
```

📌 Se usa también para concatenar textos:

```python
nombre = "Juan"
print("Hola " + nombre)
```

---

## ➖ RESTA (`-`)

Resta dos valores.

```python
resta = 45 - 3
print(resta)
```

---

## ✖️ MULTIPLICACIÓN (`*`)

Multiplica valores.

```python
multiplicacion = 12 * 5
print(multiplicacion)
```

📌 También se usa para repetir texto:

```python
print("Hola " * 3)
```

---

## ➗ DIVISIÓN (`/`)

Divide dos valores.

```python
division = 12 / 5
print(division)
```

📌 Siempre devuelve un `float` aunque sea exacto.

---

## 🧮 POTENCIA (`**`)

Eleva un número a otro.

```python
potencia = 12 ** 5
print(potencia)
```

📌 Ejemplo mental:
- 2 ** 3 = 2 × 2 × 2

---

## 🔽 DIVISIÓN ENTERA (`//`)

Divide y redondea hacia abajo.

```python
division_baja = 12 // 5
print(division_baja)
```

📌 Ejemplo:
- 12 / 5 = 2.4
- 12 // 5 = 2

---

## 🧾 MÓDULO (`%`)

Devuelve el **resto** de una división.

```python
modulo = 12 % 5
print(modulo)
```

📌 Ejemplo mental:
- 12 / 5 = 2 sobra 2
- resultado = 2

💡 Muy usado para:
- comprobar números pares/impares
- ciclos
- validaciones

---

# ⚖️ OPERADORES DE COMPARACIÓN

Devuelven siempre `True` o `False`.

Sirven para tomar decisiones.

---

## == IGUAL

```python
5 == 6
```

📌 ¿Son iguales los valores?

---

## != DISTINTO

```python
5 != 6
```

📌 ¿Son diferentes?

---

## > MAYOR QUE

```python
5 > 6
```

📌 ¿El de la izquierda es mayor?

---

## < MENOR QUE

```python
5 < 6
```

📌 ¿El de la izquierda es menor?

---

## >= MAYOR O IGUAL

```python
5 >= 6
```

---

## <= MENOR O IGUAL

```python
5 <= 6
```

---

# 🧠 IMPORTANTE

Estos operadores no “calculan”, solo responden:

- Sí → `True`
- No → `False`

---

# 🧠 OPERADORES LÓGICOS

Se usan para combinar condiciones.

---

## AND

Devuelve `True` solo si TODO es verdadero.

```python
True and True
```

📌 Tabla mental:

| A | B | Resultado |
|---|---|-----------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

---

## OR

Devuelve `True` si al menos uno es verdadero.

```python
False or True
```

📌 Tabla mental:

| A | B | Resultado |
|---|---|-----------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

---

## NOT

Invierte el valor.

```python
not True  # False
not False # True
```

---

# 🔍 OPERADORES DE PERTENENCIA

Sirven para comprobar si algo existe dentro de otro valor.

---

## IN

```python
"Hola" in "Hola Juan"
```

📌 ¿Existe dentro del texto?

---

## NOT IN

```python
"Hola" not in "Hola Juan"
```

📌 ¿NO existe dentro del texto?

---

# 🧠 RESUMEN REAL (IMPORTANTE)

- 🔢 Aritméticos → calculan valores
- ⚖️ Comparación → crean condiciones
- 🧠 Lógicos → combinan decisiones
- 🔎 Pertenencia → buscan dentro de datos

---

# 💡 IDEA CLAVE

Los operadores no son teoría aislada.

Son la base de:

- condiciones (`if`)
- bucles (`while`, `for`)
- validaciones
- lógica de programas reales

Si entiendes esto bien, todo lo demás en Python se vuelve más fácil.