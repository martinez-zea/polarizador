#!/usr/bin/python2
# -*- coding: utf-8 -*-

from espeak import espeak

class habla:
	def que(self,sentence):
		"""
      Interactua con eSpeak el motor de TTS usado para el habla.

      La cadena de texto que recibe como argumento es pasada a un
      nuevo proceso del TTS con los parametros prestablecidos de 
      sintesis de voz.

	  Usa python-espeak: https://answers.launchpad.net/python-espeak

      Arguments:
        *args: str

      Return:
        none
    """
		espeak.set_voice("es-la+m2")
		espeak.set_parameter(espeak.Parameter.Capitals,20)
		espeak.set_parameter(espeak.Parameter.Rate, 140)
		espeak.synth(sentence)
    	

