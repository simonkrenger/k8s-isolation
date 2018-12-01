#!/usr/bin/env python3

import os

# List for holding file descriptors
fdlist=[]

while True:
  fdlist.append(os.open('/etc/hosts', os.O_RDONLY))
  length = len(fdlist)
  print(f'Open file descriptors: {length}')
