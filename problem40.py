# An irrational decimal fraction is created by concatenating the positive integers:

# 0.123456789101112131415161718192021...

# It can be seen that the 12th digit of the fractional part is 1.

# If dn represents the nth digit of the fractional part, find the value of the following expression.

# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

############
# Solution #
############
import math

def nthDigit(n):
	i = 1
	d = 1
	while (i < n):
		i += int(math.log10(d + 1)) + 1
		d += 1
	remaining_digits = i - n
	while remaining_digits > 0:
		d = d // 10
		remaining_digits -= 1
	return d % 10

d1 = nthDigit(1)
d10 = nthDigit(10)
d100 = nthDigit(100)
d1000 = nthDigit(1000)
d10000 = nthDigit(10000)
d100000 = nthDigit(100000)
d1000000 = nthDigit(1000000)
print(d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000)