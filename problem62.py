# The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

# Find the smallest cube for which exactly five permutations of its digits are cube.

############
# Solution #
############

import math

def getDigitCounts(n):
	count = [0] * 10
	while n > 0:
		count[n % 10] += 1
		n = n // 10
	return count

def isPermutation(a, b):
	for i in range(10):
		if a[i] != b[i]:
			return False
	return True
	# count_a = [0] * 10
	# count_b = [0] * 10
	# while a > 0 and b > 0:
	# 	d_a = a % 10
	# 	d_b = b % 10
	# 	count_a[d_a] += 1
	# 	count_b[d_b] += 1
	# 	a = a // 10
	# 	b = b // 10
	# if a != b:
	# 	return False
	# for i in range(10):
	# 	if count_a[i] != count_b[i]:
	# 		return False
	# return True

def nextPermutation(p):
	n = len(p)
	i = n - 1
	while i > 0 and p[i - 1] >= p[i]:
		i -= 1

	if i == 0:
		return [] # done

	pivot = i - 1

	# Find smallest number that is greater than pivot
	j = n - 1
	while j > 0 and p[j] <= p[pivot]:
		j -= 1

	p[pivot], p[j] = p[j], p[pivot]
	p[i:] = reversed(p[i:])
	return p

def pow10(n):
	result = 1
	while n > 0:
		result *= 10
		n -= 1
	return result

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

def isCubed(n):
	i = int(math.pow(n, 1 / 3))
	return (i + 1) * (i + 1) * (i + 1) == n or i * i * i == n

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

# def solve(n, nnn, limit, ncounts, level):
# 	m = n
# 	mmm = m * m * m
# 	while mmm <= limit:
# 		m += 1
# 		mmm = m * m * m

# 		mcounts = getDigitCounts(mmm)
# 		if not isPermutation(ncounts, mcounts):
# 			continue
# 		# print(m, mmm)
# 		d = getDigits(mmm)
# 		count = 0
# 		while len(d) > 0:
# 			if isCubed(getNumber(d)):
# 				count += 1
# 			d = nextPermutation(d)
# 		if count == 4:
# 			return True
# 		# print(mmm, "done")
# 		# if level == 4:
# 		# 	return True
# 		# else:
# 		# 	return solve(m, mmm, pow10(int(math.log10(mmm)) + 1) * 10, mcounts, level + 1)
# 	return False

# for n in range(2, 10000):
# 	nnn = n * n * n
# 	limit = pow10(int(math.log10(nnn)) + 1) * 10
# 	ncounts = getDigitCounts(nnn)
# 	if solve(n, nnn, limit, ncounts, 2):
# 		print(n, n * n * n)
# 		break

## NOPE
# for n in range(2, 1000):
# 	nnn = n * n * n
# 	p = getDigits(nnn)
# 	count = 0
# 	print(nnn)
# 	while len(p) > 0:
# 		if isCubed(getNumber(p)):
# 			if getNumber(p) != nnn:
# 				print("ok ", getNumber(p))
# 			count += 1
# 		p = nextPermutation(p)
# 	if count == 3:
# 		print(n)
# 		break

# def solve():
# 	for n in range(2, 500):
# 		nnn = n * n * n
# 		limit = pow10(int(math.log10(nnn)) + 1) * 10
# 		for m in range(n + 1, limit):
# 			mmm = m * m * m

# 			if not isPermutation(mmm, nnn):
# 				continue

# 			limitl = pow10(int(math.log10(mmm)) + 1) * 10
# 			for l in range(m + 1, limitl):
# 				lll = l * l * l
# 				if isPermutation(lll, nnn):
# 					return n, nnn
# 			# count = 0
# 			# p = getDigits(mmm)
# 			# p = nextPermutation(p)
# 			# print(p)
# 			# while len(p) > 0:
# 			# 	if isCubed(getNumber(p)):
# 			# 		count += 1
# 			# 	p = nextPermutation(p)
# 			# if count == 1:
# 			# 	return n, nnn

# print(solve())