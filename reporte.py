print("Los agentes guardados anteriormente son: \n")

with open("Agentes.txt","r") as archivo:
    for linea in archivo:
        print(linea)

