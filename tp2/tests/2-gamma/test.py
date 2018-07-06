#!/usr/bin/env python3

# Run convergence experiment.

import argparse
import matplotlib.pyplot as plt
import os
import shutil
import subprocess as sp

parser = argparse.ArgumentParser()
parser.add_argument('-s', dest='SEEDS', default=5, type=int,
                    help='Number of seeds.')
parser.add_argument('-j', dest='JOBS', default=2, type=int,
                    help='Number of jobs.')

args = parser.parse_args()

EXE = '../../source/tp2.py'
MAPS = '../../maps/'
ALPHA = 0.3
GAMMA = [0.2, 0.5, 0.9]
EPSILON = 1

ITER = [50000, 5000000, 200000]

print('***TP2\tEXPERIMENT 2\tGAMMA***\n')

# Remove older results
contents = os.listdir('.')
del(contents[contents.index('test.py')])
for c in contents:
    if os.path.isfile(c):
        os.remove(c)
    else:
        shutil.rmtree(c)

cmds = open('cmds.txt', 'w')
maps = os.listdir('../../maps')

# Generate commands
for i, m in enumerate(sorted(maps)):
    map_dir = m.split('.')[0]
    os.mkdir(map_dir)

    for g in GAMMA:
        for s in range(args.SEEDS):
            csv_name = map_dir + '/qsum_s' + \
                str(s) + 'g' + str(g).replace('.', '') + '.csv'
            cmds.write('{} {} {} {} {} -s {} -e {} -q {}\n'.format(
                EXE, MAPS + m, ALPHA, g, ITER[i], s, EPSILON, csv_name))

cmds.close()

# Run commands
print('RUNNING COMMANDS\n')

cmds = open('cmds.txt', 'r')
sp.call(['parallel', '-j', str(args.JOBS), '--bar'], stdin=cmds)
cmds.close()
print()

data = {}
# Get data and plot
print('PLOTTING DATA\n')
for i, m in enumerate(sorted(maps)):
    data[m] = {}
    map_dir = m.split('.')[0]

    for g in GAMMA:
        # Get file names
        csv_files = []
        for s in range(args.SEEDS):
            csv_files.append('qsum_s{}g{}.csv'.format(
                s, str(g).replace('.', '')))

        data[m][g] = [0.] * int(ITER[i] / 1000)

        for csv in csv_files:
            csv_f = open(map_dir + '/' + csv, 'r')

            line = csv_f.readline().strip()
            while line:
                n, q = line.split()
                n = int((int(n) / 1000) - 1)
                q = float(q)
                data[m][g][n] += q
                line = csv_f.readline().strip()

            csv_f.close()

# Plot
legend = []
for g in GAMMA:
    legend.append(r'$\gamma = {}$'.format(g))

for i, m in enumerate(sorted(data)):
    x_axis = list(range(1000, ITER[i] + 1, 1000))
    fig = plt.figure(i)
    plt.grid(True)
    plt.ylabel(r'$\sum_{i,j} max(Q_{i,j})$')
    plt.xlabel('Tempo (iterações)')
    plt.title('Efeito do fator de desconto nos valores de Q ({})'.format(
        m.split('.')[0]))

    for g in GAMMA:
        plt.plot(x_axis, list(map(lambda x: x / args.SEEDS, data[m][g])))

    plt.legend(legend, loc='best')
    plt.tight_layout()
    fig.savefig('gamma_{}.png'.format(m.split('.')[0]))
