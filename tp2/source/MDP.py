#!/usr/bin/env python3

'''
Trabalho Pratico 2: Inteligência Artificial
Autor: Hugo Araujo de Sousa (2013007463)
MDP.py: Markov Decision Problem class.
'''


from Map import Map
import numpy as np
import operator as op


class MDP():

    WALL = '#'
    FREE = '-'
    TABLET = '0'
    GHOST = '&'

    UP = '^'
    LEFT = '<'
    RIGHT = '>'
    DOWN = 'v'

    TERMINALS = [TABLET, GHOST]

    def __init__(self, S, A, R, alpha, gamma, map_filename, iterations):
        '''
            Initialize the Markov Decision Problem instance.

            @S: (string list) Set of states where the agent can be.
            @A: (string list) Set of actions the agent can execute.
            @R: (dict {string: int}) Reward function, mapping states to
                rewards.
            @alpha: (float) Learning rate.
            @gamma: (float) Discount factor for Q-Learning algorithm.
            @map_filename: (string) Name of the file to read mapa data from.
            @iterations: (int) Number of iterations to run the Q-Learning
                algorithm for.
        '''

        self.states = S
        self.actions = A
        self.rewards = R
        self.alpha = alpha
        self.gamma = gamma
        self.map = Map(map_filename)
        self.iterations = iterations

    def init_qmatrix(self):
        '''
            Initialize the Q matrix for Q-Learning algorithm.

            @return: ((dict {string: int} list) list) Initial Q matrix for
                current MDP.
        '''

        height, width = self.map.get_height(), self.map.get_width()

        return [[dict(zip([a for a in self.actions],
            [0. for x in range(len(self.actions))])) for w in range(width)] \
            for h in range(height)]

    def select_initial_state(self, height, width):
        '''
            Select initial state for Q-Learning algorithm randomly.

            @height: (int) Map height.
            @width: (int) Map width:

            @return: (int, int) Initial state coordinates.
        '''

        x, y = np.random.randint(0, height - 1), np.random.randint(0, width - 1)
        while self.map.get_position(x, y) != self.FREE:
            x, y = np.random.randint(0, height - 1), np.random.randint(0,
                width - 1)

        return x, y

    def select_action(self, state):
        '''
            Select a random action to perform.

            @return: (string (int, int)) Action to perform and the state the
                agent will get to, by performing it.
        '''

        action = np.random.choice([action for action in self.actions])
        possible, new_state = self.simulate_action(state, action)
        while not possible:
            action = np.random.choice([action for action in self.actions])
            possible, new_state = self.simulate_action(state, action)

        return action, new_state

    def simulate_action(self, state, action):
        '''
            Simulate performing an action at a particular state.

            @state: (int, int) Current state.
            @action: (string) Action to simulate.

            @return: (bool, (int, int)) True, iff, the action can be performed
                and the state the agent would get to, by performing the given
                action.
        '''

        height, width = self.map.get_height(), self.map.get_width()

        x, y = state
        x_bound, y_bound = height - 1, width - 1

        if action == self.UP:
            new_state = (x - 1, y)
        elif action == self.LEFT:
            new_state = (x, y - 1)
        elif action == self.RIGHT:
            new_state = (x, y + 1)
        elif action == self.DOWN:
            new_state = (x + 1, y)
        else:
            new_state = (-1, -1)

        new_x, new_y = new_state
        new_position = self.map.get_position(new_x, new_y)

        if new_position == self.WALL:
            return True, state
        elif new_x < 0 or new_x > x_bound or new_y < 0 or new_y > y_bound:
            return False, None
        else:
            return True, new_state

    def get_maxq(self, Q, state):
        '''
            Get the maximum value in the Q matrix entry of a particular state.

            @Q: ((dict {string: int} list) list) Q matrix.
            @state: (int, int) Current state.

            @return: (float) Maximum Q matrix value for the given state.
        '''

        x, y = state
        return max(Q[x][y].items(), key=op.itemgetter(1))[1]

    def updateQ(self, Q, action, state, new_state_maxq):
        '''
            Update the Q matrix entry for the current state.

            @Q: ((dict {string: int} list) list) Q matrix.
            @action: (string) Action the agent is about to perform.
            @state: (int, int) Current state.
            @new_state_maxq: (float) Maximum Q matrix value for the given state.
        '''

        x, y = state
        cur_q = Q[x][y][action]
        state_r = self.rewards[self.map.get_position(*state)]
        Q[x][y][action] = cur_q + self.alpha * (state_r + \
            self.gamma*new_state_maxq - cur_q)

    def qlearning(self):
        '''
            Run the Q-Learning algorithm for the MDP instance.
        '''

        height, width = self.map.get_height(), self.map.get_width()

        Q = self.init_qmatrix()
        episode = 0

        iteration = 0
        while True:
            state = self.select_initial_state(height, width)

            # While terminal state hasn't been reached.
            while self.map.get_position(*state) not in self.TERMINALS:
                action, new_state = self.select_action(state)
                new_state_maxq = self.get_maxq(Q, new_state)
                self.updateQ(Q, action, state, new_state_maxq)
                state = new_state

                iteration += 1
                if iteration == self.iterations:
                    break

            episode += 1
            if iteration == self.iterations:
                break

        print(Q)