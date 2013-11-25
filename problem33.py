# The fraction 49/98 is a curious fraction, 
# as an inexperienced mathematician in attempting to simplify it 
# may incorrectly believe that 49/98 = 4/8, which is correct, 
# is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, 
# less than one in value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms, 
# find the value of the denominator.

# Solution
# There are four possible cases:
# 1) ax/bx = a/b and
# 2) xa/xb = a/b, which give the trivial solutions a=b, 0<=x<=9
# 3) ax/xb = a/b, which gives the solution x = 9ab/(10a-b)
# 4) xa/bx = a/b, which gives the solution x = 9ab/(10b-a)
# In the last two cases, 0 < x <= 9

# Note that here, ax means 10a + x, and so on.

for a in range(1, 10):
	for b in range(1, 10):
		if a == b or a < b: # Trivial solution or not solution
			continue

		if 9 * a * b % (10 * a - b) == 0:
			x = 9 * a * b // (10 * a - b)
			if x > 0 and x <= 9:
				print("%d%d/%d%d" % (a, x, x, b))
		elif 9 * a * b % (10 * b - a) == 0:
			x = 9 * a * b // (10 * b - a)
			if x > 0 and x <= 9:
				print("%d%d/%d%d" % (x, a, b, x))