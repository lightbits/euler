# The number, 197, is called a circular prime because all rotations of the digits: 
# 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?

# Solution

from math import *

def isPrime(n):
	for i in range(2, int(sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True

# Note that to be a circular prime, the number cannot contain ANY even numbers
# We can filter out a great deal using this fact.
candidate_primes = []
n = 1
while n <= 1000000:
	num_digits = int(log10(n)) + 1
	m = n
	for i in range(num_digits):
		digit = m % 10
		if digit % 2 == 0:
			tens = int(pow(10, i))
			# Jump to next number not containing an even digit up to here.
			# For example, 1293741 contains an even digit, 4, so we first jump to 
			# 1293750 + 1. We then find an even number, 2, and jump to 1300000 + 1.
			n = (n + tens - (n % tens)) + 1
		m = m // 10

	if isPrime(n):
		candidate_primes.append(n)

	n += 2

count = 0

for p in candidate_primes:
	num_digits = int(log10(p)) + 1
	tens = int(pow(10, num_digits - 1))
	circular = True
	rn = p
	# Rotate n and check if prime
	for i in range(num_digits):
		rn = (rn % 10) * tens + (rn // 10)
		if not isPrime(rn):
			circular = False
			break
	if circular:
		count += 1

print(count)