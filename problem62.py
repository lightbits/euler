# The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

# Find the smallest cube for which exactly five permutations of its digits are cube.

############
# Solution #
############

def getDigits(n):
	digits = []
	while n > 0:
		digits.append(n % 10)
		n = n // 10
	return digits

def getNumber(digits):
	number = 0
	for d in digits:
		number *= 10
		number += d
	return number

upper_limit = 100000 # Guessing
permutations = {}
smallest_cubes = {}
for n in range(2, upper_limit):
	nnn = n * n * n
	digits = getDigits(nnn)
	digits.sort()
	digits.reverse()
	key = getNumber(digits)
	if key in permutations:
		permutations[key] += 1
	else:
		smallest_cubes[key] = nnn
		permutations[key] = 1

smallest = upper_limit * upper_limit * upper_limit
for key, value in permutations.items():
	if value == 5:
		if smallest_cubes[key] < smallest:
			smallest = smallest_cubes[key]
print(smallest)

