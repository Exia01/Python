# iter calls next and then we initiate the StopIteration

class Counter:
	def __init__(self, start, end, steps=None):
		self.current = start
		self.end = end
		if steps:
			self.steps = steps
		else:
			self.steps = 1

	def __iter__(self): #  makes it iterable --> thus creating method
		return self # returns 

	def __next__(self): #defines the behavior of the next
		if self.current < self.end:
			num = self.current
			self.current += self.steps #0,1,2,3,4
			return num
		if self.current > self.end:
			num = self.current
			self.current -= self.steps
			return num
		raise StopIteration




for x in Counter(10,2):
	print(x)

print(help(Counter))