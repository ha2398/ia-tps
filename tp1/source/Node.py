#!/usr/bin/env python3

'''
Trabalho Pratico 1: Inteligência Artificial
Autor: Hugo Araujo de Sousa (2013007463)
Node.py: Graph search node.
'''


class Node():
	
	def __init__(self, state, parent, action, cost):
		'''
			Initialize a Node of the graph search.

			@state: The state in the state space to which the node corresponds.
			@parent: The node in teh search tree that generated this node.
			@action: The action that was applied to the parent to generate the
				node.
			@cost: The cost of the path from the initial state to the node.
		'''

		self.state = state
		self.parent = parent
		self.action = action
		self.cost = cost
		self.depth = 0

		return

	def __eq__(self, node):
		'''
			Return True, iff, the two nodes have the same state.

			@node: Node to compate self with.
			@return: True, if the compared nodes have the same state. False
				otherwise.
		'''

		return self.state == node.state

	def __lt__(self, node):
		'''
			Return True, iff, the first node has a smaller cost than the second
				one.

			@node: Node to compare self with.
			@return: True, if the first node has a smaller cost than the second
				one.. False otherwise.
		'''

		return self.cost < node.cost

	def __str__(self):
		'''
			Get string representation of node.

			@return: String representation of Node.
		'''

		x, y = self.state
		cost = self.cost
		return str('<' + str(x) + ', ' + str(y) + ', ' + str(cost) + '>')

	def build_solution(self):
		'''
			Build a solution to the problem considering self is a goal node.

			@return: List wth sequence of Nodes, from initial to goal.
		'''

		solution = []
		next_node = self
		while next_node:
			solution.insert(0, next_node)
			next_node = next_node.parent

		return solution