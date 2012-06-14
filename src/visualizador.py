#!/usr/bin/python2
from peticion import Peticion
import matplotlib.pyplot as plt
import numpy

class Visualizador:

  """
  API de visualizacion del polarizador, usa matplotlib y peticion
  """

  def __init__(self):
    """
    Instancia la clase, intancia los objetos necesarios 

    """
    self.plot = plt	
    self.pet = Peticion()
    self.np = numpy

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
    #f = self.plot.figure(figsize = (10.24, 7.68))
    self.plot.figure(figsize = (10.24, 7.68))
    self.plot.subplot(231)		
    tit = 'La conciencia de ser observado \n aumenta su sensacion de seguridad ?'
    self.plot.title(tit, fontsize = 10)
    self.plot.pie(self.pet.resPorPreg(1), colors=('k', 'w'), labels=('si', 'no'), labeldistance = 1.2)
    
    self.plot.subplot(232)
    tit = 'Estar en una base de datos \n es pertenecer a una comunidad ?'
    self.plot.title(tit, fontsize = 10)
    self.plot.pie(self.pet.resPorPreg(2), colors=('k', 'w'), labels=('si', 'no'), labeldistance = 1.2)

    self.plot.subplot(233)
    tit = 'Deberia usted tener acceso \n a la informacion de otros ?'
    self.plot.title(tit, fontsize = 10)
    self.plot.pie(self.pet.resPorPreg(3), colors=('k', 'w'), labels=('si', 'no'), labeldistance = 1.2)
    #self.plot.figure(2)
    self.plot.subplot(234)
    #self.plot.title('promedio de preguntas')
    self.plot.axes([0.05, 0.05, 0.8, 0.45] )
    total = self.pet.cuantUsers()	
    pregs = [total, self.pet.cuantPregs(1), self.pet.cuantPregs(2), self.pet.cuantPregs(3)]
    self.plot.bar(self.np.arange(4), pregs, width = 0.5, color='k', align = 'center')
    self.plot.xticks([0, 1, 2, 3], ('Total', 'preg. uno', 'preg. dos', 'preg. tres'))	
    
    self.plot.yticks(self.np.arange(0, total, 10))
    #self.plot.ylabel('Preguntas')
    self.plot.savefig('todo.png')	
    #self.plot.show()
