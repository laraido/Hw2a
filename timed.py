import time

def timeme(func):
	def inner1(*args, **kwargs):
		begin = time.time()
		func(*args, **kwargs)
		end = time.time()
		print("Total time ", end-begin)
	return inner1

"""
@timeme
def funcused():
	time.sleep(2)
	
funcused()
"""
