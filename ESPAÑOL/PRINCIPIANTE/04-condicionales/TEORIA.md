# 🔀 CONDICIONALES EN PYTHON

> Los condicionales permiten que un programa **tome decisiones** dependiendo de si una condición se cumple o no.

En otras palabras: el código deja de ser lineal y empieza a “elegir caminos”.

---

# 🧠 IDEA CLAVE

Un condicional siempre responde a una pregunta:

- ¿Se cumple esto? → sí / no (`True` / `False`)

---

# 🟢 IF (SI)

El `if` ejecuta código solo si la condición es verdadera.

---

## 📌 Ejemplo básico

```python
edad = 18

if edad >= 18:
    print("Genial, ¡Puedes pasar!")
```

---

## 🔍 ¿Qué está pasando aquí?

- `edad >= 18` → se evalúa como `True` o `False`
- si es `True` → entra al bloque
- si es `False` → lo ignora

---

# 🔴 ELSE (SI NO)

El `else` se ejecuta cuando el `if` NO se cumple.

---

## 📌 Ejemplo

```python
edad = 17

if edad >= 18:
    print("Genial, ¡Puedes pasar!")
else:
    print("No puedes pasar.")
```

---

## 🧠 IDEA IMPORTANTE

El `if/else` siempre cubre **todos los casos posibles**:

- uno se ejecuta
- el otro no

Nunca quedan “en el aire”

---

# 🟡 ELIF (SI NO, SI…)

El `elif` permite añadir **múltiples condiciones**.

Es como decir:

> “Si no es esto, prueba esto otro”

---

## 📌 Ejemplo

```python
dinero = 100000

if dinero >= 100000:
    print("¡Eres rico!")
elif dinero >= 10000:
    print("Puedes vivir bastante bien.")
elif dinero > 1000:
    print("Está bastante bien para sobrevivir.")
else:
    print("Eres pobre.")
```

---

## 🔍 ¿Cómo se ejecuta esto?

Python evalúa de arriba hacia abajo:

1. `if`
2. primer `elif`
3. segundo `elif`
4. `else` (si nada se cumple)

📌 IMPORTANTE:
- Solo se ejecuta **una opción**
- Cuando una condición es verdadera, se detiene todo

---

# ⚠️ ERROR COMÚN

Pensar que todos los `elif` se ejecutan.

❌ Incorrecto

✔️ Solo se ejecuta el primero que sea verdadero

---

# 🧠 ORDEN IMPORTA

En `elif`, el orden cambia el resultado.

Ejemplo:

```python
if dinero >= 1000:
    print("Bien")
elif dinero >= 100000:
    print("Rico")
```

📌 Problema:
- nunca llegará a “Rico” porque 100000 también cumple >= 1000

---

# 🧩 ESTRUCTURA GENERAL

```python
if condicion:
    # se ejecuta si es True
elif otra_condicion:
    # se ejecuta si la anterior es False y esta True
else:
    # se ejecuta si ninguna se cumple
```

---

# 🧠 CÓMO PENSAR LOS CONDICIONALES

No pienses en código.

Piensa en decisiones reales:

- si tienes 18 → entras
- si tienes menos → no entras
- si tienes mucho dinero → eres rico
- si tienes poco → sobrevives

Python solo traduce lógica humana a código.

---

# 💡 CONSEJO IMPORTANTE

Los condicionales son la base de TODO:

- videojuegos 🎮
- apps 📱
- IA 🤖
- backend 🌐

Si controlas bien esto, controlas el comportamiento del programa.

---