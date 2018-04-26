#!/usr/bin/env python3

'''
Trabalho Pratico 1: Inteligência Artificial
Autor: Hugo Araujo de Sousa (2013007463)
tp1.py:
'''

from Map import Map
import sys


def print_usage():
	'''
		Print program usage.
	'''

	print('tp1.py <map_file>')
	return


def main():
	'''
		Main program.
	'''

	# Check args
	if len(sys.argv) != 2:
		print_usage()
		return

	a = Map(sys.argv[1])
	print(a.grid)


main()