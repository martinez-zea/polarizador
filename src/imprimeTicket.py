#!/usr/bin/python2
# -*- coding: utf-8 -*-

import os
import datetime
from time import sleep


class imprimeTicket:
    def imp(self,codigo,respuesta,cuantos,acuerdo,veces, cualpreg):
        """
          Envia el texto formateado a la impresora directamente por el
          puerto serial. El control y formato de los textos es generado usando
          los comandos ESC/POS soportados por la impresora EPSON TMU200.
          Estos se envian codificados en caracteres hexadecimales.

          Argumentos:
            codigo: int
            respuesta: str
            cuantos: int
            acuerdo: str
            veces: int
            cualpreg: int
        """ 
        barcode = codigo
        cualPregunta = " "
					
        tiempo = datetime.datetime.now()
        tiempoStr = tiempo.strftime("Fecha: %Y/%m/%d   Hora: %H:%M:%S")

        os.system('echo -e "\x1B\x40" > /dev/ttyS0')
        os.system('echo -e "\x1B\x47\x31" > /dev/ttyS0')
        os.system('cat templates/header.txt > /dev/ttyS0')
        os.system('cat templates/deco1.txt > /dev/ttyS0')

        vis = "Visitante numero: %s" %(barcode)
        vez = "Usted me ha visitado %s veces" %(veces)
		
        os.system('echo  "'+vis+'" > /dev/ttyS0')
        os.system('echo  "'+tiempoStr+'" > /dev/ttyS0')
        os.system('echo  "'+vez+'" > /dev/ttyS0')

        os.system('cat templates/deco2.txt > /dev/ttyS0')
        os.system('cat templates/deco3.txt > /dev/ttyS0')
		
        resp = "Usted respondio: "+respuesta
        acu = "Usted esta deacuerdo con %s" %(cuantos)
        visi = "de los visitantes"

        opi = "Usted esta "+acuerdo+" conmigo"
		
        print cualPregunta
        #os.system('echo "'+cualPregunta+'" > /dev/ttyS0')
        
        if cualpreg == 1:
            os.system('echo "Cree usted que los medios de " > /dev/ttyS0')
            os.system('echo "comunicacion son opositores al " > /dev/ttyS0')
            os.system('echo "gobierno?" > /dev/ttyS0')
            os.system('echo "\n" > /dev/ttyS0')
		
        if cualpreg == 2:
            os.system('echo "Cree usted que el arte en el " > /dev/ttyS0')
            os.system('echo "Ecuador debe estar ligado a la" > /dev/ttyS0')
            os.system('echo "labor social?" > /dev/ttyS0')
            os.system('echo "\n" > /dev/ttyS0')
		
        if cualpreg == 3:
            os.system('echo "Deberia usted tener acceso" > /dev/ttyS0')
            os.system('echo "a la informacion de otros?" > /dev/ttyS0')
            os.system('echo "\n" > /dev/ttyS0')

        os.system('echo "'+resp+'" > /dev/ttyS0')
        os.system('echo "\n" > /dev/ttyS0')
        os.system('echo "'+acu+'" > /dev/ttyS0')
        os.system('echo "\n" > /dev/ttyS0')
        os.system('echo "'+visi+'" > /dev/ttyS0')
        os.system('echo "\n" > /dev/ttyS0')
        os.system('echo "'+opi+'" > /dev/ttyS0')

        os.system('cat templates/deco4.txt > /dev/ttyS0')
		
        os.system('echo -e "\x1B\x61\x31" > /dev/ttyS0')
        os.system('echo -e "Reuerde que usted SOLO puede estar DE ACUERDO o en DESACUERDO con mi opinion" > /dev/ttyS0')
		
        sleep(7)

        os.system('echo -e "\x1B\x61\x30" > /dev/ttyS0')
        os.system('cat templates/footer.txt > /dev/ttyS0')
        os.system('echo -e "\x1D\x56\x41" > /dev/ttyS0')

