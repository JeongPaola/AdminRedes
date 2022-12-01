import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from getSNMP import consultaSNMP2

COMMASPACE = ', '
# Define params
rrdpath = '/home/paola/Escritorio/AdminRedes/Practica3/RRD/'
imgpath = '/home/paola/Escritorio/AdminRedes/Practica3/IMG/'

mailsender = "dummycuenta3@gmail.com"
mailreceip = "innjeong73@gmail.com"
mailserver = 'smtp.gmail.com: 587'
password = 'dvduuffmlhspbmjj'
dispositivo = consultaSNMP2('comunidadASRWin','172.100.90.148','1.3.6.1.2.1.1.5.0')
software = consultaSNMP2('comunidadASRWin','172.100.90.148','1.3.6.1.2.1.1.1.0')
tiemposis = consultaSNMP2('comunidadASRWin','172.100.90.148','1.3.6.1.2.1.1.3.0')
comunidad = 'comunidadASRWin'

def send_alert_attached(subject, imagen):
    """ Envía un correo electrónico adjuntando la imagen en IMG
    """
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = mailsender
    msg['To'] = mailreceip
    m = msgdatos + '\n'
    msgdatos = "Los datos del equipo son los siguentes" + dispositivo + software + tiemposis + comunidad
    fp = open(imgpath+ imagen + '.png', 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    msg.attach(img)
    msg.attach(MIMEText(msgdatos, _charset='utf-8'))
    s = smtplib.SMTP(mailserver)

    s.starttls()
    # Login Credentials for sending the mail
    s.login(mailsender, password)

    s.sendmail(mailsender, mailreceip, msg.as_string())
    s.quit()
