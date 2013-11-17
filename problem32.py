# We shall say that an n-digit number is pandigital 
# if it makes use of all the digits 1 to n exactly once; 
# for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 × 186 = 7254, 
# containing multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity
# can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to 
# only include it once in your sum.

# Solution
# --------
# Note that we cannot have a 4+ digit product, as if we have a 5 digit product
# where the remaining 4 digits must form the multiplicand and multiplier, 
# it is not possible to obtain the smallest product 12345 with the remaining digits.
# We cannot have a less than 4-digit product either, as the multiplicand and multiplier
# would then have to be both 3-digit numbers. The product of two 3-pandigital numbers has
# more than 3 digits.

# Thus, the product is a 4-digit or less pandigital number.

# Note that the multiplicand, multiplier and product must in total be 1 to 9 pandigital.
# Thus, none can share any digits, and the multiplican and multiplier must be a total of
# 5 digits.

import math

def isSolution(a, b, c):
	digits = [0] * 10
	while a > 0:
		d = a % 10
		digits[d] += 1
		if digits[d] > 1:
			return False
		a = a // 10
	while b > 0:
		d = b % 10
		digits[d] += 1
		if digits[d] > 1:
			return False
		b = b // 10
	while c > 0:
		d = c % 10
		digits[d] += 1
		if digits[d] > 1:
			return False
		c = c // 10
	return digits == [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

s = 0
unusuals = set()
for a in range(1000, 10000):
	# b <= sqrt(a), because otherwise c would be < sqrt(a),
	# but we already have that solution!
	limit = int(math.sqrt(a) + 1)
	for b in range(2, limit):
		if a % b == 0:
			c = a // b
			if isSolution(a, b, c):
				unusuals.add(a)

for i in unusuals:
	s += i
print(s)