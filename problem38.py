# Take the number 192 and multiply it by each of 1, 2, and 3:

# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576

# By concatenating each product we get the 1 to 9 pandigital, 192384576. 
# We will call 192384576 the concatenated product of 192 and (1,2,3)

# The same can be achieved by starting with 9 and multiplying 
# by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, 
# which is the concatenated product of 9 and (1,2,3,4,5).

# What is the largest 1 to 9 pandigital 9-digit number that 
# can be formed as the concatenated product of an integer with 
# (1,2, ... , n) where n > 1?

############
# Solution #
############

import math

# One-to-nine pandigital
def isPandigital(n):
	digits = [False] * 10
	while n > 0:
		digit = n % 10
		if digit == 0 or digits[digit]:
			return False
		digits[digit] = True
		n = n // 10
	return True

def pow10(n):
	result = 1
	for i in range(n):
		result *= 10
	return result

# Returns the concatenated 9-digit number
# i x 1 cat i x 2 cat ... i x n
def concatenateProduct(i):
	cat = i
	digit_count = int(math.log10(cat)) + 1
	k = 2
	while digit_count < 9:
		pp = i * k
		pp_digits = int(math.log10(pp)) + 1
		digit_count += pp_digits
		cat *= pow10(pp_digits)
		cat += pp
		k += 1
	return cat

greatest = 0
i = 9999
while i > 10:
	p = concatenateProduct(i)
	if isPandigital(p) and p > greatest:
		greatest = p
	i -= 1

print(greatest)