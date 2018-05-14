#!/usr/bin/env python3

'''
Trabalho Pratico 1: Inteligência Artificial
Autor: Hugo Araujo de Sousa (2013007463)
GraphSearch.py: Graph search template code.
'''


from Node import Node

import numpy as np
import time


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
		self.is_in_frontier = None
		self.expanded = 0
		self.runtime = 0

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
		self.is_in_frontier = np.zeros(height * width, dtype=int)
		self.explored.shape = (height, width)
		self.is_in_frontier.shape = (height, width)

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

	def is_action_allowed(self, action, current):
		'''
			Check if an action is allowed.

			@action: (string) Action to check.
			@current: (int, int) Current position.
			@return: True, iff, the action is allowed.
		'''

		height = self.problem_map.height
		width = self.problem_map.width
		grid = self.problem_map.grid
		x, y = current

		if action == 'u': # Up
			if x != 0 and grid[x - 1, y] != '@':
				return True
		elif action == 'd': # Down
			if x != (height - 1) and grid[x + 1, y] != '@':
				return True
		elif action == 'l': # Left
			if y != 0 and grid[x, y - 1] != '@':
				return True
		elif action == 'r': # Right
			if y != (width - 1) and grid[x, y + 1] != '@':
				return True
		elif action == 'ul': # Up and left
			if x != 0 and y != 0 and grid[x - 1, y - 1] != '@':
				cell_up = grid[x - 1, y]
				cell_left = grid[x, y - 1]

				if cell_up != '@' and cell_left != '@':
					return True
		elif action == 'ur': # Up and Right
			if x != 0 and y != (width - 1) and grid[x - 1, y + 1] != '@':
				cell_up = grid[x - 1, y]
				cell_right = grid[x, y + 1]

				if cell_up != '@' and cell_right != '@':
					return True
		elif action == 'dl': # Down and left
			if x != (height - 1) and y != 0 and grid[x + 1, y - 1] != '@':
				cell_down = grid[x + 1, y]
				cell_left = grid[x, y - 1]

				if cell_down != '@' and cell_left != '@':
					return True
		elif action == 'dr': # Down and right
			if x != (height - 1) and y != (width - 1) and \
				grid[x + 1, y + 1] != '@':

				cell_down = grid[x + 1, y]
				cell_right = grid[x, y + 1]

				if cell_down != '@' and cell_right != '@':
					return True

		return False

	def expand_node(self, node):
		'''
			Expand the chosen node, adding the resulting nodes to the frontier.

			@node: Node to expand.
		'''

		current_state = node.state
		current_cost = node.cost
		self.expanded += 1

		for action in self.actions:
			if self.is_action_allowed(action, current_state):
				new_state = tuple(map(lambda x, y: x + y, current_state, 
					self.mov[action]))
				new_cost = current_cost + self.costs[action]
				new_node = Node(new_state, node, action, new_cost)

				self.add_to_frontier(new_node)

		return

	def start(self):
		'''
			Perform the graph search.

			@return: List wth sequence of Nodes, from initial to goal, in case
				of success. None otherwise.
		'''

		self.runtime = time.process_time()

		if  self.problem_map.grid[self.initial] == '@' or \
			self.problem_map.grid[self.goal] == '@':
			solution = None

			self.runtime = time.process_time() - self.runtime
			return solution

		self.init_explored()
		self.init_frontier()

		while True:
			if self.is_frontier_empty(): # Failure
				self.runtime = time.process_time() - self.runtime
				return None

			next_node = self.get_next_node()

			if next_node.state == self.goal:
				self.runtime = time.process_time() - self.runtime
				return next_node.build_solution()

			self.set_explored(next_node)
			self.expand_node(next_node)

		self.runtime = time.process_time() - self.runtime
		return None

	def manhattan_distance(self, state1, state2):
		'''
			Calculate manhattan distance between two states.

			@state1: First state.
			@state2: Second state.
			@return: Manhattan distance between state1 and state2.
		'''

		return sum(tuple(map(lambda x, y: abs(x - y), state1, state2)))

	def octile_distance(self, state1, state2):
		'''
			Calculate octile distance between two states.

			@state1: First state.
			@state2: Second state.
			@return: Octile distance between state1 and state2.
		'''

		tuple_dxdy = tuple(map(lambda x, y: abs(x - y), state1, state2))
		return max(tuple_dxdy) + 0.5 * min(tuple_dxdy)

	def print_solution(self, solution):
		'''
			Print the found solution.

			@solution: List with solution nodes, from initial to goal.
		'''

		if solution is None:
			print(Node(self.initial, None, None, 0))
			print(Node(self.goal, None, None, float('inf')))
			return

		print(solution[0])
		print(solution[-1])
		print()

		solution_str = solution.__repr__()
		# Format output
		solution_str = solution_str.replace('[', '')
		solution_str = solution_str.replace(']', '')
		solution_str = solution_str.replace('>,', '>')

		print(solution_str)

		return

	def print_path(self, solution):
		'''
			Print solution path. Affects original grid.

			@solution: List of nodes. Solution found.
		'''

		if solution is None:
			return

		output = open('path.map', 'w')

		height = self.problem_map.height
		width = self.problem_map.width

		self.problem_map.grid[(solution[0].state)] = 'I'
		self.problem_map.grid[(solution[-1].state)] = 'F'
		for i in solution[1:-1]:
			self.problem_map.grid[(i.state)] = 'X'

		for i in self.problem_map.grid:
			output.write(''.join(i) + '\n')

		output.close()
		return