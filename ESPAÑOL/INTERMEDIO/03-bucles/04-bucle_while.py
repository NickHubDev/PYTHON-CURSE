# ============================================
# BUCLE WHILE
# ============================================

"""
Un bucle while ejecuta código mientras
una condición siga siendo verdadera.

En este ejemplo:
- Empezamos desde 0
- El bucle continuará mientras numero sea menor que 11
- En cada vuelta aumentamos el valor en 1
"""

numero = 0

while numero < 11:
    print(numero)

    # Incrementamos el valor para evitar un bucle infinito
    numero += 1