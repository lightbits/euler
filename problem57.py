# It is possible to show that the square root of two can 
# be expressed as an infinite continued fraction.

# √ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

# By expanding this for the first four iterations, we get:

# 1 + 1/2 							= 3/2	= 1.5
# 1 + 1/(2 + 1/2) 					= 7/5	= 1.4
# 1 + 1/(2 + 1/(2 + 1/2)) 			= 17/12	= 1.41666...
# 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) 	= 41/29	= 1.41379...

# The next three expansions are 99/70, 239/169, and 577/408, 
# but the eighth expansion, 1393/985, is the first example 
# where the number of digits in the numerator exceeds the 
# number of digits in the denominator.

# In the first one-thousand expansions, how many fractions 
# contain a numerator with more digits than denominator?

############
# Solution #
############

# Returns a (simplified) fraction n / d = a + b / c
def simplify(a, b, c):
	n = b + a * c
	return (n, c)

def solve(depth):
	n = 1
	d = 2

	while depth >= 1:
		# simplify and do reciprocal
		d, n = simplify(2, n, d)
		depth -= 1

	# Last depth, 1 + n / d
	return simplify(1, n, d)

def numDigits(n):
	num = 0
	while n > 0:
		num += 1
		n = n // 10
	return num

answer = 0
for i in range(1000):
	n, d = solve(i)
	if numDigits(n) > numDigits(d):
		answer += 1
print(answer)