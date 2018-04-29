#!/usr/bin/env python3

'''
Trabalho Pratico 1: Inteligência Artificial
Autor: Hugo Araujo de Sousa (2013007463)
AStar.py: A* graph search. Two available heuristics: Manhattan and Octile.
'''


from GraphSearch import GraphSearch
from Node import Node


class AStar(GraphSearch):

	def __init__(self, initial, goal, problem_map, heuristic):
		'''
			Initialize the A* graph search for a problem.

			@initial: Initial state of the problem.
			@goal: Goal state of the problem.
			@problem_map: Map to perform the search on.
			@heuristic: Heuristic to use.
				1: Manhattan.
				2: Octile.
		'''
		super().__init__(initial, goal, problem_map)
		self.heuristic = heuristic
		return

	def heuristic_value(self, node):
		'''
			Calculate the heuristic value for a node.

			@node: Node to calculate the heuristic value for.
			@return: h(n), heuristic value.
		'''

		if self.heuristic == 1: # Mahattan
			return self.manhattan_distance(node.state, self.goal)
		elif self.heuristic == 2: # Octile
			return self.octile_distance(node.state, self.goal)
		else:
			return float('inf')

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
		# lowest to highest f(n) = g(n) + h(n).
		i = 0
		while i < len(self.frontier):
			fn_node = node.cost + self.heuristic_value(node)
			fn_i = self.frontier[i].cost + \
				self.heuristic_value(self.frontier[i])

			if fn_node < fn_i:
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