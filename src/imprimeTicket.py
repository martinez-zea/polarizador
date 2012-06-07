#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import datetime
from time import sleep


class imprimeTicket:
    def imp(self,codigo,respuesta,cuantos,acuerdo,veces, cualpreg):
      """
          Envia el texto formateado a la impresora directamente por el
          puerto serial. El control y formato de los textos es generado usando
          los comandos ESC/POS soportados por la impresora EPSON TMU200.
          Estos se envian codificados en caracteres hexadecimales.

          Argumentos:
            codigo: int
            respuesta: str
            cuantos: int
            acuerdo: str
            veces: int
            cualpreg: int
      """ 
          #self.imprimeTicket()
		cualPregunta = ""
		if cualpreg == "1":
			cualPregunta = """
La conciencia de ser observado aumenta 
su sensacion de seguridad?
		"""
		if cualpreg == "2":
			cualPregunta = """
Estar en una base de datos 
es pertenecer a una comunidad?
		"""
		if cualpreg == "3":
			cualPregunta = """
Deberia usted tener acceso 
a la informacion de otros? 
		"""
				
		tiempo = datetime.datetime.now()
		tiempoStr = tiempo.strftime("Fecha: %Y/%m/%d   Hora: %H:%M:%S")

    printer = os.popen('lpr', 'w')
		printer.write(""" 
\x1B\x40
\x1B\x47\x31
 .......................  _  | .....
 ....................... (/_ | ..... 
 ...................................
 ._   _  |  _. ._ o _   _.  _|  _  ._ 
 |_) (_) | (_| |  | /_ (_| (_| (_) |  
 | .................................  
 ...................................
                  :
                  :
 :::::::::::::::::::::::::::::::::::::
  :TRANSFORMA SUS FLUJOS DE OPINION :
  :    EN UN UNICO ESTADO POLAR     :
 :::::::::::::::::::::::::::::::::::::
 """)
    printer.close()
    sleep(3)

    printer = os.popen('lpr', 'w')
    printer.write("""                  
__/\__________________________________/\__

 Visitante numero:"""+codigo+""" 
 """+tiempoStr+"""
 Usted me ha visitado """+veces+""" veces
__  __________________________________  __
  \/                                  \/
  """)  
    printer.close()
    sleep(2)

    printer = os.popen('lpr', 'w')  
    printer.write("""
_ __ _ __:__ __/\  _______________________
                 \/                        
 A la pregunta: 
 """+cualPregunta+"""      
 Usted respondio: """+respuesta+"""

 Usted esta deacuerdo con """+cuantos+"""
 de los visitantes

 Usted esta """+acuerdo+""" conmigo
_____ _ __ ___ __  _ _________________\ \>
""")
    printer.close()
    sleep(3)

    printer = os.popen('lpr', 'w')
    printer.write("""
\x1B\x61\x31
Recuerde que usted SOLO puede estar en PRO o en CONTRA de mi opinion
\x1B\x61\x30      .
____              .                   ____
\___|http://nerdbots.info/polarizador|___/      
                  .
\x1D\x56\x41
""")
    printer.close()
