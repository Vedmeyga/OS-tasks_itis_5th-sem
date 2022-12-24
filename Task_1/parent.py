#!/usr/bin/python

import os
import sys
import random

def fork_child():
	ch_pid = os.fork()
	if ch_pid == 0:
		os.execl("./child.py", "child.py", str(random.randint(5, 10)))
	print(f"Parent [{os.getpid()}]: I ran children process with PID {ch_pid}")

amount = int(sys.argv[1])

for i in range(0, amount):
	fork_child()

while amount > 0:
	child_pid, status = os.wait()
	status = status // 256
	if status != 0:
        child_pid = fork_child()
    else:
        print(f"Parent[{os.getpid()}]: Child with PID {child_pid} terminated. Exit Status {status}.")
        amount -= 1