#!/usr/bin/env python3

'''
Trabalho Pratico 1: Inteligência Artificial
Autor: Hugo Araujo de Sousa (2013007463)
PointGen.py: Point generator to run
'''

from random import *
import sys

seed()

num_points = int(sys.argv[1])

for i in range(num_points):
	for j in range(4):
		print(randint(0, 255), end=' ')

	print()