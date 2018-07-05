#!/usr/bin/env python3

# Run convergence experiment.

import matplotlib.pyplot as plt
import os
import shutil
import subprocess as sp

EXE = '../../source/tp2.py'
MAPS  = '../../maps/'
ALPHA = 0.3
GAMMA = 0.9
ITER = 1000
EPSILON = 1
SEEDS = 5
JOBS = 4

plt.xlabel('Tempo (iterações)')
plt.ylabel(r'$\sum_{i,j} max(Q_{i,j}$')
plt.title('Convergência da política ótima')
plt.grid(True)

print('***TP2\tEXPERIMENT 1\tCONVERGENCE/ITERATIONS***\n')

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
for m in maps:
	map_dir = m.split('.')[0]
	os.mkdir(map_dir)

	for s in range(SEEDS):
		csv_name = map_dir + '/qsum_s' + str(s) + '.csv' 
		cmds.write('{} {} {} {} {} -s {} -e {} -q {}\n'.format(
			EXE, MAPS+m, ALPHA, GAMMA, ITER, s, EPSILON, csv_name))

cmds.close()

# Run commands
print('RUNNING COMMANDS\n')
cmds = open('cmds.txt', 'r')
sp.call(['parallel', '-j', str(JOBS), '--bar'], stdin=cmds)
cmds.close()
print()

data = {}
# Get data and plot
print('PLOTTING DATA\n')
for m in maps:
	data[m] = [0.] * ITER
	map_dir = m.split('.')[0]
	csv_files = os.listdir(map_dir)

	# Get data
	for csv in csv_files:
		csv_f = open(map_dir + '/' + csv, 'r')

		line = csv_f.readline().strip()
		while line:
			i, q = line.split()

			i = int(i) - 1
			q = float(q)

			data[m][i] += q

			line = csv_f.readline().strip()

		csv_f.close()

# Plot
x_axis = list(range(1, ITER+1))
legend = []

for m in data:
	legend.append(m)
	plt.plot(x_axis, list(map(lambda x: x/SEEDS, data[m])))

plt.legend(legend, loc='upper left')
plt.show()