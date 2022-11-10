import time
import rrdtool
from getSNMP import consultaSNMP

#paq_uni_interfaz = 0
#paq_ipv4_err = 0
#mens_icmp_agen = 0
#nseg_err = 0
#data_udp = 0

while 1:
    paq_uni_interfaz = int(consultaSNMP('EsmeraldaZP','192.168.243.230',
                                          '1.3.6.1.2.1.2.2.1.11.1'))
    paq_ipv4_err = int(consultaSNMP('EsmeraldaZP','192.168.243.230',
                                           '1.3.6.1.2.1.4.3.0'))
    mens_icmp_agen = int(consultaSNMP('EsmeraldaZP','192.168.243.230',
                                            '1.3.6.1.2.1.5.21.0'))
    nseg_err = int(consultaSNMP('EsmeraldaZP','192.168.243.230',
                                            '1.3.6.1.2.1.6.10.0'))
    data_udp = int(consultaSNMP('EsmeraldaZP','192.168.243.230',
                                            '1.3.6.1.2.1.7.1.0'))

    valor = "N:" + str(paq_uni_interfaz) + ':' + str(paq_ipv4_err) + ':' + str(mens_icmp_agen) + ':' + str(nseg_err) + ':' + str(data_udp)
    print (valor)
    rrdtool.update('traficoRED.rrd', valor)
    rrdtool.dump('traficoRED.rrd','traficoRED.xml')
    time.sleep(1)

if ret:
    print (rrdtool.error())
    time.sleep(300)
