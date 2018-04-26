#!/usr/bin/env python3

'''
Trabalho Pratico 1: Inteligência Artificial
Autor: Hugo Araujo de Sousa (2013007463)
GraphSearch.py: Graph search template code.
'''


import numpy as np


class GraphSearch():

	def __init__(self, initial, goal, problem_map):
		'''
			Initialize the graph search for a problem.

			@initial: Initial state of the problem.
			@goal: Goal state of the problem.
			@map: Map to perform the search on.
		'''

		self.initial = initial
		self.goal = goal
		self.problem_map = problem_map
		self.explored = None
		self.frontier = None

		# up, down, left, right, up and left, up and right, down and left,
		# down and right.
		self.actions = ['u', 'd', 'l', 'r', 'ul', 'ur', 'dl', 'dr']

		# Indicates how to move in the grid according to the actions.
		self.mov = {
			'u': (-1, 0),
			'd': (1, 0),
			'l': (0, -1),
			'r': (0, 1),
			'ul': (-1, -1),
			'ur': (-1, 1),
			'dl': (1, -1),
			'dr': (1, 1)
		}

		return

	def init_explored(self):
		'''
			Initialize the explored nodes set of the problem.
		'''

		# Each position is indicated as explored (1) or not explored (0).
		height = self.problem_map.height
		width = self.problem_map.width
		self.explored = np.zeros(height * width, dtype=int)
		self.explored.shape = (height, width)

		return

	def init_frontier(self):
		'''
			Initialize the search frontier using the initial state of the
			problem.

			(to be implemented in child classes)
		'''

		pass

	def add_to_frontier(self, node):
		'''
			Add a node to the frontier.

			(to be implemented in child classes)
		'''

		pass

	def is_frontier_empty(self):
		'''
			Check if frontier is empty.

			(to be implemented in child classes)
		'''

		return False

	def get_next_node(self):
		'''
			Choose a leaf node and remove it from the frontier.

			(to be implemented in child classes)
		'''

		return None

	def set_explored(self, node):
		'''
			Set a node as explored.

			@node: Node to set as explored.
		'''

		x, y = node.state
		self.explored[x, y] = 1

		return

	def expand_node(self, node):
		'''
			Expand the chosen node, adding the resulting nodes to the frontier.

			@node: Node to expand.
		'''

		# TODO

		return

	def start(self):
		'''
			Perform the graph search.

			@return: List wth sequence of Nodes, from initial to goal, in case
				of success. None otherwise.
		'''

		self.init_explored()
		self.init_frontier()

		while True:
			if self.is_frontier_empty(): # Failure
				return None

			next_node = self.get_next_node()

			if next_node.equals(self.goal):
				return next_node.build_solution()

			self.set_explored(next_node)
			self.expand_node(next_node)