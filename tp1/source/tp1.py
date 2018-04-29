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

import sys


# Arg indices.
MAP_ARG = 1

# Initial state
IX_ARG = 2
IY_ARG = 3

# Final state
FX_ARG = 4
FY_ARG = 5

# Search type
SEARCH_ARG = 6

HEURISTIC_ARG = 7

def main():
	'''
		Main program.
	'''

	# Check args
	if len(sys.argv) < SEARCH_ARG + 1:
		return

	problem_map = Map(sys.argv[MAP_ARG])
	initial_state = (int(sys.argv[IX_ARG]), int(sys.argv[IY_ARG]))
	final_state = (int(sys.argv[FX_ARG]), int(sys.argv[FY_ARG]))
	search_type = sys.argv[SEARCH_ARG]

	if search_type == 'bf': # Best first
		search = BestFirst(initial_state, final_state, problem_map)
	elif search_type == 'uc': # Uniform cost
		search = UniformCost(initial_state, final_state, problem_map)
	elif search_type == 'ids': # Iterative deepening depth-first
		pass
	elif search_type == 'astar': # A*
		# Check args
		if len(sys.argv) < HEURISTIC_ARG + 1:
			return

		heuristic = int(sys.argv[HEURISTIC_ARG])
		search = AStar(initial_state, final_state, problem_map, heuristic)
	else:
		return

	solution = search.start()
	search.print_path(solution)
	search.print_solution(solution)


main()