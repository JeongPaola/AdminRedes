from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A3
from getSNMP import consultaSNMP
import datetime

hoy = datetime.datetime.now()

pdf = canvas.Canvas("Administracion de contabilidad de mi compañero.pdf", pagesize = A3)
pdf.setTitle("Reporte de contabilidad")
cont = pdf.beginText(100,1150)
cont.setFont("Times-Roman", 18)
cont.textLine("Administraciòn de servicios en Red")
cont.textLine("Practica 2")
cont.textLine("Reporte de contabilidad")
cont.setFont("Helvetica", 16)
cont.textLine("Jeong Paola")
cont.textLine("Trafico de red")
cont.textLine("")

cont.setFont("Helvetica", 14)
cont.textLine("version: 1")
cont.textLine("device: server3")
cont.textLine("description: Accounting Server 3")
cont.textLine("date: "+str(hoy))
cont.textLine("defaultProtocol: radius")
cont.textLine("")

cont.textLine("rdate: "+str(hoy))

inoctets = int(consultaSNMP('comunidadSNMP','localhost','1.3.6.1.2.1.2.2.1.10.1'))
cont.textLine("#Acct-Input-Octets: "+str(inoctets))

outoctets = int(consultaSNMP('comunidadSNMP','localhost','1.3.6.1.2.1.2.2.1.16.1'))
cont.textLine("#Acct-Output-Octets: "+str(outoctets))

inpack = int(consultaSNMP('comunidadSNMP','localhost','1.3.6.1.2.1.4.8.0'))
cont.textLine("#Acct-Input-Packets: "+str(inpack))

outpack = int(consultaSNMP('comunidadSNMP','localhost','1.3.6.1.2.1.4.9.0'))
cont.textLine("#Acct-Output-Packets: "+str(outpack)) 

sestime= int(consultaSNMP('comunidadSNMP','localhost','1.3.6.1.2.1.1.3.0'))
cont.textLine("#Acct-Session-Time: "+str(sestime)) 

cont.textLine("")
pdf.drawImage("/home/paola/Escritorio/AdminRedes/Practica2/img1.png",150,650)
pdf.drawImage("/home/paola/Escritorio/AdminRedes/Practica2/img2.png",150,460)
pdf.drawImage("/home/paola/Escritorio/AdminRedes/Practica2/img3.png",150,280)
pdf.drawImage("/home/paola/Escritorio/AdminRedes/Practica2/img4.png",150,100)
#pdf.drawImage("/home/paola/Escritorio/AdminRedes/Practica2/img5.png",150,800)

pdf.drawText(cont)
pdf.save()
