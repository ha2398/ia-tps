#!/usr/bin/env python3

'''
Trabalho Pratico 1: Inteligência Artificial
Autor: Hugo Araujo de Sousa (2013007463)
UniformCost.py: Uniform cost search.
'''


from GraphSearch import GraphSearch
from Node import Node


class UniformCost(GraphSearch):

	def __init__(self, initial, goal, problem_map):
		'''
			Initialize the uniform cost graph search for a problem.

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
		# lowest to highest path cost.
		i = 0
		for i in range(len(self.frontier)):
			path_cost_node = node.cost
			path_cost_i = self.frontier[i].cost

			if path_cost_node < path_cost_i:
				break

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