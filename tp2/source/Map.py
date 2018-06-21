#!/usr/bin/env python3

'''
Trabalho Pratico 2: Inteligência Artificial
Autor: Hugo Araujo de Sousa (2013007463)
Map.py: Pac-Maze 2D map with blocked, pill and ghost cells.
'''


import numpy as np


class Map():

    def __init__(self, input_file):
        '''
            Initialize a map.

            @input_file: (string) Name of the input file to read map data from.
        '''

        map_file = open(input_file, 'r')

        # Get dimensions
        self.height, self.width = map_file.readline().split(' ')
        self.height = int(self.height)
        self.width = int(self.width)

        # Build map grid
        grid = []
        next_line = map_file.readline().strip()
        while next_line:
            grid = grid + [c for c in next_line]
            next_line = map_file.readline().strip()

        self.grid = np.array(grid)
        self.grid.shape = (self.height, self.width)

        map_file.close()

        return
