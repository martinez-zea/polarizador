#!/usr/bin/python
import sys
from peticion import Peticion

class Visualizador:

	"""
	API de visualizacion del polarizador, usa matplotlib y peticion
	"""

	def __init__(self, engine='GTKAgg'):
		"""
		Instancia la clase, intancia los objetos necesarios 
	
		"""
		
		"""
		### carga y descarga dinamica de matplotlib, para cambiar de backend, no funciona 

		try: 
			sys.modules["matplotlib"]
			del sys.modules["matplotlib"]
			#del plt
			#del matplotlib
			print 'matplotlib removido'
				
			import matplotlib
			matplotlib.use(engine)
			import matplotlib.pyplot
			print 'matplotlib recargado'

		except KeyError:
			
			import matplotlib
			matplotlib.use(engine)
			import matplotlib.pyplot
			print 'matplotlb cargado'
		"""
		import matplotlib
		matplotlib.use(engine)
		import matplotlib.pyplot
		#import matplotlib.figure
		#import matplotlib.axes
	


		self.plot = matplotlib.pyplot	
		self.pet = Peticion()


	def torta(self, preg):
		"""
		Crea graficos de torta para la pregunta en el parametro 'preg', usa sa funcion resPorPreg() del API de l abase de datos en peticiqn.py para obtener los datos, realiza el grafico de torta y lo exporta al directorio actual con el nombre 'torta_numpreg.png
		
		Argumentos:
		-preg: int, numero de la preguneta a ser graficada

		Returns: Nada
		"""
		fn = 'torta_%s.png' %preg
		self.plot.axes([0, 0, 0.5, 0.6])
		tit = 'pregunta %s' %preg
		self.plot.title(tit)
		self.plot.pie(self.pet.resPorPreg(preg), colors=('k', 'w'), labels=('si', 'no'))
		self.plot.savefig(fn)
		self.plot.show()


	def barras(self):
		"""
		Crea graficos de barras para la cantidad de preguntas en el parametro 'cant',Usa la funcion cuantasPreg() del API de la base de datos en peticion.py para obtener los datos
		"""

		pregs = [self.pet.cuantUsers(), self.pet.cuantPregs(1), self.pet.cuantPregs(2), self.pet.cuantPregs(3)]
		self.plot.bar([0, 1, 2, 3], pregs) 
		self.plot.savefig('barras.png')
		self.plot.show()

	def todo(self):
		#self.plot.figure(1)
		self.plot.subplot(231)
		tit = 'pregunta 1'
		self.plot.title(tit)
		self.plot.pie(self.pet.resPorPreg(1), colors=('k', 'w'), labels=('si', 'no'))

		self.plot.subplot(232)
		tit = 'pregunta 2'
		self.plot.title(tit)
		self.plot.pie(self.pet.resPorPreg(2), colors=('k', 'w'), labels=('si', 'no'))

		self.plot.subplot(233)
		tit = 'pregunta 3'
		self.plot.title(tit)
		self.plot.pie(self.pet.resPorPreg(3), colors=('k', 'w'), labels=('si', 'no'))
		#self.plot.figure(2)
		#self.plot.subplot(234)
		self.plot.axes([0.1, 0.05, 0.8, 0.45])
		pregs = [self.pet.cuantUsers(), self.pet.cuantPregs(1), self.pet.cuantPregs(2), self.pet.cuantPregs(3)]
		self.plot.bar([0, 1, 2, 3], pregs) 
		self.plot.savefig('todo.png')	
		self.plot.show()
