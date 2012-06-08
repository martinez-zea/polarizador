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
from time import sleep
from random import randint
from  serial import Serial
import logging
from threading import Thread, Event, Lock

#polarizador modules
from habla import habla
from peticion import Peticion
from imprimeTicket import imprimeTicket

#TODO: import visualizador

#Logging configuration
logging.basicConfig(level = logging.DEBUG,
		 format = '(%(threadName)-10s) %(message)s',)

#serial ports (QuitoVersion)
lcd_port = '/dev/ttyACM1'
BARCODE_READER = '/dev/ttyACM0'
BUTTONS = '/dev/ttyUSB0'

BAUD_RATE = 9600

QUESTIONS = {
		'q1': 'La conciencia de ser observado, aumenta su sensacion de seguridad?',
		'q2': 'Estar en una base de datos, es pertenecer a una comunidad?',
		'q3': 'Deberia usted tener acceso, a la informacion de otros?',
		}

SENTENCES = {
		'firstTime': 'Esta es la primera vez que me visita',
		'previous' : 'Usted me ha visitado',
		'oneTime' : 'vez',
		'many': 'veces',
		'push': 'Presione un boton para responder la pregunta',
		'opposite': 'Usted respondio lo contrario al visitante',
		'printing': 'imprimiendo',
		}

class UserInteraction(Thread):
	def __init__(self, userCode):
		Thread.__init__(self)
		self.name = 'UserInteraction'
		self.dataBase = Peticion()
		self.txt2spch = habla()
		self.printer = imprimeTicket()
		self.userCode = userCode

	def run(self):
		previuosVisits = self.dataBase.buscaAnteriores(int(self.userCode))
		logging.debug('previous visits: %s',previuosVisits)

		if previuosVisits == 0:
			self.txt2spch.que(SENTENCES['firstNime'])
		elif previuosVisits >0 :
			self.txt2spch.que(SENTENCES['previous'])
			self.txt2spch.que(str(previuosVisits))
			if previuosVisits == 1:
				self.txt2spch.que(SENTENCES['oneTime'])
			else:
				self.txt2spch.que(SENTENCES['many'])

		question = randint(1,3)
		if question == 1:
			self.txt2spch.que(QUESTIONS['q1'])
		elif question == 2:
			self.txt2spch.que(QUESTIONS['q2'])
		elif question == 3:
			self.txt2spch.que(QUESTIONS['q3'])

		buttons = Serial(BUTTONS, 9600, timeout=None)
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
		
		if int(answer) == 1:
			self.dataBase.guardaRespuesta(self.userCode,question,"no",time,now)
			opposite = self.dataBase.buscaRespuesta(question, "si")
			self.txt2spch.que(SENTENCES['opposite'])
			self.txt2spch.que(opposite)
			self.txt2spch.que(SENTENCES['printing'])
			self.printer.imp(self.userCode,"SI",
					str(self.dataBase.buscaPares(question,"si")),
					"de acuerdo",
					str(previuosVisits), 
					question)

class BarcodeReader(Thread):
	def __init__(self, serialPort, baudRate):
		Thread.__init__(self)
		self.name = 'BarcodeReader'
		self.reader = Serial(BARCODE_READER, BAUD_RATE, timeout=None)
		self.loop = Event()
		self.gotCode = False
		
		logging.debug('barcode thread initialized')

	def run(self):
		while not self.loop.is_set():
			self.gotCode = False
			code = self.reader.readline()
			self.gotCode = True
			
			interact = UserInteraction(code)
			interact.run()

			logging.debug('barcode: %s',code)

			self.loop.wait(0.01)

	def quit(self):
		self.reader.close()
		self.loop.set()

class Speech(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.name = 'Speech'
		self.loop = Event()
		self.txt2spch = habla()
		logging.debug('Speech thread initialized')

	def run(self):
		while not self.loop.is_set():
			print 'work on me!!'
			self.loop.wait(1)

	def helloWorld(self):
		logging.debug('helloWorld')

		self.txt2spch.que('Soy el polarizador')
		self.txt2spch.que('Identifiquese usando su codigo de barras')

	def quit(self):
		self.loop.set()

def main():
	try:
		barReader = BarcodeReader(BARCODE_READER,BAUD_RATE)
		barReader.start()
		
		speech = Speech()
		speech.start()
		speech.helloWorld()

		while True:
			sleep(0.01)
	
	except KeyboardInterrupt:
		"""
		End threads and exit main program
		"""
		barReader.quit()
		barReader.join()
		
		speech.quit()
		speech.join()

		sys.exit(1)

	except Exception, err:
		logging.debug('Ups::  %s',err)

if __name__ == '__main__': 
	main()
