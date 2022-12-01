import time
import rrdtool
from getSNMP import consultaSNMP2
rrdpath = '/home/paola/Escritorio/AdminRedes/Practica3/RRD/'
carga_CPU = 0

while 1:
    usoCPU = int(consultaSNMP('comunidadASRWin','172.100.90.148','1.3.6.1.2.1.25.3.3.1.2.5'))
    usoRED = int(consultaSNMP('comunidadASRWin','172.100.90.148','1.3.6.1.2.1.6.10.0'))
    ramUSO = int(consultaSNMP('comunidadASRWin','172.100.90.148','1.3.6.1.2.1.25.2.3.1.6.3'))
    ramTot = int(consultaSNMP('comunidadASRWin','172.100.90.148','1.3.6.1.2.1.25.2.3.1.5.3'))
    redE = int(consultaSNMP('comunidadASRWin','172.100.90.148','1.3.6.1.2.1.2.2.1.10.15'))
    redS = int(consultaSNMP('comunidadASRWin','172.100.90.148','1.3.6.1.2.1.2.2.1.16.15'))
    c = int(consultaSNMP('comunidadASRWin','172.100.90.148','1.3.6.1.2.1.2.2.1.5.13'))
    
    usoRAM = int((ramUSO*100)/ramTot)
    traRED = int((redE+redS*8*100)/c)
    
    valorCPU = "N:" +str(usoCPU) 
    valorRAM = "N:" +str(usoRAM)
    valorRED = "N:"+ str(traRED)
    print (valorCPU + " " + valorRAM + " " + valorRED)
    
    rrdtool.update(rrdpath+'trendCPU.rrd', valorCPU)
    rrdtool.update(rrdpath+'trendRAM.rrd', valorRAM)
    rrdtool.update(rrdpath+'trendRED.rrd', valorRED)
    rrdtool.dump(rrdpath+'trendCPU.rrd',rrdpath+'trendCPU.xml')
    rrdtool.dump(rrdpath+'trendRAM.rrd',rrdpath+'trendRAM.xml')
    rrdtool.dump(rrdpath+'trendRED.rrd',rrdpath+'trendRED.xml')
    time.sleep(5)

if ret:
    print (rrdtool.error())
    time.sleep(300)
