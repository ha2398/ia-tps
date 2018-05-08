#!/usr/bin/env python3

'''
Trabalho Pratico 1: Inteligência Artificial
Autor: Hugo Araujo de Sousa (2013007463)
tp1.py:
'''

from AStar import *
from BestFirst import *
from IDS import *
from Map import *
from UniformCost import *

import argparse


parser = argparse.ArgumentParser()
parser.add_argument('map', type=str, help='Map to perform the search on.')
parser.add_argument('ix', type=int, help='x coordinate of the initial state')
parser.add_argument('iy', type=int, help='y coordinate of the initial state')
parser.add_argument('fx', type=int, help='x coordinate of the goal state')
parser.add_argument('fy', type=int, help='y coordinate of the goal state')
parser.add_argument('search', type=str, help='Search type.')
parser.add_argument('-he', dest='h_number', type=int,
	help='Heuristic to use with A*.')
parser.add_argument('-d', '--debug', action='store_true',
	help='Debug mode. Prints extra information.')

args = parser.parse_args()

HEURISTIC = {1: 'manhattan', 2: 'octile'}

def main():
	'''
		Main program.
	'''

	problem_map = Map(args.map)
	initial_state = (args.ix, args.iy)
	final_state = (args.fx, args.fy)
	search_type = args.search

	if search_type == 'bf': # Best first
		search = BestFirst(initial_state, final_state, problem_map)
	elif search_type == 'uc': # Uniform cost
		search = UniformCost(initial_state, final_state, problem_map)
	elif search_type == 'ids': # Iterative deepening depth-first
		search = IDS(initial_state, final_state, problem_map)
	elif search_type == 'astar': # A*
		heuristic = HEURISTIC[args.h_number]
		search = AStar(initial_state, final_state, problem_map, heuristic)
	else:
		return

	solution = search.start()
	search.print_solution(solution)

	if (args.debug):
		search.print_path(solution)
		print('Expanded nodes:', search.expanded)
		print('Runtime:', search.runtime)


main()