
#!/usr/bin/env python
import rrdtool

ret = rrdtool.create("traficoRED.rrd",
                     "--start",'N',
                     "--step",'300',
                     "DS:paq_uni_interfaz:COUNTER:122:U:U",
                     "DS:paq_ipv4_err:COUNTER:122:U:U",
                     "DS:mens_icmp_agen:COUNTER:122:U:U",
                     "DS:nseg_err:COUNTER:122:U:U",
                     "DS:data_udp:COUNTER:122:U:U",
                     "RRA:AVERAGE:0.5:5:150",
                     "RRA:AVERAGE:0.5:5:150",
                     "RRA:AVERAGE:0.5:5:150",
                     "RRA:AVERAGE:0.5:5:150",
                     "RRA:AVERAGE:0.5:5:150")

if ret:
    print (rrdtool.error())
