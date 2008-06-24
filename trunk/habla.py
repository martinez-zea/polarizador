#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

class habla:
	def __init__(self,*args):
		"""Interactua con espeak, espera recibir algo como habla("que va a decir") """
		pid = os.fork()
		if not pid:
			os.execvp("espeak", ("espeak", "-ves") +  args)
			os.wait()[0]
    	

