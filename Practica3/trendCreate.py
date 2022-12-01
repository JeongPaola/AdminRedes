import rrdtool
retCPU = rrdtool.create("/home/paola/Escritorio/AdminRedes/Practica3/RRD/trendCPU.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:usoCPU:GAUGE:60:U:U",
                     "RRA:AVERAGE:0.5:1:24")
if retCPU:
    print (rrdtool.error())
    
retRAM = rrdtool.create("/home/paola/Escritorio/AdminRedes/Practica3/RRD/trendRAM.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:usoRAM:GAUGE:60:U:U",
                     "RRA:AVERAGE:0.5:1:24")
if retRAM:
    print (rrdtool.error())

retRED = rrdtool.create("/home/paola/Escritorio/AdminRedes/Practica3/RRD/trendRED.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:traRED:GAUGE:60:U:U",
                     "RRA:AVERAGE:0.5:1:24")
if retRED:
    print (rrdtool.error())
