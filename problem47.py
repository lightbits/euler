# The first two consecutive numbers to have two distinct prime factors are:

# 14 = 2 × 7
# 15 = 3 × 5

# The first three consecutive numbers to have three distinct prime factors are:

# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.

# Find the first four consecutive integers to have four distinct prime factors. 
# What is the first of these numbers?

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

primes = [2]
for n in range(3, 10000, 2):
	if isPrime(n):
		primes.append(n)

def numPrimeFactors(n):
	num_factors = 0
	for p in primes:
		if n == 1:
			break
		if n % p == 0:
			num_factors += 1
		while n % p == 0:
			n = n // p
	return num_factors

for n in range(10, 500000):
	if numPrimeFactors(n + 3) != 4:
		n += 3
		continue
	if numPrimeFactors(n + 2) != 4:
		n += 2
		continue
	# We get to this point quite often
	# Could perhaps reuse n2 and n3 cleverly?
	if numPrimeFactors(n + 1) != 4:
		n += 1
		continue
	if numPrimeFactors(n) != 4:
		continue

	print(n, n + 1, n + 2, n + 3)
	break