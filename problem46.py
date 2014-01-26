# It was proposed by Christian Goldbach that every odd composite number 
# can be written as the sum of a prime and twice a square.

# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^3
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2

# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

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

twice_squares = []
for n in range(1, 100):
	twice_squares.append(2 * n * n)

odd_composites = []
primes = [1, 2, 3]
for n in range(5, 10000, 2):
	if isPrime(n):
		primes.append(n)
	else:
		odd_composites.append(n)

def fitsConjecture(n):
	for p in primes:
		if p > n:
			break
		for ts in twice_squares:
			sm = p + ts
			if sm > c:
				break
			elif sm == c:
				return True
	return False

for c in odd_composites:
	if not fitsConjecture(c):
		print(c)
		break