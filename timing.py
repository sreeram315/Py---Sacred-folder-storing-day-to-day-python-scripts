# proprietary to BEERA // DO NOT COPY

def func1():
	a = 0
	for _ in range(1000000000):
		a += 1

def func2():
	a = 0
	for _ in range(1000000000):
		a = a + 1





import timeit

start_time = timeit.default_timer()
func1()
print(timeit.default_timer() - start_time)

start_time = timeit.default_timer()
func2()
print(timeit.default_timer() - start_time)