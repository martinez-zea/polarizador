#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb 
import os 
import time
import habla

h = habla.habla()

## Habla con espeak
class peticion:
	
#	def __init__(self):
		
#		quienId = 0
	

	



	## Guarda el dato de la respuesta en la bd
	def guardaRespuesta(self, quien, respuesta):

		db = MySQLdb.connect(host="localhost", user="root", passwd="", db="panoptico")
		cursor = db.cursor()
		cursor.execute("INSERT INTO responde (quien,respuesta) VALUES (%s,%s)", (quien,respuesta))
		cursor.close

	################################################################################
	##############     PREGUNTAS A LA BD     #######################################
	################################################################################


	
	def buscaRespuesta(self, que):
		db1 = MySQLdb.connect(host="localhost", user="root", passwd="", db="panoptico") ##conexion a la bd
		cursor1 = db1.cursor() ##crea cursor
		cursor1.execute("SELECT quien, respuesta  FROM responde WHERE respuesta = %s ORDER BY rand()" ,(que)) ##busca el ultimo registro	
		row1 = cursor1.fetchone() ##mete el resultado en fetch one
		print row1[0], row1[1]
		
		h.que("Usted respondio lo contrario al visitante numero")
		h.que(str(row1[0]))
		#habla("espeak", "-ves",  "-s 135", row1[1])

	def buscaAnteriores(self,codigo):
		db = MySQLdb.connect(host="localhost", user="root", passwd="", db="polarizador")
		cursor = db.cursor()
		cuantos = cursor.execute("SELECT quien  FROM responde WHERE quien = %s ", (codigo))
		print cuantos
	
		if cuantos == 0:
			h.que("Esta es la primera vez que me visita")
			print "esta es la primera vez"
		
		if cuantos > 0:
			h.que("Usted me ha visitado")
			h.que(str(cuantos))
			h.que("veces")
			print "usted se he registrado",cuantos,"veces"

	def buscaPares(self, que):
		db1 = MySQLdb.connect(host="localhost", user="root", passwd="", db="panoptico") ##conexion a la bd
		cursor1 = db1.cursor() ##crea cursor
		cursor1.execute("SELECT respuesta  FROM responde WHERE respuesta = %s" ,(que)) ##busca el ultimo registro	
		columnas = int(cursor1.rowcount)
		return columnas
