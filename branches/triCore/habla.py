#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

class habla:
	def que(self,*args):
		"""Interactua con espeak, espera recibir algo como habla("que va a decir") """
		pid = os.fork()
		if not pid:
			os.execvp("espeak", ("espeak", "-ves") +  args)
		return os.wait()[0]
    	

