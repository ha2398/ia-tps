#!/usr/bin/env python3

'''
Trabalho Pratico 1: Inteligência Artificial
Autor: Hugo Araujo de Sousa (2013007463)
AStar.py: A* graph search. Two available heuristics: Manhattan and Octile.
'''


from GraphSearch import GraphSearch
from heapq import *
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

		if self.heuristic == 'manhattan': # Mahattan
			return self.manhattan_distance(node.state, self.goal)
		elif self.heuristic == 'octile': # Octile
			return self.octile_distance(node.state, self.goal)
		else:
			return float('inf')

	def init_frontier(self):
		'''
			Initialize the search frontier using the initial state of the
			problem.
		'''

		first_node = Node(self.initial, None, None, 0)
		fn = self.heuristic_value(first_node)
		self.frontier = [(fn, first_node)]
		return

	def add_to_frontier(self, node):
		'''
			Add a node to the frontier.

			@node: Node to add.
		'''

		if self.explored[node.state]:
			return
		elif self.is_in_frontier[node.state]:
			# Find node
			index = list(map(lambda x: x[1], self.frontier)).index(node)

			old_node = self.frontier[index][1]
			old_cost = old_node.cost

			# Updates in case the new cost is smaller.
			if node.cost < old_cost:
				self.frontier.pop(index)
				heapify(self.frontier)
			else:
				return

		fn = node.cost + self.heuristic_value(node)
		heappush(self.frontier, (fn, node))
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