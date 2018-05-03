#!/usr/bin/env python3

'''
Trabalho Pratico 1: Inteligência Artificial
Autor: Hugo Araujo de Sousa (2013007463)
BestFirst.py: Best first search.
'''


from GraphSearch import GraphSearch
from heapq import *
from Node import Node


class BestFirst(GraphSearch):

	def __init__(self, initial, goal, problem_map):
		'''
			Initialize the best first graph search for a problem.

			Heuristic: Manhattan.

			@initial: Initial state of the problem.
			@goal: Goal state of the problem.
			@map: Map to perform the search on.
		'''
		super().__init__(initial, goal, problem_map)
		return

	def init_frontier(self):
		'''
			Initialize the search frontier using the initial state of the
			problem.
		'''

		first_node = Node(self.initial, None, None, 0)
		distance = self.manhattan_distance(self.initial, self.goal)
		self.frontier = [(distance, first_node)]
		return

	def add_to_frontier(self, node):
		'''
			Add a node to the frontier.

			@node: Node to add.
		'''

		if self.is_in_frontier[node.state] or self.explored[node.state]:
			return					

		distance = self.manhattan_distance(node.state, self.goal)
		heappush(self.frontier, (distance, node))
		self.is_in_frontier[node.state] = 1

		return

	def is_frontier_empty(self):
		'''
			Check if frontier is empty.
			
			@return: True, iff, frontier is empty.
		'''

		return len(self.frontier) == 0

	def get_next_node(self):
		'''
			Choose a leaf node and remove it from the frontier.

			@node: Next node in frontier to explore.
		'''

		return heappop(self.frontier)[1]