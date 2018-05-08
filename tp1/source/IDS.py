#!/usr/bin/env python3

'''
Trabalho Pratico 1: Inteligência Artificial
Autor: Hugo Araujo de Sousa (2013007463)
IDS.py: Iterative deepening depth-first search.
'''


from GraphSearch import GraphSearch
from Node import Node


import time


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

		if node.cost > self.L:
			return

		if 	self.explored[node.state] > node.cost or \
				(self.explored[node.state] == 0 and
				not self.is_in_frontier[node.state]):
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

		self.runtime = time.process_time()

		if  self.problem_map.grid[self.initial] == '@' or \
			self.problem_map.grid[self.goal] == '@':
			solution = [Node(self.initial, None, None, 0),
				Node(self.goal, None, None, float('inf'))]

			self.runtime = time.process_time() - self.runtime
			return solution

		self.L = 0
		while True:
			self.init_explored()
			self.init_frontier()

			while True:
				if self.is_frontier_empty(): # Failure
					self.L += .5
					break

				next_node = self.get_next_node()

				if next_node.state == self.goal:
					self.runtime = time.process_time() - self.runtime
					return next_node.build_solution()

				old_cost = self.explored[next_node.state]
				if old_cost == 0 and next_node.state != self.initial:
						self.explored[next_node.state] = next_node.cost
				else:
					self.explored[next_node.state] = min(old_cost,
						next_node.cost)

				self.expand_node(next_node)

		self.runtime = time.process_time() - self.runtime
		return None