# A unit fraction contains 1 in the numerator. 
# The decimal representation of the unit fractions with denominators 2 to 10 are given:

# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. 
# It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in 
# its decimal fraction part.
############################

# Bruteforce solution
for d in range(2, 1000):

	# Keep track of when in the expansion which remainder appears
	remainders = []
	for r in range(0, d):
		remainders.append(-1)

	# We expand 1 / d and keep track of the remainders.
	# Note that we only need to do at most d-1 expansions, because
	# if we have d-1 unique remainders after d-1 expansions (that is, no cycle),
	# then the d'th expansion must give a remainder we already have, thus 
	# leading to a cycle. (Because there are only d-1 unique remainders of any
	# number divided by d)
	cycle = 0
	numerator = 10
	for i in range(0, d): # only consider first d-1 decimals
		# quotient = int(numerator / d)
		remainder = numerator % d
		numerator = remainder * 10

		if(remainders[remainder] == -1):
			remainders[remainder] = i
		else:
			# We got a previous remainder, thus there is a cycle from
			# where it first occurred to here
			cycle = i - remainders[remainder]
			break

		if numerator == 0: # d is a divisor of numerator
			break

	if cycle != 0:
		print("1 / %d has a cycle of length %d" % (d, cycle))
	else:
		print("1 / %d is regular" % (d))

# Not part of solution, but nice for debugging
# def getFractionPart(a, b, max):
# 	ret = []
# 	i = 0
# 	# perform long division and keep track of the quotients
# 	while(a != 0 and i < max):
# 		a *= 10
# 		q = int(a / b)
# 		ret.append(q)
# 		a = a % b
# 		i += 1
# 	return ret