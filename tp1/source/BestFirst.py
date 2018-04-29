#!/usr/bin/env python3

'''
Trabalho Pratico 1: Inteligência Artificial
Autor: Hugo Araujo de Sousa (2013007463)
BestFirst.py: Best first search.
'''


from GraphSearch import GraphSearch
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

		self.frontier = [Node(self.initial, None, None, 0)]
		return

	def add_to_frontier(self, node):
		'''
			Add a node to the frontier.

			@node: Node to add.
		'''

		# Find position to insert Node, in order to keep frontier sorted by
		# lowest to highest heuristic value.
		i = 0
		distance_node = self.manhattan_distance(node.state, self.goal)
		while i < len(self.frontier):
			distance_i = self.manhattan_distance(self.frontier[i].state,
				self.goal)

			if distance_node < distance_i:
				break
			i += 1

		self.frontier.insert(i, node)
		return

	def is_frontier_empty(self):
		'''
			Check if frontier is empty.
			
			@return: True, iff, frontier is empty.
		'''

		return len(self.frontier) == 0

	def is_in_frontier(self, node):
		'''
			Check if node is in frontier.

			@return: True, iff, node is in frontier.
		'''

		return node in self.frontier

	def get_next_node(self):
		'''
			Choose a leaf node and remove it from the frontier.

			@node: Next node in frontier to explore.
		'''

		return self.frontier.pop(0)