import datetime
import time

print("Sistema de administraciòn de red")
print("Practica 2 - Administracioin de contabilidad")
print("Jeong Paola 4CM13 2020630193")

def tiempostart():
    print("Ingrese el año del tiempo inicial")
    anio = int(input(""))
    print("Ingrese el mes del tiempo inicial")
    mes = int(input(""))
    print("Ingrese el dia del tiempo inicial")
    dia = int(input(""))
    print("Ingrese la hora del tiempo inicial")
    hora = int(input(""))
    print("Ingrese los minutos del tiempo inicial")
    mnt= int(input(""))
    print("Ingrese los segundos del tiempo inicial")
    seg = int(input(""))

    timestart = datetime.datetime(anio,mes,dia,hora,mnt,seg)
    unixtime = datetime.datetime.timestamp(timestart)
    return unixtime
    
tiempostart()
    
def tiempoend():
    print("Ingrese el año del tiempo final")
    aniof = int(input(""))
    print("Ingrese el mes del tiempo final")
    mesf = int(input(""))
    print("Ingrese el dia del tiempo final")
    diaf = int(input(""))
    print("Ingrese la hora del tiempo final")
    horaf = int(input(""))
    print("Ingrese los minutos del tiempo final")
    mntf = int(input(""))
    print("Ingrese los segundos del tiempo final")
    segf = int(input(""))

    timend= datetime.datetime(aniof,mesf,diaf,horaf,mntf,segf)
    unixtimef = datetime.datetime.timestamp(timend)
    return unixtimef
tiempoend()

