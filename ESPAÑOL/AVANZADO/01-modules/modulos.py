# import modulo_suma

# suma = modulo_suma.suma(1,56,98)

import modulo_suma as module

suma = module.suma(1,56,85)

from modulo_suma import suma

suma(14,23,67)

# print(dir(suma))

import submodules.saludo as subm

print(subm.saludo("Juan"))

from sys import path

print(path)

import sys

sys.path.append('/home/nick/Documentos/PYTHON CURSE/ESPAÑOL/INTERMEDIO/04-funciones')

