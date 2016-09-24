# Pyrate_Limiter
## A simple rate limiter module for Python3

###start by importing the module:
	import rate_limiter

###to instantiate your own object:
	my_rate_limited_queue = rate_limiter.task_processing(q_size, calls, time_seconds, lock_timeout = 10)
	
	all arguments are type int
	q_size: size of queue
	calls/time_seconds: how many function calls are allowed for allotted time_seconds. 
	this represents the maximum rate.
	lock_timeout: how long to wait until queue lock is automatically released.

###start the rate limited queue:
	my_rate_limited_queue.start()


###enqueue a function and its arguments!
	my_rate_limited_queue.enq(func, *args, add_counter = True, **kwargs)
	
	add_counter: as an option, enqueue a function that doesn't count against the rate by specifying as False. 
	by default, this is true the queue counts all functions against the rate limit.

###enqueue the stop:
	my_rate_limited_queue.enq_stop()
	
	this function will enqueue the stop command, terminating the queue and the thread.

###stop immediately:
	my_rate_limited_queue.imm_stop()
	
	this function sends the stop command immediately and terminates the queue at the next loop evaluation. 

###more stuff about python multithreading here:
	https://docs.python.org/3/library/threading.html
