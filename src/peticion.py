#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sqlite3 
import datetime

class Peticion:
	def __init__(self):
		
		self.id = None
	

	def ahora(self):
		""" 
		simple funcion que devuelve la hora y fecha formateados para la base de datos

		Parametros: Ninguno

		Ej: ahora()
		"""
		
		tiempo = datetime.datetime.now()
		fecha = tiempo.strftime("%Y/%m/%d")
		hora = tiempo.strftime("%H:%M:%S")
		return fecha, hora




	## Guarda el dato de la respuesta en la bd
	def guardaRespuesta(self, quien, pregunta,respuesta, hora, fecha):
		"""
		Guarda las respuestas en la base de datos

		Arguments:
		-quien: int, numero identificador del usuario
		-pregunta: int, numero identificador de la progunta, de 1 a 3.
		-respuesta: str, strng con la respuesta del usuario
		-hora : str, hora en formato: 'hh:mm:ss'
		-fecha: str, fecha en formato: 'aaaa/mm/dd'

		Ej: guardaRespuesta(101, 1, 'si', '01:10:45', '2009/01/25')
		
		""" 
	
		db = sqlite3.connect('pola.db')
		cursor = db.cursor()
		cursor.execute("insert into responde values(?, ?, ?, ?, ?, ?)", (self.id, quien, pregunta, respuesta, hora, fecha))
		db.commit()
		cursor.close

	################################################################################
	##############     PREGUNTAS A LA BD     #######################################
	################################################################################

	def buscaHora(self, quien):
		"""
		Retorna la hora de la ultimo acceso a la base de datos del usuaro con el numero quien

		Arguments:
		-quien: int, numero identificador del usuario

		Returns:
		-str, hora del ultimo acceso del usuario

		Ej: buscaHora(108)
		"""
		q = int(quien)
		db1 = sqlite3.connect("pola.db") ##conexion a la bd
		cursor1 = db1.cursor() ##crea cursor
		cursor1.execute("select hora quien from responde where quien = ?", (q,)) ##busca el ultimo registro	
		res = cursor1.fetchone() ##mete el resultado en fetch one
		print "lista tiene ",len(res), " elementos"		
		for i in res:
			print i[0]
		return str(res[0])

	def buscaFecha(self, quien):
		"""
		Retorna la fecha del ultimo acceso a la base de datos del usuario identificado con el numero quien, 

		Arguments:
		-quien: int, numero identificador del usuario

		Returns:
		-str, fecha del ultimo acceso del usuario a la base de datos

		Ej: buscaFecha(108)
		"""
		db1 = sqlite3.connect('pola.db') ##conexion a la bd
		cursor1 = db1.cursor() ##crea cursor
		cursor1.execute("select fecha from responde where quien = ?",(quien,)) ##busca el ultimo registro	
		res = cursor1.fetchone()
		print "la lista tiene ",len(res), " elementos"		
		for i in res:
			print i

		return str(res[0])

	def buscaRespuesta(self, pregnum, respuesta):
		"""
		Busca una respuesta en la base de datos contraria a la respusta en el parametro 'que', seleccionada aleatoriamente.  Luego pronuncia el resultado de la comparacion con speak.

		Arguments:
		-pregnum: int, numero de identificacion de la pregunta
		-respuesta: str, respuesta del usuario a ser comparada, debe ser 'si' o 'no'

		Returns: Numero de usuario en str

		Ej: buscaRespuesta(1, 'si')
		"""
		db1 = sqlite3.connect('pola.db')#conexion a la bd
		cursor1 = db1.cursor() ##crea cursor
		cursor1.execute("SELECT quien, respuesta FROM responde WHERE pregunta=? AND respuesta != ? order by random()" ,(pregnum,respuesta)) ##busca el ultimo registro
		row1 = cursor1.fetchone() ##mete el resultado en fetch one

		if row1:
			print row1[0], row1[1]
			return str(row1[0])		
		else:
			print 'Todos iguales'
			return '0'

	def buscaAnteriores(self, quien):

		"""
		Verifica el numero de veces que el usuario ha accedido anteriormente a la base de datos. Pronuncia la respuesta con speak

		Arguments:
		-quien: int, numero identificador del usuario

		Returns:
		-cuantos: numero de accesos del usuario a la base de datos

		Ej: buscaAnteriores(108)
		"""
		db = sqlite3.connect('pola.db')
		cursor = db.cursor()
		cursor = cursor.execute("select quien from responde where quien = ? ", (quien,))
		cuantos = cursor.fetchall()
		print len(cuantos)

		
		return len(cuantos)

	def buscaPares(self, preg, que):

		"""
		Retorna el numero de respuestas a la pregnta en el parametro 'preg' en la base de datos iguales a la respuesta en el parametro 'que'.

		Arguments:
		-preg: str, pregunta a ser comparada
		-que: str, respuesta a ser camparada

		Returns:
		-int, numero de respuestas iguales en la base de datos

		Ej: buscaPares(1, 'si')
		"""

		db1 = sqlite3.connect('pola.db') ##conexion a la bd
		cursor1 = db1.cursor() ##crea cursor
		cursor1.execute("select respuesta from responde where pregunta = ? and respuesta = ?", (preg, que,)) ##busca el ultimo registro	
		res = cursor1.fetchall()

		return len(res)

	def resPorPreg(self, preg):

		"""
		Retorna el numero de respuestas 'si' y 'no' por la preguta 'preg' en la base de datos

		Argumentos:
		-preg: int, numero de la pregunta, entre 1 y 3

		Retorna:
		-res: lista de dos elementos, numero de 'si' y 'no'

		Ej: resPorPreg(1)
		"""

		db = sqlite3.connect('pola.db')
		c = db.cursor()
		c.execute("select quien from responde where pregunta = ? and respuesta = 'si'", (preg,))
		row = c.fetchall()
		si = len(row)
		c.execute("select quien from responde where pregunta = ? and respuesta = 'no'", (preg,))
		row = c.fetchall()
		no = len(row)
		res = [si, no]
		return res


	def cuantPregs(self, preg):

		db = sqlite3.connect('pola.db')
		c = db.cursor()
		c.execute("select quien from responde where pregunta = ?", (preg,))
		row = c.fetchall()
		res = len(row)		

		return res

	def cuantUsers(self):
		db = sqlite3.connect('pola.db')
		c = db.cursor()
		c.execute("select * from responde")
		row = c.fetchall()
		res = len(row)

		return res
