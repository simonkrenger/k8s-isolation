#!/usr/bin/env python3

import os
import time
import uuid

# Number of files
length=0

try:
  print(f'Starting to generate files...')

  while True:
    with open(str(uuid.uuid4()), 'w') as f:
      f.write('a')
      
    length = length + 1
    if length % 10000 == 0:
      print(f'Files generated: {length}', flush=True)
except:
  print(f'open, write or close failed, now sleeping forever...') 

while True:
  time.sleep(5)
  print(f'Sleeping.')
