import time

def timestamp(func):
	def inner1():
		print(time.ctime())
		func()
	return inner1

"""	
@timestamp
def hi():
	print('hi')

def main():
	hi()
	
main()
"""
