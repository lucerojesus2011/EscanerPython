import os
import sys
import platform
import socket
from datetime import datetime

def testPuertoTcp(ip): #Funcion para puertos TCP



    portBasic = {'FTP File Transfer Protocol' : 21,'SSH, scp, SFTP' : 22,'Telnet ' : 23,'SMTP Simple Mail Transfer Protocol' : 25,'HTTP HyperText Transfer Protocol' :80,'POP3 Post Office Protocol' : 110,'HTTPS/SSL' : 443}

    for port in portBasic:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        it = portBasic[port]
        result = sock.connect_ex((str(ip), it))
        if result == 0:
            print("       "+str(portBasic[port]) + "      "+port)

def obtenerIp():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(("google.com", 80))
        return s.getsockname()[0]



print("\n")
print("          █▀▀ ▄▀▀ ▄▀▀ ▄▀▄ █▄ █ █▀▀ █▀▄   █▀▄ █▀▀   █▀▄ █▀▀ █▀▄")
print("          █▀▀  ▀▄ █   █▄█ █▀██ █▀▀ █▀▄   █ █ █▀▀   █▀▄ █▀▀ █ █")
print("          ▀▀▀ ▀▀   ▀▀ ▀ ▀ ▀  ▀ ▀▀▀ ▀ ▀   ▀▀  ▀▀▀   ▀ ▀ ▀▀▀ ▀▀ ")
print("               ▀▀ PROGRAMADO POR JESUS ADRIAN LUCERO ▀▀""\n")




ip = obtenerIp()
ipDividida = ip.split('.')
portBasic = [21,22,23,25,80,110,443]



try:
    red = ipDividida[0] + '.' + ipDividida[1] + '.' + ipDividida[2] + '.'
    comienzo = 1
    fin = 254
except:
    print("[!] Error")
    sys.exit(1)

if (platform.system() == "Windows"):
    ping = "ping -n 1"
else:
    ping = "ping -c 1"

tiempoInicio = datetime.now()
print("----------------------------------------------------------------------------------")
print("--------- Escaneando la red desde la ip ", red + str(comienzo), "hasta", red + str(fin)+" ---------")
print("----------------------------------------------------------------------------------""\n")


for subred in range(comienzo, fin + 1):
    direccion = red + str(subred)
    response = os.popen(ping + " " + direccion)
    for line in response.readlines():
        if ("ttl" in line.lower()):
            print("\n")
            print("       ==================")
            print("          "+direccion)
            print("       ==================")
            print("\n")
            testPuertoTcp(direccion)
            break

tiempoFinal = datetime.now()
tiempo = tiempoFinal - tiempoInicio
print("[*] El escaneo ha durado %s" % tiempo)