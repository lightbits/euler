# The 5-digit number, 16807=7^5, is also a fifth power. 
# Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

# How many n-digit positive integers exist which are also an nth power?

############
# Solution #
############

def numDigits(n):
	result = 0
	while (n > 0):
		n = n // 10
		result += 1
	return result

# Note that the base can only go from 1 to 9, as any base above 9
# raised to a power n will always generate a number with more than n digits
# For example: 10^1 = 10 (2 digits), 10^2 = 100 (3 digits)

# How is the exponent limited though?
# For some exponent, n, and upwards, the number b^n will generate numbers
# with more than n digits. This limit can be found by solving
# 	lg10 (b^n) + 1 <= n
# 	b^n <= 10^(n - 1)
# That is, we break when the number 10^(n - 1) exceeds b^n

# For example: 10^(n - 1) exceeds 5^n at n = 3
# Any exponent applied to 5 greater than 3 will thus
# generate a number with more digits than the exponent.

ans = 0
for base in range(1, 10):
	tens = 1
	n = base
	exponent = 1
	while (tens <= n):
		tens *= 10
		if (numDigits(n) == exponent):
			print("%d^%d = %d" % (base, exponent, n))
			ans += 1
		exponent += 1
		n *= base

print(ans)