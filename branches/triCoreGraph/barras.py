import sys
import cairo
import pycha.bar
import MySQLdb

##Se llama:
#b.barChart('preg4.png', pycha.bar.VerticalBarChart)
#b.barChart('preg4.png', pycha.bar.HorizontalBarChart)
class barras:
	def barChart(self, output, chartFactory):
		dbg = MySQLdb.connect(host="localhost", user="root", passwd="", db="polarizador") ##conexion a la bd
		cursorg = dbg.cursor() ##crea cursor
		cursorg.execute("SELECT DISTINCT quien  FROM responde ") ##busca los diferentes
		cuantos = int(cursorg.rowcount)

		cursorg.execute("SELECT respuesta  FROM responde ") ##busca cuantas respuestas hay	
		cuantasRespuestas = int(cursorg.rowcount)
		
		cursorg.execute("SELECT respuesta  FROM responde WHERE respuesta = 'si' ") ##busca cuantos SI	
		cuantosSi = int(cursorg.rowcount)
		
		cursorg.execute("SELECT respuesta  FROM responde WHERE respuesta = 'no' ") ##busca cuantos NO	
		cuantosNo = int(cursorg.rowcount)
		
		cursorg.execute("SELECT pregunta  FROM responde WHERE pregunta = '1' ") ##busca cuantas veces esta la pregunta 1	
		cuantosUno = int(cursorg.rowcount)
		
		cursorg.execute("SELECT pregunta  FROM responde WHERE pregunta = '2' ") ##busca cuantas veces esta la pregunta 2	
		cuantosDos = int(cursorg.rowcount)
		
		cursorg.execute("SELECT pregunta  FROM responde WHERE pregunta = '3' ") ##busca cuantas veces esta la pregunta 3	
		cuantosTres = int(cursorg.rowcount)
		
		cursorg.close()
		
		surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1024, 384)

		dataSet = (('visitante', [(0, cuantos), (1,cuantasRespuestas), (2,cuantosNo), (3,cuantosSi), (4,cuantosUno), (5,cuantosDos), (6,cuantosTres)]),)

		options = {
		    'axis': {
		        'x': {
		            'ticks': [{'label': 'Visitantes', 'v': 0}, {'label': 'CantidadRespuestas', 'v': 1}, {'label': 'CantidadNo', 'v': 2}, {'label': 'CantidadSi', 'v': 3} , {'label': 'CuantasVecesPreg1', 'v': 4}, {'label': 'CuantasVecesPreg2', 'v': 5}, {'label': 'CuantasVecesPreg3', 'v': 6}],
		            'rotate': 25,
		            'tickCount' : 2,
		            
		        },
		        'y': {
		            'tickCount': 10,
		            'rotate' : 25,
		            
		        }
		    },
		    'background': {
		        'chartColor': '#ffeeff',
		        'baseColor': '#ffffff',
		        'lineColor': '#444444'
		    },
		    'colorScheme': 'red',
		    'legend': {
		        'hide': True,
		    },
		    'padding': {
		        'left': 75,
		        'bottom': 85,
		        'right' : 75,
		    },
		    'colorScheme' : 'blue',
		}
		chart = chartFactory(surface, options)

		chart.addDataset(dataSet)
		chart.render()

		surface.write_to_png(output)

#if __name__ == '__main__':
#    output = sys.argv[1] if len(sys.argv) > 1 else 'barchart.png'
#    barChart('v' + output, pycha.bar.VerticalBarChart)
#    barChart('h' + output, pycha.bar.HorizontalBarChart)
