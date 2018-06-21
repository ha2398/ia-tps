#!/usr/bin/env python3

'''
Trabalho Pratico 2: Inteligência Artificial
Autor: Hugo Araujo de Sousa (2013007463)
MDP.py: Markov Decision Problem class.
'''


from Map import Map


class MDP():
    def __init__(self, S, A, R, map_filename):
        '''
            Initialize the Markov Decision Problem instance.

            @S: (string list) Set of states where the agent can be.
            @A: (string list) Set of actions the agent can execute.
            @R: (dict {string: int}) Reward function, mapping states to
                rewards.
            @map_filename: (string) Name of the file to read mapa data from.
        '''

        self.states = S
        self.actions = A
        self.rewards = R
        self.map = Map(map_filename)
