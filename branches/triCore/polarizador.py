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
import peticion

h = habla.habla()
m = imprimeTicket.imprimeTicket()
p = peticion.peticion()

quienId = 0




################################################################################ Funcion Principal
def polariza():
	while 1:
		print 'Este es el polarizador'
		lcd = serial.Serial('/dev/ttyUSB2', 9600, timeout=None)
		lcd.write('3')
		print "escribi 3"
		lcd.close()
		print "cierro el serial"

		lector = serial.Serial('/dev/ttyUSB1', 9600, timeout=None)
		codigo = str(lector.readline())
		lector.close()
		print 'Usted es el visitante numero: ', codigo
		print 'Presione un boton para responder la pregunta'

		anteriores = p.buscaAnteriores(int(codigo))			
		
		while len(codigo) > 0:
			lcd = serial.Serial('/dev/ttyUSB2', 9600, timeout=None)
			lcd.write('2')
			lcd.close()
			
			botones = serial.Serial('/dev/ttyUSB0', 9600, timeout=None)
			h.que("Presione un boton, para contestar la pregunta")
			bots = int(botones.readline())
			botones.close() 
			
			
			lcd = serial.Serial('/dev/ttyUSB2', 9600, timeout=None)
			lcd.write('3')
			lcd.close()
			
			tiempo = datetime.datetime.now()
			fecha = tiempo.strftime("%Y/%m/%d")
			hora = tiempo.strftime("%H:%M:%S")
			
			if bots == 1:
				print "boton 2 presionado por ", codigo
				#cantaRespuesta1()
				
				p.guardaRespuesta(codigo,1, "si",hora,fecha)
				p.buscaRespuesta("no")
				print str(p.buscaPares("si"))
				h.que("Imprimiendo")
				m.imp(codigo,"SI",str(p.buscaPares("si")),"de acuerdo",str(anteriores))
				break

			if bots == 2:
				print "boton 3 presionado por ", codigo
				p.guardaRespuesta(codigo,1, "no",hora,fecha)
				p.buscaRespuesta("si")
				print str(p.buscaPares("no"))
				h.que("Imprimiendo")
				m.imp(codigo,"NO",str(p.buscaPares("no")),"en desacuerdo",str(anteriores))
				break
		#	print bots
if __name__ == '__main__': polariza()
