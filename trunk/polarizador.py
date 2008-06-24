#!/usr/bin/python
#          .Mms:.                        
#          .Ms:smdo-                     
#-hhhhhhhhhdMo   .+hmy/                 
#          .Mo       -odds:             
#          .Mo         ./mMdhhhhhhhhhhhh-
#          .Mo      -+hms/              
# NNhhhhhhhhMo   /ymh+.                  
# Ny       .Mhodds:                      
# Ny        hy/                         
# Ny                                     
# y+
#http://nerdbots.info/polarizador
#Camilo Martinez <cmart AT decoloector DOT net>
#Gabriel Zea <zea AT randomlab DOT net>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 2 of the License.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.




import MySQLdb 
import os 
import datetime
import serial
import sys
import time

import imprimeTicket
import habla

quienId = 0



## Guarda el dato de quien llega y toma un id
def guardaLlegada():
	""" Guarda la hora de llegada de un visitante al tomar la tarjeta con el 
	codigo de barras """
	global quienId
	quienId = quienId + 1	
	
	tiempo = datetime.datetime.now()
	tiempoStr = tiempo.strftime("%Y-%m-%d-%H-%M-%S")
	
	db = MySQLdb.connect(host="localhost", user="root", passwd="", db="panoptico")
	cursor = db.cursor()	
	cursor.execute("INSERT INTO llega (quien,hora) VALUES (%s,%s)", (quienId,tiempoStr))
	cursor.close()

## Guarda el dato de la respuesta en la bd
def guardaRespuesta(quien, respuesta):

		db = MySQLdb.connect(host="localhost", user="root", passwd="", db="panoptico")
		cursor = db.cursor()
		cursor.execute("INSERT INTO responde (quien,respuesta) VALUES (%s,%s)", (quien,respuesta))
		cursor.close

################################################################################
##############     PREGUNTAS A LA BD     #######################################
################################################################################

def cantaRespuesta1():
	db2 = MySQLdb.connect(host="localhost", user="root", passwd="", db="panoptico") ##conexion a la bd
	cursor2 = db2.cursor() ##crea cursor
	cursor2.execute("SELECT LAST_INSERT_ID()  FROM responde") ##busca el ultimo registro
	columnas2 = int(cursor2.rowcount) ##mira cuantos rows hay
	cursor2.execute("SELECT *  FROM responde WHERE ID = %s" ,(columnas2))## hace el query preguntando por el ultimo registro del Id
	row2 = cursor2.fetchone() ##mete el resultado en fetch one
	print "ID: ", row2[0], "quien: ", row2[1], "resp: ", row2[2]
	
	h=habla.habla("El visistante, numero.")
	h=habla.habla(str(row2[1]))
	h=habla.habla("respondio que .")			
	h=habla.habla(row2[2])	
	
def buscaRespuesta(que):
	db1 = MySQLdb.connect(host="localhost", user="root", passwd="", db="panoptico") ##conexion a la bd
	cursor1 = db1.cursor() ##crea cursor
	cursor1.execute("SELECT quien, respuesta  FROM responde WHERE respuesta = %s ORDER BY rand()" ,(que)) ##busca el ultimo registro	
	row1 = cursor1.fetchone() ##mete el resultado en fetch one
	print row1[0], row1[1]
	h=habla.habla("Uste respondio lo contrario al visitante numero")
	h=habla.habla(str(row1[0]))
	#h=habla.habla("espeak", "-ves",  "-s 135", row1[1])

def buscaPares(que):
	db1 = MySQLdb.connect(host="localhost", user="root", passwd="", db="panoptico") ##conexion a la bd
	cursor1 = db1.cursor() ##crea cursor
	cursor1.execute("SELECT respuesta  FROM responde WHERE respuesta = %s" ,(que)) ##busca el ultimo registro	
	columnas = int(cursor1.rowcount)
	return columnas
	

################################################################################ Funcion Principal
def polariza():
	while 1:
		print 'Este es el polarizador'

		lector = serial.Serial('/dev/ttyUSB1', 9600, timeout=None)

		codigo = str(lector.readline())
		#print codigo
		lector.close()

		print codigo
		while len(codigo) > 0:
			time.sleep(0.5)
			h=habla.habla("Presione un boton, para contestar la pregunta")
			#h=habla.habla("respondio que .")	
			botones = serial.Serial('/dev/ttyUSB0', 9600, timeout=None)
			bots = int(botones.readline())
			botones.close() 
		

			if bots == 2:
				print "boton 2 presionado por ", codigo
				#cantaRespuesta1()
				guardaRespuesta(codigo, "si")
				buscaRespuesta("no")
				print str(buscaPares("si"))
				h1=habla.habla("Imprimiendo")
				imprime = imprimeTicket.imprimeTicket(codigo,"SI",str(buscaPares("si")),"de acuerdo")
				break

			if bots == 3:
				print "boton 3 presionado por ", codigo
				guardaRespuesta(codigo, "no")
				buscaRespuesta("si")
				print str(buscaPares("no"))
				h2=habla.habla("Imprimiendo")
				imprime = imprimeTicket.imprimeTicket(codigo,"NO",str(buscaPares("no")),"en desacuerdo")
				break
		#	print bots
if __name__ == '__main__': polariza()
