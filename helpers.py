import os
import platform
import re

def limpiar_pantalla():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# Luego, cuando necesites limpiar la pantalla, simplemente llama a la función:
limpiar_pantalla()

    
    
def leer_texto(longitud_min=0, longitud_max=100, mensaje=None):
    print(mensaje) if mensaje else None
    while True:
        texto = input("> ")
        if len(texto) >= longitud_min and len(texto) <= longitud_max:
            return texto
        
# validar si el dni existe

def dni_valido(dni,lista):
    if not re.match('[0-9]{2}[A-Z]$',dni):
        print('DNI incorrecto')
        return False
    for cliente in lista:
        if cliente.dni == dni:
            print('DNI existente')
            return False
    return True

               