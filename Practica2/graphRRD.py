import sys
import rrdtool
import time
#from tiempoRRD import tiempostart
#from tiempoRRD import tiempoend

tiempo_actual = int(1667958000)
#Grafica desde el tiempo actual menos diez minutos
tiempo_inicial = int(1667956500) - 600

ret = rrdtool.graph( "img1.png",
                     "--start",str(tiempo_inicial),
                     "--end",str(tiempo_actual),
                     "--vertical-label=Bytes/s",
                     "--title=Tráfico de Red de un agente \n Usando SNMP y RRDtools",
                     "DEF:traficoPaqInter=traficoRED.rrd:paq_uni_interfaz:AVERAGE",
                     "CDEF:escalaIn=traficoPaqInter,8,*",
                     "LINE1:escalaIn#FF0000:Paquetes unicast que ha recibido una interfaz")
                     
ret = rrdtool.graph( "img2.png",
                     "--start",str(tiempo_inicial),
                     "--end",str(tiempo_actual),
                     "--vertical-label=Bytes/s",
                     "--title=Tráfico de Red de un agente \n Usando SNMP y RRDtools",
                     "DEF:traficoPaqIpv4=traficoRED.rrd:paq_ipv4_err:AVERAGE",
                     "CDEF:escalaIn=traficoPaqIpv4,8,*",
                     "LINE1:escalaIn#FF0000:Paquetes recibidos a protocolo IPv4, incluyendo los que tienen error")
                     
ret = rrdtool.graph( "img3.png",
                     "--start",str(tiempo_inicial),
                     "--end",str(tiempo_actual),
                     "--vertical-label=Bytes/s",
                     "--title=Tráfico de Red de un agente \n Usando SNMP y RRDtools",
                     "DEF:traficoMenIcmp=traficoRED.rrd:mens_icmp_agen:AVERAGE",
                     "CDEF:escalaIn=traficoMenIcmp,8,*",
                     "LINE1:escalaIn#FF0000:Mensajes ICMP Echo que se ha enviado al agente")

ret = rrdtool.graph( "img4.png",
                     "--start",str(tiempo_inicial),
                     "--end",str(tiempo_actual),
                     "--vertical-label=Bytes/s",
                     "--title=Tráfico de Red de un agente \n Usando SNMP y RRDtools",
                     "DEF:traficoSegErr=traficoRED.rrd:nseg_err:AVERAGE",
                     "CDEF:escalaIn=traficoSegErr,8,*",
                     "LINE1:escalaIn#FF0000:Numero de segmentos recibidos, incluyendo los que se han recibido con errores")

ret = rrdtool.graph( "img5.png",
                     "--start",str(tiempo_inicial),
                     "--end",str(tiempo_actual),
                     "--vertical-label=Bytes/s",
                     "--title=Tráfico de Red de un agente \n Usando SNMP y RRDtools",
                     "DEF:traficoDataUdp=traficoRED.rrd:data_udp:AVERAGE",
                     "CDEF:escalaIn=traficoDataUdp,8,*",
                     "LINE1:escalaIn#FF0000:Datagramas entregados a usuarios UDP")
