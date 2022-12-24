#!/usr/bin/python

import sys
import os
import time
import random

arg = int(sys.argv[1])
child_pid = os.getpid()
parent_pid = os.getppid()
print(f"Сhild[{pid}]: I am started. My PID {child_pid}. Parent PID {parent_pid}")
time.sleep(arg)
print(f"Child[{pid}]: I am ended. PID {child_pid}. Parent PID {parent_pid}")
status = random.randint(0, 1)
os._exit(status)