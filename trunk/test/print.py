import os
import datetime

Num = 1
ticketNum = str(Num)

tiempo = datetime.datetime.now()
tiempoStr = tiempo.strftime("Fecha: %Y-%m-%d   Hora: %H:%M:%S")

imp = """ &%FW0 

          .Mms:.                        
          .Ms:smdo-                     
-hhhhhhhhhdMo   .+hmy/                 
          .Mo       -odds:             
          .Mo         ./mMdhhhhhhhhhhhh-
          .Mo      -+hms/              
 NNhhhhhhhhMo   /ymh+.                  
 Ny       .Mhodds:                      
 Ny        hy/                         
 Ny                                     
 y+                                     

&%FW1 
   El   POLARIZADOR 

TRANSFORMA SUS FLUJOS
DE OPINION EN UN 
UNICO ESTADO POLAR

&%FW0  
&%F1
--------------------------------------------
Corro sobre:

Ubuntu Gutsy GNU/Linux 7.10
Python 2.5.1
MySQL 5.0.45
eSpeak 1.29
Arduino Diecimilia
--------------------------------------------


Tiquete numero:"""+ticketNum+""" 

"""+tiempoStr+"""



********************************************
********************************************
*					   *
* Codigo			           *
*					   *
* Respuesta				   *
*					   *
*					   *
*					   *
* Ud. Piensa lo contrario que yo	   *
*					   *
********************************************
********************************************
&%FW1

Recuerde que usted 
SOLO puede estar
en PRO o en CONTRA
de mi opinion 
&%FW0 
http://nerdbots.info/polarizador

&%VT 
&%FC

"""
salida = open('/tmp/salida.txt','w')
salida.write(imp)	
salida.close()
os.system('cat /tmp/salida.txt > /dev/lp0')