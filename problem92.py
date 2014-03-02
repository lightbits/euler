# A number chain is created by continuously adding the square of the digits 
# in a number to form a new number until it has been seen before.

# For example,

# 44 → 32 → 13 → 10 → 1 → 1
# 85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

# Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. 
# What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

# How many starting numbers below ten million will arrive at 89?

############
# Solution #
############

# We can be clever here.
# For example, the number 999 reduces to checking if 243 arrives at 89
# The number 9999 reduces to checking if 324 arrives at 89
# 99999 to 405, and so on, up to 999 999 9 which reduces to 567.
# That is, large numbers immediately reduce to much smaller numbers.

# So we could make a lookup table for the numbers from 1 to 567 and
# check if they arrive at 89. Checking larger numbers should then be 
# simple by doing a single pass over the digits, and then checking
# with the LUT.

# This is still pretty slow though, because one to ten million is a lot
# of numbers. Even just doing a lookup per iteration takes a long time.

def squareDigits(n):
	ret = 0
	while n > 0:
		d = n % 10
		ret += d * d
		n = n // 10
	return ret

def chain(n):
	next = squareDigits(n)
	if next == 89:
		return True
	elif next == 1:
		return False
	else:
		return chain(next)

lut = {}
for n in range(1, 567 + 1):
	lut[n] = chain(n)

ans = 0
for n in range(1, 10000000):
	first_pass = squareDigits(n)
	if lut[first_pass]:
		ans += 1
print(ans)