#!/usr/bin/env python3

import time
from multiprocessing import Pool

processes = 100

def get_entropy():
  entropy_avail = open('/proc/sys/kernel/random/entropy_avail', 'rb')
  rand_bytes = str(entropy_avail.read(), 'utf-8').replace('\n','')
  entropy_avail.close()
  return rand_bytes

def consume(x):
  rand = open('/dev/random','rb')
  while True:
    data = rand.read(1024*1024)

if __name__ == '__main__':
  print(f'Entropy available: {get_entropy()} bytes')
  print('Starting to consume entropy...')
  pool = Pool(processes)
  pool.map_async(consume, range(processes))

  while True:
    print(f'Entropy available: {get_entropy()} bytes')
    time.sleep(1)
