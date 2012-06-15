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

import sys
import datetime
import logging
from time import sleep
from random import randint
from threading import Thread, Event

import pygame
from  serial import Serial

#polarizador modules
from habla import habla
from peticion import Peticion
from imprimeTicket import imprimeTicket
from visualizador import Visualizador


#Logging configuration
logging.basicConfig(level = logging.DEBUG,
		 format = '(%(threadName)-10s) %(message)s',)

#serial ports (QuitoVersion)
LCD = '/dev/ttyACM1'
BARCODE_READER = '/dev/ttyACM0'
BUTTONS = '/dev/ttyUSB0'

BAUD_RATE = 9600

QUESTIONS = {
		'q1': 'Cree usted que los medios de comunicacion son opositores al gobierno?',
		'q2': 'Cree usted que el arte en el Ecuador debe estar ligado a la labor social?',
		'q3': 'El arte bla?',
		}

SENTENCES = {
		'whoami' : 'soy el polarizador',
		'identify' : 'identifiquese usando su codigo de barras',
		'answer' : 'Responda la siguiente pregunta',
		'firstTime': 'Esta es la primera vez que me visita',
		'previous' : 'Usted me ha visitado',
		'oneTime' : 'vez',
		'many': 'veces',
		'push': 'Presione un boton para responder la pregunta',
		'opposite': 'Usted respondio lo contrario al visitante',
		'printing': 'imprimiendo',
        'ticket':'Retire su recibo',
		'thanks': 'Gracias por usarme',
		}

class GraphGenerator(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.name = 'GraphGenerator'
        self.engine = Visualizador()
        
        logging.debug('GraphGenerator started')
        
    def run(self):
        self.engine.todo()

class UserInteraction(Thread):
    def __init__(self, userCode, lcdThread, speechThread, graphThread):
        Thread.__init__(self)
        self.name = 'UserInteraction'
        self.dataBase = Peticion()
        self.txt2spch = habla()
        self.printer = imprimeTicket()
        self.userCode = userCode
        #self.infoGraph = Visualizador(engine='Agg')
        self.infoGraph = graphThread
        self.lcd = lcdThread
        self.speech = speechThread
		
        logging.debug('User interaction started')

    def run(self):
        self.speech.waiting = True
        previuosVisits = self.dataBase.buscaAnteriores(int(self.userCode))
        logging.debug('previous visits: %s',previuosVisits)

        if previuosVisits == 0:
            self.txt2spch.que(SENTENCES['firstTime'])
        elif previuosVisits >0 :
            self.txt2spch.que(SENTENCES['previous'])
            self.txt2spch.que(str(previuosVisits))
            if previuosVisits == 1:
                self.txt2spch.que(SENTENCES['oneTime'])
            else:
                self.txt2spch.que(SENTENCES['many'])
		sleep(3)		
		self.txt2spch.que(SENTENCES['answer'])
		sleep(3)

		question = randint(1,3)
		if question == 1:
			self.lcd.write('1')
			self.txt2spch.que(QUESTIONS['q1'])
		elif question == 2:
			self.lcd.write('2')
			self.txt2spch.que(QUESTIONS['q2'])
		elif question == 3:
			self.lcd.write('3')
			self.txt2spch.que(QUESTIONS['q3'])
		
		sleep(3)

        buttons = Serial(BUTTONS, 9600, timeout=None)
        self.lcd.write('4')
        self.txt2spch.que(SENTENCES['push'])
        answer = buttons.readline()
        buttons.close()
        logging.debug('answer: %s',answer)

        now = datetime.datetime.now()
        date = now.strftime("%Y/%m/%d")
        time = now.strftime("%H:%M:%S")
		
        if int(answer) == 2:
            self.dataBase.guardaRespuesta(self.userCode,question,"si",time,now)
            opposite = self.dataBase.buscaRespuesta(question, "no")
            self.txt2spch.que(SENTENCES['opposite'])
            self.txt2spch.que(opposite)
            self.txt2spch.que(SENTENCES['printing'])
            self.printer.imp(self.userCode,"SI",
					str(self.dataBase.buscaPares(question,"si")),
					"de acuerdo",
					str(previuosVisits), 
					question)
			
			#self.infoGraph.todo()
            self.infoGraph.run()

            self.lcd.write('5')
            self.txt2spch.que(SENTENCES['ticket'])
            sleep(3)
            self.txt2spch.que(SENTENCES['thanks'])

            self.lcd.write('6')
			
            sleep(5)
            self.speech.waiting = False
		
        if int(answer) == 1:
            self.dataBase.guardaRespuesta(self.userCode,question,"no",time,now)
            opposite = self.dataBase.buscaRespuesta(question, "si")
            self.txt2spch.que(SENTENCES['opposite'])
            self.txt2spch.que(opposite)
            self.txt2spch.que(SENTENCES['printing'])
            self.printer.imp(self.userCode,"NO",
					str(self.dataBase.buscaPares(question,"si")),
					"de acuerdo",
					str(previuosVisits), 
					question)

            #self.infoGraph.todo()
            self.infoGraph.run()
			
            self.lcd.write('5')
            self.txt2spch.que(SENTENCES['ticket'])
            sleep(3)
            self.txt2spch.que(SENTENCES['thanks'])
			#self.txt2spch.que(SENTENCES['whoami'])
            self.lcd.write('6')
            
            sleep(5)
            self.speech.waiting = False

class Speech(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.name = 'Speech'
		self.loop = Event()
		self.txt2spch = habla()
		self.waiting = False
		logging.debug('Speech thread initialized')


	def run(self):
		while not self.loop.is_set():
			if not self.waiting:
				#logging.debug('--- onWaiting')
				self.helloWorld()
				self.loop.wait(randint(30,90))
			else:
				#logging.debug('*** on')
				self.loop.wait(0.01)

	def helloWorld(self):
		logging.debug('helloWorld')

		self.txt2spch.que(SENTENCES['whoami'])
		self.txt2spch.que(SENTENCES['identify'])

	def quit(self):
		self.loop.set()

class Render(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.name = 'Render'
		self.loop = Event()
		
		width = 1024
		height = 768
		pygame.init()
		self.screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN, 32)
		#self.screen = pygame.display.set_mode((width, height), pygame.RESIZABLE, 32)

		logging.debug('Render thread initialized')

	def run(self):
		while not self.loop.is_set():
			img = pygame.image.load('todo.png').convert()
			self.screen.blit(img, (0, 0))
			pygame.display.flip()
			self.loop.wait(2)

	def quit(self):
		self.loop.set()

class LcdWriter(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.name = 'LcdWriter'
		self.lcd = Serial(LCD, 9600, timeout=None)
		self.loop = Event()

	def run(self):
		while not self.loop.is_set():
			self.loop.wait(0.1)

	def write(self,msg):
		self.lcd.write(msg)
		logging.debug('lcd msg: %s',msg)
	
	def quit(self):
		self.lcd.close()
		self.loop.set()

def main():
	try:
		reader =  Serial(BARCODE_READER, BAUD_RATE, timeout=None)
		code = None
		
		speech = Speech()
		speech.start()
		#speech.helloWorld()
		
		lcd = LcdWriter()
		lcd.start()
		lcd.write('6')
		
		graph = GraphGenerator()

		viz = Render()
		viz.start()

		while True:
			code = reader.readline()
			if code is not None:
				logging.debug('barcode: %s', code)
				interact = UserInteraction(code,lcd,speech,graph)
				interact.run()
				code = None

			sleep(0.01)
	
	except KeyboardInterrupt:
		"""
		End threads and exit main program
		"""
		reader.close()
		
		speech.quit()
		speech.join()
		graph.quit()
		grapht.join()
		viz.quit()
		viz.join()
		lcd.quit()
		lcd.join()

		sys.exit(1)

	except Exception, err:
		logging.debug('Ups::  %s',err)

if __name__ == '__main__': 
	main()
