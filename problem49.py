# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, 
# is unusual in two ways: 
# (i) each of the three terms are prime, and, 
# (ii) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
# exhibiting this property, but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating the three terms in this sequence?

############
# Solution #
############

import math

def isPrime(n):
	lim = int(math.sqrt(n) + 1)
	for i in range(3, lim, 2):
		if n % i == 0:
			return False
	return True

primes = [] # List of four-digit primes
is_prime = [False] * 11001
for n in range(1001, 10000, 2):
	if isPrime(n):
		primes.append(n)
		is_prime[n] = True

# See problem 43 and some more
def nextPermutation(p):
	n = len(p)
	i = n - 1
	while i > 0 and p[i - 1] >= p[i]:
		i -= 1
	if i == 0:
		return []
	pivot = i - 1
	j = n - 1
	while j > 0 and p[j] <= p[pivot]:
		j -= 1
	p[pivot], p[j] = p[j], p[pivot]
	p[i:] = reversed(p[i:])
	return p

# For four-digit n
def getDigits(n):
	return [n // 1000, (n % 1000) // 100, (n % 100) // 10, n % 10]

def primePermutations(n):
	p = getDigits(n)
	result = []
	while len(p) > 0: # While there is a new permutation
		num = p[0] * 1000 + p[1] * 100 + p[2] * 10 + p[3]
		if is_prime[num]:
			result.append(num)
		p = nextPermutation(p)
	return result

for p in primes:
	perms = primePermutations(p)
	# Now we only need to look for arithmetic sequences
	# in this list of increasing prime permutations
	for i in range(len(perms)):
		diff0 = perms[i] - p
		for j in range(i + 1, len(perms)):
			diff1 = perms[j] - perms[i]
			if diff1 > diff0:
				break
			elif diff1 == diff0:
				# The answer
				print(p, perms[i], perms[j])