from pysnmp.hlapi import *

print("Los agentes guardados anteriormente son: \n")

with open("Agentes.txt","r") as archivo:
    for linea in archivo:
        print(linea)

def consulta( oid ):
	iterator = getCmd(
		SnmpEngine(),
		CommunityData('comunidadASRWin', mpModel=0),
		UdpTransportTarget(('192.168.0.5', 161)),
		ContextData(),
		ObjectType(ObjectIdentity(oid))
	)
	return iterator
	
def imprimir(iterator):
	errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

	if errorIndication:
		print(errorIndication)

	elif errorStatus:
		print('%s at %s' % (errorStatus.prettyPrint(),
		         errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
	else:
		for varBind in varBinds:
			print(' = '.join([x.prettyPrint() for x in varBind]))

print("Sistema operativo")
iterator1 = consulta('1.3.6.1.2.1.1.1.0')
imprimir(iterator1)

print("\nNombre del dispositivo")
iterator2 = consulta('1.3.6.1.2.1.1.5.0')
imprimir(iterator2)

print("\nContacto")
iterator3 = consulta('1.3.6.1.2.1.1.4.0')
imprimir(iterator3)

print("\nUbicación")
iterator4 = consulta('1.3.6.1.2.1.1.6.0')
imprimir(iterator4)

print("\nNúmero de interfaces")
iterator5 = consulta('1.3.6.1.2.1.2.1.0')
imprimir(iterator5)






