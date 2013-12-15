# The number 3797 has an interesting property. 
# Being prime itself, it is possible to continuously remove digits 
# from left to right, and remain prime at each stage: 3797, 797, 97, and 7. 
# Similarly we can work from right to left: 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

############
# Solution #
############

# Deciding the upper limit:
# is hard... Let's just search for eleven truncatable primes
# as cunningly as we can (ugly solution)

UPPER_LIMIT = 1000000 # Guessing...

import math

# Generate primes
primes = [False] * UPPER_LIMIT
primes[2] = True
for n in range(3, UPPER_LIMIT, 2): # Avoiding even numbers
	lim = int(math.sqrt(n)) + 1
	is_prime = True
	for i in range(3, lim, 2): # Do not need to check even numbers
		if n % i == 0:
			is_prime = False
			break
	primes[n] = is_prime

def isTruncatablePrime(n):
	reverse = 0
	tens = 1
	while n > 0:
		if not primes[n]:
			return False
		d = n % 10
		reverse += d * tens
		if not primes[reverse]:
			return False
		tens *= 10
		n = n // 10
	return True

answer = 0

for n in range(11, UPPER_LIMIT, 2):
	last = n % 10
	if last == 3 or last == 7:
		if isTruncatablePrime(n):
			answer += n

print(answer)