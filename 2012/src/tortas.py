import sys
import cairo
import pycha.pie
import pycha.color
import MySQLdb

## llamar t.pieChart('preg1.png', 1, 'red')

class tortas:
	def pieChart(self,output,pregunta,colSch):
		
		db1 = MySQLdb.connect(host="localhost", user="root", passwd="", db="polarizador") ##conexion a la bd
		cursor1 = db1.cursor() ##crea cursor
		cursor1.execute("SELECT pregunta, respuesta  FROM responde WHERE pregunta = %s AND respuesta = 'si'", (pregunta)) ##busca el ultimo registro	
		cuantosSi = int(cursor1.rowcount)
		cursor1.execute("SELECT pregunta, respuesta  FROM responde WHERE pregunta = %s AND respuesta = 'no'", (pregunta)) ##busca el ultimo registro	
		cuantosNo = int(cursor1.rowcount)
		cursor1.close()
		
		surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 341, 384)

		dataSet = [('si', [[0, cuantosSi]]), ('no', [[0, cuantosNo]])]
	
		options = {
			'axis': {
				'x': {
				    'ticks': [{'label': 'si', 'v': 0}, {'label': 'no', 'v': 1}],
				}
			},
			'background': {
				'hide': True,
			},
			'padding': {
				'left': 40,
				'right': 50,
				'top': 30,
				'bottom': 30,
			},
			'legend': {
				'hide': True,
			},
			'colorScheme' : colSch,
		
		}
		chart = pycha.pie.PieChart(surface, options)
		chart.addDataset(dataSet)
		chart.render()

		surface.write_to_png(output)



