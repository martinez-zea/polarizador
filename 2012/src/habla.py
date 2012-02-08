#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

class habla:
	def que(self,*args):
		"""
      Interactua con eSpeak el motor de TTS usado para el habla.
      La cadena de texto que recibe como argumento es pasada a un
      nuevo proceso del TTS con los parametros prestablecidos de 
      sintesis de voz.

      Arguments:
        *args: str

      Return:
        none
    """
		pid = os.fork()
		if not pid:
			os.execvp("espeak", ("espeak", "-v es-la+m2", "-k 20", "-s 140") +  args)
		return os.wait()[0]
    	

