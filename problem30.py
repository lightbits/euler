# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
# As 1 = 1^4 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

########################

from time import time

# Note that we can maximally have 6 digits, as 7 * 9^5 is less than a 7-digit number of only 9's

def solveProblem(ndigits, number, partialsum, result):
	tens = 10 ** (ndigits - 1)
	ret = result
	for i in range(0, 10):
		ps = partialsum + (i ** 5)
		n = number + i * tens
		if ps == n and i != 0 and ndigits > 1:
			ret += n
		if ndigits < 6:
			ret += solveProblem(ndigits + 1, n, ps, result)

	return ret

t0 = time()
s = solveProblem(1, 0, 0, 0)
t = time() - t0
print("solution: %d, time: %ds + %dms" % (s, t, (t - int(t)) * 1000))