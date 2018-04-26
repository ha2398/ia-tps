#!/usr/bin/env python3

'''
Trabalho Pratico 1: Inteligência Artificial
Autor: Hugo Araujo de Sousa (2013007463)
tp1.py:
'''

from Map import Map
import sys

def main():
	'''
		Main program.
	'''

	a = Map('../maps/map1.map')
	print(a.grid)


main()