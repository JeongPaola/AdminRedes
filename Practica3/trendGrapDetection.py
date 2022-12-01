import sys
import rrdtool
import time
import datetime
from  Notify import send_alert_attached
import time
rrdpath = '/home/paola/Escritorio/AdminRedes/Practica3/RRD/'
imgpath = '/home/paola/Escritorio/AdminRedes/Practica3/IMG/'

def generarGraficaCPU(ultima_lectura):
    tiempo_final = int(ultima_lectura)
    tiempo_inicial = tiempo_final - 1800
    retCPU = rrdtool.graphv( imgpath+"usoCPU.png",
                     "--start",str(tiempo_inicial),
                     "--end",str(tiempo_final),
                     "--vertical-label=Cpu load",
                    '--lower-limit', '0',
                    '--upper-limit', '100',
                    "--title=Uso del CPU",
                    "DEF:usoCPU="+rrdpath+"trendCPU.rrd:usoCPU:AVERAGE",
                     "AREA:usoCPU#00FF00:Carga del CPU",
                     "HRULE:40#FF0000:Umbral  40%",
                     "HRULE:60#DC143C:Umbral  60%",
                     "HRULE:75#5F9EA0:Umbral  75%")
    
while (1):
    ultima_actualizacionCPU = rrdtool.lastupdate(rrdpath + "trendCPU.rrd")
    timestamp=ultima_actualizacionCPU['date'].timestamp()
    datoCPU=ultima_actualizacionCPU['ds']["usoCPU"]
    
    if datoCPU> 40:
        generarGraficaCPU(int(timestamp))
        send_alert_attached("Sobrepasa el primer umbral del CPU", 'usoCPU')
        print("sobrepasa el umbral del CPU")
        
    if datoCPU> 60:
        generarGraficaCPU(int(timestamp))
        send_alert_attached("Sobrepasa el segundo umbral del CPU", 'usoCPU')
        print("sobrepasa el umbral del CPU")
        
    if datoCPU> 75:
        generarGraficaCPU(int(timestamp))
        send_alert_attached("Sobrepasa el tercer umbral del CPU", 'usoCPU')
        print("sobrepasa el umbral del CPU")
    time.sleep(20)
    
#############################################################################################################

def generarGraficaRAM(ultima_lectura):
    tiempo_final = int(ultima_lectura)
    tiempo_inicial = tiempo_final - 1800
    retRAM = rrdtool.graphv( imgpath+"usoRAM.png",
                     "--start",str(tiempo_inicial),
                     "--end",str(tiempo_final),
                     "--vertical-label=Almacenamiento",
                    '--lower-limit', '0',
                    '--upper-limit', '100',
                    "--title=Uso de la memoria",
                    "DEF:usoRAM="+rrdpath+"trendRAM.rrd:usoRAM:AVERAGE",
                     "AREA:umbral50#FF9F00:Carga RAM mayor de 50",
                     "HRULE:40#FF0000:Umbral  40%",
                     "HRULE:60#DC143C:Umbral  60%",
                     "HRULE:75#5F9EA0:Umbral  75%")

while (1):
    ultima_actualizacionRAM = rrdtool.lastupdate(rrdpath + "trendRAM.rrd")
    timestamp=ultima_actualizacionRAM['date'].timestamp()
    datoRAM=ultima_actualizacionRAM['ds']["usoRAM"]
    if datoRAM> 40:
        generarGraficaRAM(int(timestamp))
        send_alert_attached("Sobrepasa el primer umbral de la RAM", 'usoRAM')
        print("sobrepasa el umbral de la RAM")
        
    if datoRAM> 60:
        generarGraficaRAM(int(timestamp))
        send_alert_attached("Sobrepasa el segundo umbral de la RAM", 'usoRAM')
        print("sobrepasa el umbral de la RAM")
        
    if datoRAM> 75:
        generarGraficaRAM(int(timestamp))
        send_alert_attached("Sobrepasa el tercer umbral de la RAM", 'usoRAM')
        print("sobrepasa el umbral de la RAM")
    time.sleep(20)

#############################################################################################################

def generarGraficaRED(ultima_lectura):
    tiempo_final = int(ultima_lectura)
    tiempo_inicial = tiempo_final - 1800
    retRED = rrdtool.graphv( imgpath+"traficoRED.png",
                     "--start",str(tiempo_inicial),
                     "--end",str(tiempo_final),
                     "--vertical-label=Trafico de red",
                    '--lower-limit', '0',
                    '--upper-limit', '100',
                    "--title=Uso del tràfico de red",
                    "DEF:traRED="+rrdpath+"trendRED.rrd:traRED:AVERAGE",
                     "AREA:traRED#00FF00:Trafico de red",
                     "HRULE:40#FF0000:Umbral  40%",
                     "HRULE:60#DC143C:Umbral  60%",
                     "HRULE:75#5F9EA0:Umbral  75%")

while (1):
    ultima_actualizacionRED = rrdtool.lastupdate(rrdpath + "trendRED.rrd")
    timestamp=ultima_actualizacionRED['date'].timestamp()
    datoRED=ultima_actualizacionRED['ds']["traRED"]
    
    if datoRED> 40:
        generarGraficaRED(int(timestamp))
        send_alert_attached("Sobrepasa el primer umbral del trafico de red", 'traficoRED')
        print("sobrepasa el umbral del trafico de red")
        
    if datoRED> 60:
        generarGraficaRED(int(timestamp))
        send_alert_attached("Sobrepasa el segundo umbral del trafico de red", 'traficoRED')
        print("sobrepasa el umbral del trafico de red")
    
    if datoRED> 75:
        generarGraficaRED(int(timestamp))
        send_alert_attached("Sobrepasa el tercer umbral del trafico de red", 'traficoRED')
        print("sobrepasa el umbral del trafico de red")
    
    time.sleep(20)

