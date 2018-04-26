#!/usr/bin/env python3

'''
Trabalho Pratico 1: Inteligência Artificial
Autor: Hugo Araujo de Sousa (2013007463)
tp1.py:
'''

from BestFirst import BestFirst
from Map import Map

import sys


def main():
	'''
		Main program.
	'''

	# Check args
	if len(sys.argv) != 2:
		return

	problem_map = Map(sys.argv[1])
	bf = BestFirst((18, 90), (100, 100), problem_map)
	solution = bf.start()
	bf.print_path(solution)
	bf.print_solution(solution)


main()