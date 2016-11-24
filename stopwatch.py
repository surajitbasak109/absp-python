#! python3
# stopwatch.py - A simple stopwatch program.

import time
print("Press 'Enter' to begin the Stopwatch and Press CTRL-C to stop.")
input()
print('Started')
startTime = time.time()
lastTime = startTime
lapNum = 1

# Start tracking the lap times
try:
	while True:
		input()
		lapTime = round(time.time() - lastTime, 2)
		totalTime = round(time.time() - startTime, 2)
		print('Lap %s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
		lapNum += 1
		lastTime = time.time()
except KeyboardInterrupt:
	print('\nDone')
