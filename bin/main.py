#author: johnny

# thread-1: accept user input, spawns player threads
# thread-2: rate limiter control

import queue
import threading
import time

q = queue.Queue(10)
queue_lock = threading.Lock()
cv = threading.Condition(queue_lock)

#class to add tasks to the rate limited queue
class tasks():
	def __init__(self, q):
		self.q = q
	
	def enq(self, args):
		self.q.put(args)
		print(args + ' added')
		
	def stop(self):
		self.q.put('quit')
		print('stop command issued')

# thread object that gets and prints name data member of player object in queue
# has timer and counter for rate limiting
# currently prints at 1 second intervals.
# goal is for a thread which gets and makes api calls
class task_processing(threading.Thread):
	def  __init__(self, q):
		threading.Thread.__init__(self)
		self.q = q
		self.delay = 5 #seconds per reset
		self.call_limit = 1 # calls before reset
		self.counter = 0 #init counter
		#set timer
		now = time.time() # current time
		self.reset_time = now + self.delay # time to reset

	def run(self):
		print('starting task thread')
		quit = False
		while quit != True:
			if not self.q.empty():
				cv.acquire()
				cv.wait_for(self.check_lock, 5)
				params = self.q.get()
				if params == 'quit':
					quit = True
				else:
					print(params + ': ' + str(time.time()))
					self.counter += 1
				cv.release()
		print('stopping task thread')

	def check_lock(self):
		unlocked = True
		exceed_call_limit = (self.counter >= self.call_limit)
		if exceed_call_limit:
			unlocked = False
		while not unlocked or (time.time() >= self.reset_time): # loop until lock can be opened
			if time.time() >= self.reset_time: # check if enough time has elapsed to reset
				unlocked = True # open lock
				self.counter = 0
				self.reset_time = time.time() + self.delay #reset to current time
		return unlocked

if __name__ == '__main__':
	processing = task_processing(q)
	processing.start()
	
	new_task = tasks(q)
	new_task.enq('test0')
	new_task.enq('test1')
	new_task.enq('test2')
	new_task.enq('quit')
	
	processing.join()
	
	