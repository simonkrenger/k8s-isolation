#!/usr/bin/env python3

import os
import time

# List for holding file descriptors
fdlist=[]
length=0

try:
  while True:
    fdlist.append(os.open('/etc/hosts', os.O_RDONLY))
    length = len(fdlist)
    print(f'Open file descriptors: {length}')
except:
  print(f'os.open() failed, now pausing and keeping the file descriptors open.') 

while True:
  time.sleep(5)
  print(f'Sleeping. Keeping {length} file descriptors open.')
