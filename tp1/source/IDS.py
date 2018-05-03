#!/usr/bin/env python3

'''
Trabalho Pratico 1: Inteligência Artificial
Autor: Hugo Araujo de Sousa (2013007463)
IDS.py: Iterative deepening depth-first search.
'''


from GraphSearch import GraphSearch
from Node import Node


class IDS(GraphSearch):

	def __init__(self, initial, goal, problem_map):
		'''
			Initialize the iterative deepening depth-first search for a problem.

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
		self.frontier = [first_node]
		return

	def add_to_frontier(self, node):
		'''
			Add a node to the frontier.

			@node: Node to add.
		'''

		if node.parent is not None:
			node.depth = node.parent.depth + 1

		if self.is_in_frontier[node.state] or self.explored[node.state]:
			return					

		self.frontier.append(node)
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

		return self.frontier.pop()

	def start(self):
		'''
			Perform the graph search.

			@return: List wth sequence of Nodes, from initial to goal, in case
				of success. None otherwise.
		'''

		if  self.problem_map.grid[self.initial] == '@' or \
			self.problem_map.grid[self.goal] == '@':
			solution = [Node(self.initial, None, None, 0),
				Node(self.goal, None, None, float('inf'))]

			return solution

		L = 0
		while True:
			print('Depth limit:', L)
			self.init_explored()
			self.init_frontier()

			while True:
				if self.is_frontier_empty(): # Failure
					L += 1
					break

				next_node = self.get_next_node()

				if next_node.depth > L:
					continue

				if next_node.state == self.goal:
					return next_node.build_solution()

				self.set_explored(next_node)
				self.expand_node(next_node)

		return None