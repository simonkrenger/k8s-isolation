#!/usr/bin/env python

# Code comes from: https://gist.github.com/tott/3895832
# Converted to Python 3

from multiprocessing import Pool
from multiprocessing import cpu_count

def f(x):
    while True:
        x*x

if __name__ == '__main__':
    processes = cpu_count()
    print(f'Utilizing {processes} cores\n')
    pool = Pool(processes)
    pool.map(f, range(processes))
