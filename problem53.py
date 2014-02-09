# There are exactly ten ways of selecting three from five, 12345:

# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

# In combinatorics, we use the notation, 5C3 = 10.

# In general,
# 		   n!
# nCr = --------,
# 	 	r!(n−r)!
# where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
# It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

# How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, 
# are greater than one-million?

############
# Solution #
############

def choose(n, k):
	if k == 0:
		return 1
	numerator = n
	n_min = n - k + 1
	while n > n_min:
		n -= 1
		numerator *= n
	denominator = k
	while k > 2:
		k -= 1
		denominator *= k
	return numerator // denominator

# Returns number of values of nCr that were > one million,
# for 1 <= r <= n
def num_greater_than_mill(n):
	ret = 0
	r = 1
	while r <= n:
		if choose(n, r) > 1000000:
			ret += 1
		r += 1
	return ret

# def num_greater_than_mill(n):
# 	ret = 0
# 	r_max = n // 2
# 	r = r_max
# 	while r >= 1: # Going downwards from middle, as it is max there
# 		if choose(n, r) <= 1000000:
# 			break
# 		ret += 2 # 2 because of symmetry
# 		r -= 1

# 	if ret > 0 and n % 2 == 0: # Include the middle value
# 		ret -= 1
# 	return ret

total = 0
for n in range(1, 100 + 1):
	total += num_greater_than_mill(n)
print(total)