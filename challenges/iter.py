numbers = [1, 2, 3, 5]

iterator = iter(numbers)

for n in range(len(numbers)):
	print(next(iterator))