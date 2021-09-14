import os
import time
import sys
from typing import Protocol

RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'

#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

os.system("clear")
os.system("figlet  JsHack En YT")

print (BLUE+""" 
´´´´´´´´´´´´´´´´´´´ ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´´`
´´´´´´´´´´´´´´´´´¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´
´´´´´´´´´´´´´´¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶´´´´´´´´´´´´´´
´´´´´´´´´´´´´¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´´
´´´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´
´´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´`´´´´´´´´´´´¶¶´´´´´´´´´´`
´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´
´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´´´´´´´´´´
´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶´´´´´´´´´´
´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶´´´´´´´´´´
´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´´´´´´´´´´
´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´
´´´´´´´´´´´¶¶´¶¶´´´¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶´´´¶¶´¶¶´´´´´´´´´´´
´´´´´´´´´´´´¶¶¶¶´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶´¶¶¶¶¶´´´´´´´´´´´
´´´´´´´´´´´´´¶¶¶´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶´¶¶¶´´´´´´´´´´´´´
´´´´¶¶¶´´´´´´´¶¶´´¶¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶¶¶´´¶¶´´´´´´¶¶¶¶´´´
´´´¶¶¶¶¶´´´´´¶¶´´´¶¶¶¶¶¶¶´´´¶¶¶´´´¶¶¶¶¶¶¶´´´¶¶´´´´´¶¶¶¶¶¶´´
´´¶¶´´´¶¶´´´´¶¶´´´´´¶¶¶´´´´¶¶¶¶¶´´´´¶¶¶´´´´´¶¶´´´´¶¶´´´¶¶´´
´¶¶¶´´´´¶¶¶¶´´¶¶´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´¶¶´´¶¶¶¶´´´´¶¶¶´
¶¶´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´¶¶
¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶´´´´¶¶¶¶¶¶¶´´´´¶¶¶¶¶¶¶¶´´´´´´¶¶¶¶¶¶¶¶
´´¶¶¶¶´¶¶¶¶¶´´´´´´¶¶¶¶¶´´´´´´´´´´´´´´¶¶¶´¶¶´´´´´¶¶¶¶¶¶´¶¶¶´
´´´´´´´´´´¶¶¶¶¶¶´´¶¶¶´´¶¶´´´´´´´´´´´¶¶´´¶¶¶´´¶¶¶¶¶¶´´´´´´´´
´´´´´´´´´´´´´´¶¶¶¶¶¶´¶¶´¶¶¶¶¶¶¶¶¶¶¶´¶¶´¶¶¶¶¶¶´´´´´´´´´´´´´´
´´´´´´´´´´´´´´´´´´¶¶´¶¶´¶´¶´¶´¶´¶´¶´¶´¶´¶¶´´´´´´´´´´´´´´´´´
´´´´´´´´´´´´´´´´¶¶¶¶´´¶´¶´¶´¶´¶´¶´¶´¶´´´¶¶¶¶¶´´´´´´´´´´´´´´
´´´´´´´´´´´´¶¶¶¶¶´¶¶´´´¶¶¶¶¶¶¶¶¶¶¶¶¶´´´¶¶´¶¶¶¶¶´´´´´´´´´´´´
´´´´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶´´´´´´´´´´´´´´´´´¶¶´´´´´´¶¶¶¶¶¶¶¶¶´´´´
´´´¶¶´´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´´´´¶¶´´´
´´´´¶¶¶´´´´´¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶´´´´´¶¶¶´´´´
´´´´´´¶¶´´´¶¶¶´´´´´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´´´´¶¶¶´´´¶¶´´´´´´
´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´
´´´´´´´¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶´´´´´´´""")

print (BLUE+"Autor: JsHack")
print (BLUE+"You Tube : https://m.youtube.com/channel/UC-Kz94tNfH4ued-Ux1p9VWg")
print (BLUE+"github   : https://github.com/jsh4ck ")

print(RED+"[1] Camaras de seguridad")
print(RED+"[2] Herramientas DDoS")
print(RED+"[3] Herramientas DE Rastrear")
opcion=input("\nElije una opcion: ")
if opcion=="1":
    os.system("clear")
    os.system("figlet CaM")
    print(GREEN+"""[1] Cam-Hacker
          
          
          Esta herramienta es para ver caramas 
          de seguridad de distintos paises.""")
    opcion=input("\nPreciona 1 y se descargara: ")
    if opcion=="1":
        os.system("pkg install git")
        os.system("pkg install python")
        os.system("git clone https://github.com/AngelSecurityTeam/Cam-Hackers")
        os.system("cd Cam-Hackers")
        os.system("ls")
        
        opcion=input("\nSeleccione :) ; ")
        if opcion=="1":
            os.system("clear")
            os.system("figlet DDoS")
            print(GREEN+"""[1] JsDDoS
                  
                  Esta herramienta de ddos esta hecha para
                  hacer ataques a sus propias [PAGINAS]
                  no me hago responsable del mal 
                  uso que le puedan dar""")
            
            
            
            
            print(GREEN+"""
                  
                  
                  
                  
                  
                  [2] XerXes
                  
                  Xerxes es una herramienta muy potente
                  CUANDO INSTALES LA HERRAMIENTA
                  LEEAN README ES MUY IMPORTANTE
                  """)
            
            
            print(GREEN+"""
                  
                  
                  
                  
                  
                  [3] Hammer
                  
                  Hammer es una herramienta de DoS
                  no es tan potente pero es funcional...""")
            
            print(GREEN+"""
                  
                  
            
            
                  
                  [4] Hulk
                  
                  hulk es una herramienta un Poco potente
                  pero funcionan ;)""")
            
            opcion=input("\nElije la opcion y se descargara: ")
            if opcion=="1":
                  os.system("clear")
                  os.system("pkg install git")
        os.system("pkg install python")
        os.system("git clone https://github.com/jsh4ck/DDoS")
        os.system("cd DDoS")
        os.system("ls")
        
        if opcion=="2":
                  os.system("clear")
                  os.system("pkg install git")
        os.system("pkg install python")
        os.system("git clone https://github.com/ngrock90/xerxes")
        os.system("cd xerxes")
        os.system("ls")
        
        if opcion=="3":
                  os.system("clear")
                  os.system("pkg install git")
        os.system("pkg install python")
        os.system("git clone https://github.com/rk1342k/Hammer")
        os.system("cd Hammer")
        os.system("ls")
        
        if opcion=="4":
                  os.system("clear")
                  os.system("pkg install git")
        os.system("pkg install python")
        os.system("git clone https://github.com/Mr4FX/HULK")
        os.system("cd HULK")
        os.system("ls")
        
        
        
        
        
        