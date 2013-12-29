# We shall say that an n-digit number is pandigital if 
# it makes use of all the digits 1 to n exactly once. 
# For example, 2143 is a 4-digit pandigital and is also prime.

# What is the largest n-digit pandigital prime that exists?

############
# Solution #
############

# The upper limit is the 9-digit pandigital number 987654321
# Instead of iterating through the numbers from the upper limit and
# downwards, we permute 987654321 (so we don't need a pandigital check)
# and break as soon as we find a permutation that is prime.
# We start from the highest lexicographic ordering, and proceed downwards.

import math

# Returns the next decreasing lexicographic permutation,
# and whether or not it is the lowest permutation.
def prevPermutation(p):
	# The idea is that we want to decrease the sequence as little as possible
	# Find the longest non-decreasing suffix (the longest, lowest permutation)
	seq_len = len(p)
	suffix = seq_len - 1
	while suffix > 0 and p[suffix - 1] <= p[suffix]:
		suffix -= 1

	# If there is no pivot then we have the lowest permutation and are done
	if suffix == 0:
		return p, True

	# Find first element from the right that is smaller than the pivot
	pivot = suffix - 1
	pred = seq_len - 1
	while pred > pivot and p[pred] >= p[pivot]:
		pred -= 1

	# Swap it with the pivot
	p[pivot], p[pred] = p[pred], p[pivot]

	# Reverse the suffix (giving the greatest permutation)
	p[suffix:] = reversed(p[suffix:])
	return p, False

def isPrime(p):
	if p % 2 == 0:
		return False
	n = 3
	lim = int(math.sqrt(p)) + 1
	for n in range(3, lim + 1):
		if p % n == 0:
			return False
	return True

p = [9, 8, 7, 6, 5, 4, 3, 2, 1]
num_digits = len(p)
last = False
while num_digits > 1:
	n = p[0]
	for i in range(1, num_digits):
		n = n * 10 + p[i]

	if isPrime(n):
		print(n)
		break

	# The sequence is the lowest permutation
	# So we remove the last element, and reverse it
	# to begin the next sequence
	if last:
		p = p[:-1]
		p.reverse()
		num_digits -= 1
		last = False
	else:
		p, last = prevPermutation(p)