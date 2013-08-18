# Euler discovered the remarkable quadratic formula:

# n² + n + 41

# It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. 
# However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly 
# when n = 41, 41² + 41 + 41 is clearly divisible by 41.

# The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the
# consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.

# Considering quadratics of the form:

# n² + an + b, where |a| < 1000 and |b| < 1000

# where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |−4| = 4
# Find the product of the coefficients, a and b, for the quadratic expression that produces
# the maximum number of primes for consecutive values of n, starting with n = 0.

import math

def is_prime(n):
	for i in range(2, int(math.sqrt(n)) + 2):
		if n % i == 0:
			return False
	return True

# Precompute boolean values for whether a number is prime or not
listOfPrimes = []
for i in range(0, 100000):
	listOfPrimes.append(is_prime(i))

print("built list of primes!")

# Returns the number of consecutive primes produced by the formula
# n^2 + an + b, starting with n = 0
def prime_length(a, b):
	n = 0
	x = b
	while listOfPrimes[x]:
		n += 1
		x = n * n + a * n + b
		if x < 0:
			break
	return n

# Note that b must be prime, otherwise n=0 will yield a non-prime...
# Also note that b must be greater than 0, for this reason, thus
# we do not have to iterate from -1000 to 1000
maxPrimeLength = 0
maxPrimeLengthA = 0
maxPrimeLengthB = 0
for a in range(-1000, 1000):
	for b in range(0, 1000):
		primeLength = prime_length(a, b)
		if primeLength > maxPrimeLength:
			maxPrimeLength = primeLength
			maxPrimeLengthA = a
			maxPrimeLengthB = b

print("a = %d, b = %d gave %d consecutive primes" % (maxPrimeLengthA, maxPrimeLengthB, maxPrimeLength))