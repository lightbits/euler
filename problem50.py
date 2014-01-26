# The prime 41, can be written as the sum of six consecutive primes:

# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.

# The longest sum of consecutive primes below one-thousand that adds to a prime, 
# contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the most consecutive primes?

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

upper_limit = 1000000

primes = [] # List of four-digit primes
is_prime = [False] * (upper_limit + 1)
for n in range(1, upper_limit, 2):
	if isPrime(n):
		primes.append(n)
		is_prime[n] = True

print("generated primes")

current_answer = -1
length = 200
while length < 1000: # Uhhh
	# Generate a decreasing sequence of primes, starting from upper_limit
	seq_sum = 0
	for i in range(length):
		seq_sum += primes[len(primes) - i - 1]

	# Shift sequence downwards until its sum is < 1000 and prime
	begin = len(primes) - length
	end = len(primes) - 1
	was_ans = False
	while begin >= 0:
		seq_sum -= primes[end]
		end -= 1
		begin -= 1
		seq_sum += primes[begin]
		if seq_sum < upper_limit and is_prime[seq_sum]:
			print(length, seq_sum)
			break

	length += 1