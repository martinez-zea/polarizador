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




import sql3    
import os 
import datetime
import serial
import sys
import time
import random as r
#import pycha
#import pycha.bar
#import pycha.pie

import imprimeTicket
import habla
import peticion
import tortas
import barras

h = habla.habla()
m = imprimeTicket.imprimeTicket()
p = peticion.peticion()
t = tortas.tortas()
b = barras.barras()

quienId = 0		

################################################################################ Funcion Principal
def polariza():
	while 1:
		h.que("Soy el Polarizador")
		print 'Este es el polarizador'
		lcd = serial.Serial('/dev/ttyUSB2', 9600, timeout=None)
		lcd.write('4')
		print "escribi 4"
		lcd.close()
		print "cierro el serial"

		lector = serial.Serial('/dev/ttyUSB1', 9600, timeout=None)
		codigo = str(lector.readline())
		lector.close()
		print 'Usted es el visitante numero: ', codigo
		print 'Presione un boton para responder la pregunta'

		anteriores = p.buscaAnteriores(int(codigo))			
		
		while len(codigo) > 0:
			pregnum = str(r.randint(1,3))
			lcd = serial.Serial('/dev/ttyUSB2', 9600, timeout=None)
			lcd.write(pregnum)
			lcd.close()
			
			if pregnum == 1:
			h.que('La conciencia de ser observado, aumenta su sensacion de seguridad?')
			if cualpreg == 2:
			h.que('Estar en una base de datos, es pertenecer a una comunidad?')
			if cualpreg == 3:
			h.que('Deberia usted tener acceso, a la informacion de otros?')
			
			botones = serial.Serial('/dev/ttyUSB0', 9600, timeout=None)
			h.que("Presione un boton, para contestar la pregunta")
			bots = int(botones.readline())
			botones.close() 
			
			
			lcd = serial.Serial('/dev/ttyUSB2', 9600, timeout=None)
			lcd.write('4')
			lcd.close()
			
			tiempo = datetime.datetime.now()
			fecha = tiempo.strftime("%Y/%m/%d")
			hora = tiempo.strftime("%H:%M:%S")
			
			if bots == 2:
				print "boton 2 presionado por ", codigo
				#cantaRespuesta1()
				
				p.guardaRespuesta(codigo,1,"si",hora,fecha)
				p.buscaRespuesta("no")
				print str(p.buscaPares("si"))
				h.que("Imprimiendo")
				m.imp(codigo,"SI",str(p.buscaPares("si")),"de acuerdo",str(anteriores), pregnum)
				h.que("Gracias por usarme")
				#dibuja charts
				t.pieChart('preg1.png', 1, 'red')
				t.pieChart('preg2.png', 2, 'green')
				t.pieChart('preg3.png', 3, 'grey')
				b.barChart('preg4.png', pycha.bar.VerticalBarChart)
				break

			if bots == 1:
				print "boton 1 presionado por ", codigo
				p.guardaRespuesta(codigo,1, "no",hora,fecha)
				p.buscaRespuesta("si")
				print str(p.buscaPares("no"))
				h.que("Imprimiendo")
				m.imp(codigo,"NO",str(p.buscaPares("no")),"en desacuerdo",str(anteriores), pregnum)
				h.que("Gracias por usarme")
				#dibuja charts
				t.pieChart('preg1.png', 1, 'red')
				t.pieChart('preg2.png', 2, 'green')
				t.pieChart('preg3.png', 3, 'grey')
				b.barChart('preg4.png', pycha.bar.VerticalBarChart)
				
				break
		#	print bots
if __name__ == '__main__': polariza()
