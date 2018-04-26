#!/usr/bin/env python3

'''
Trabalho Pratico 1: Inteligência Artificial
Autor: Hugo Araujo de Sousa (2013007463)
GraphSearch.py: Graph search template code.
'''


import numpy as np
import operator as op


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

		# Cost of each movement.
		self.costs = {
			'u': 1,
			'd': 1,
			'l': 1,
			'r': 1,
			'ul': 1.5,
			'ur': 1.5,
			'dl': 1.5,
			'dr': 1.5
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

	def is_in_frontier(self, node):
		'''
			Check if node is in frontier.

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

	def is_action_allowed(self, action, current):
		'''
			Check if an action is allowed.

			@action: (string) Action to check.
			@current: (int, int) Current position.
			@return: True, iff, the action is allowed.
		'''

		height = self.problem_map.height
		width = self.problem_map.width
		x = current[0]
		y = current[1]

		if action == 'u': # Up
			if x != 0:
				return True
		elif action == 'd': # Down
			if x != (height - 1):
				return True
		elif action == 'l': # Left
			if y != 0:
				return True
		elif action == 'r': # Right
			if y != (width - 1):
				return True
		elif action == 'ul': # Up and left
			if x != 0 and y != 0:
				cell_up = self.problem_map[x - 1, y]
				cell_left = self.problem_map[x, y - 1]

				if cell_up != '@' and cell_left != '@':
					return True
		elif action == 'ur': # Up and Right
			if x != 0 and y != (width - 1):
				cell_up = self.problem_map[x - 1, y]
				cell_right = self.problem_map[x, y + 1]

				if cell_up != '@' and cell_right != '@':
					return True
		elif action == 'dl': # Down and left
			if x != (height - 1) and y != 0:
				cell_down = self.problem_map[x + 1, y]
				cell_left = self.problem_map[x, y - 1]

				if cell_down != '@' and cell_left != '@':
					return True
		elif action == 'dr': # Down and right
			if x != (height - 1) and y != (width - 1):
				cell_down = self.problem_map[x + 1, y]
				cell_right = self.problem_map[x, y + 1]

				if cell_down != '@' and cell_down != '@':
					return True

		return False

	def expand_node(self, node):
		'''
			Expand the chosen node, adding the resulting nodes to the frontier.

			@node: Node to expand.
		'''

		current_state = node.state
		current_cost = node.cost

		for action in self.actions:
			if self.is_action_allowed(action, current_state):
				new_state = tuple(map(lambda x, y: x + y, current_state, 
					self.mov[action]))
				new_node = Node(new_state, node, action, current_cost)

				explored = self.explored[new_state]

				if not self.is_in_frontier(new_node) and not explored:
					self.add_to_frontier(new_node)

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

			if next_node.state == self.goal:
				return next_node.build_solution()

			self.set_explored(next_node)
			self.expand_node(next_node)

	def manhattan_distance(state1, state2):
		'''
			Calculate manhattan distance between two states.

			@state1: First state.
			@state2: Second state.
			@return: Manhattan distance between state1 and state2.
		'''

		return sum(tuple(map(lambda x, y: abs(x - y), state1, state2)))