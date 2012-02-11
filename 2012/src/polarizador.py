#!/usr/bin/python2
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
#http://martinez-zea.info/
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





import datetime
import serial
import random as r
import pygame
from pygame.locals import *

#import pycha
#import pycha.bar
#import pycha.pie

#import imprimeTicket
import habla
import peticion
import visualizador
#import tortas
#import barras

h = habla.habla()
#m = imprimeTicket.imprimeTicket()
p = peticion.Peticion()
v = visualizador.Visualizador(engine='Agg')
#t = tortas.tortas()
#b = barras.barras()

width = 1024
height = 768

size = width, height


quienId = 0

#serial ports
lcd_port = '/dev/ttyACM0'
reader_port = '/dev/ttyACM1'
buttons_port = '/dev/ttyUSB0'

#LCD messages
lcd_msgs = {'question1':'1',
			'question2':'2',
			'question3':'3',
			'button':'4',
			'thanks':'5',
			'elPola':'6',
			}

def lcd_com(msg):
	"""
		Escribe el mensaje necesario al puerto
		serial para controlar el LCD
	"""
	print '--- LCD init ---'
	lcd = serial.Serial(lcd_port, 9600, timeout=None)
	lcd.write(msg)
	print 'msg: %s' %msg
	lcd.close()
	print '--- LCD end ---'

def elPola():
	"""
		Dice el mensaje de inicio
	"""
	h.que('Soy el Polarizador')
	lcd_com(lcd_msgs['elPola'])
	h.que('Identifiquese usando su codigo de barras')
	print '*** elPola ***'

def bar_reader():
	"""
		Escucha el puerto serial en busca del
		codigo de barras entregado por el lector

		return: el codigo
	"""
	print '--- Barcode reader ---'
	reader = serial.Serial(reader_port, 9600, timeout=None)
	code = str(reader.readline())
	print 'barcode: %s' %code
	reader.close()
	print '--- Barcode end ---'
	
	return code

################################################################################ Funcion Principal
def polariza():
	while 1:
		elPola()	

		#actualiza la visualizacion
		v.todo()
		sc = pygame.display.set_mode((size), FULLSCREEN, 32)
		back = pygame.Surface(sc.get_size())
		back = back.convert()
		back.fill((255, 255, 255))
		sc.blit(back, (0, 0))
		sc.blit(back, (0, 0))
		img = pygame.image.load('todo.png')
		sc.blit(img, (0, 0))
		pygame.display.flip()
		print "displayed" 

		barcode = bar_reader()
		
		other_interactions = p.buscaAnteriores(int(barcode))
		if other_interactions  == 0:
			h.que("Esta es la primera vez que me visita")
			print "primera vez"

		elif other_interactions > 0:
			h.que("Usted me ha visitado")
			h.que(str(other_interactions))
			if other_interactions == 1:
				h.que('vez')
			else:	
				h.que("veces")
			print "el visitante se ha registrado %s veces" % (other_interactions)
	

		while len(barcode) > 0:
			pregnum = r.randint(1,3)
			if pregnum == 1:
				lcd_com(lcd_msgs['question1'])
				h.que('La conciencia de ser observado, aumenta su sensacion de seguridad?')
			elif pregnum == 2:
				lcd_com(lcd_msgs['question2'])
				h.que('Estar en una base de datos, es pertenecer a una comunidad?')
			elif pregnum == 3:
				lcd_com(lcd_msgs['question3'])
				h.que('Deberia usted tener acceso, a la informacion de otros?')

			
			botones = serial.Serial(buttons_port, 9600, timeout=None)
			h.que("Presione un boton, para contestar la pregunta")
			bots = botones.readline()
			botones.close()
			

			lcd_com(lcd_msgs['elPola'])

			tiempo = datetime.datetime.now()
			fecha = tiempo.strftime("%Y/%m/%d")
			hora = tiempo.strftime("%H:%M:%S")

			if int(bots) == 2:
				print "boton 2 presionado por %s", barcode

				p.guardaRespuesta(barcode,pregnum,"si",hora,fecha)
				opposite = p.buscaRespuesta(pregnum, "no")
				h.que("Usted respondio lo contrario al visitante numero")
				h.que(opposite)
				print str(p.buscaPares(pregnum,"si"))

				h.que("Imprimiendo")
				#m.imp(codigo,"SI",str(p.buscaPares("si")),"de acuerdo",str(anteriores), pregnum)
				#h.que("Gracias por usarme")
				#dibuja charts
				#t.pieChart('preg1.png', 1, 'red')
				#t.pieChart('preg2.png', 2, 'green')
				#t.pieChart('preg3.png', 3, 'grey')
				#b.barChart('preg4.png', pycha.bar.VerticalBarChart)
				break

			if int(bots) == 1:
				print "boton 1 presionado por ", barcode

				p.guardaRespuesta(barcode,pregnum, "no",hora,fecha)
				opposite = p.buscaRespuesta(pregnum, "si")
				h.que("Usted respondio lo contrario al visitante numero")
				h.que(opposite)
				print str(p.buscaPares(pregnum, "no"))
				
				h.que("Imprimiendo")
				#m.imp(codigo,"NO",str(p.buscaPares("no")),"en desacuerdo",str(anteriores), pregnum)
				#h.que("Gracias por usarme")
				#dibuja charts
				#t.pieChart('preg1.png', 1, 'red')
				#t.pieChart('preg2.png', 2, 'green')
				#t.pieChart('preg3.png', 3, 'grey')
				#b.barChart('preg4.png', pycha.bar.VerticalBarChart)

				break
if __name__ == '__main__': polariza()
