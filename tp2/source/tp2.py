#!/usr/bin/env python3

'''
Trabalho Pratico 2: Inteligência Artificial
Autor: Hugo Araujo de Sousa (2013007463)
tp2.py:
'''


from MDP import MDP
import argparse
import numpy as np


parser = argparse.ArgumentParser()
parser.add_argument('map', type=str, help='Map of the world.')
parser.add_argument('alpha', type=float, help='Learning rate.')
parser.add_argument('gamma', type=float, help='Discount factor.')
parser.add_argument('iter', type=int, help='Number of iterations.')
parser.add_argument('-e', dest='EPSILON', default=0, type=float,
	help='Epsilon for e-greedy policy.')
parser.add_argument('-s', dest='SEED', default=0, type=int,
	help='Seed for pseudo-number generator.')

args = parser.parse_args()

np.random.seed(args.SEED)

STATES = ['-', '0', '&']
ACTIONS = ['^', '<', '>', 'v']
REWARDS = {'-': -1, '0': 10, '&': -10}


def main():
    '''
        Main function.
    '''

    pac_maze = MDP(STATES, ACTIONS, REWARDS, args.alpha, args.gamma, args.map,
    	args.iter, args.EPSILON)
    pac_maze.qlearning()


main()
