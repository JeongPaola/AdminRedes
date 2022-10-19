import re

print("Sistema de Administración de Red")
print("Práctica 1 - Adquisición de información")
print("Jeong Paola 4CM13 2020630193")

menu = """
Elija una opción
1) Agregar dispositivo
2) Cambiar información de dispositivo
3) Eliminar dispositivo
"""
print(menu)
op = int(input(""))
if op == 1:

    file = open("Agentes.pdf","a")

    com = input("Ingrese el nombre de la comunidad\n")
    file.write(com + '\n')

    ver = input ("Ingrese la versión SNMP\n")
    file.write('% s' %ver + '\n')

    puerto = input("Ingrese el puerto\n")
    file.write('% s' %puerto + '\n')

    ip = input("Ingrese la dirección IP\n")
    file.write('% s' %ip + '\n')

    file.close()

    print("¿Desea agregar otro agente?")
    menu="""
    1. Sí
    2.No
    """
    print(menu)
    sop = int(input(""))

    if sop == 1:
        file = open("Agentes.txt","a")

        com = input("Ingrese el nombre de la comunidad\n")
        file.write(com + '\n')

        ver = input ("Ingrese la versión SNMP\n")
        file.write('% s' %ver + '\n')

        puerto = input("Ingrese el puerto\n")
        file.write('% s' %puerto + '\n')

        ip = input("Ingrese la dirección IP\n")
        file.write('% s' %ip + '\n')
        
    elif sop == 2:
        print("")  

    else:
        file.close()

elif op == 2:
    menu = """
    Elija una opción
    1) Modificar comunidad
    2) Modificar versión SNMP
    3) Modificar puerto
    4) Modificar IP
    """

elif op == 3:
    print("Hola galaxia")
else:
    print("No se ha seleccionado una opción")
