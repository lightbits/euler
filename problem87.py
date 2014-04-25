# The smallest number expressible as the sum of a prime square, prime cube, 
# and prime fourth power is 28. In fact, there are exactly four numbers below 
# fifty that can be expressed in such a way:

# 28 = 2^2 + 2^3 + 2^4
# 33 = 3^2 + 2^3 + 2^4
# 49 = 5^2 + 2^3 + 2^4
# 47 = 2^2 + 3^3 + 2^4

# How many numbers below fifty million can be expressed as the sum of a prime square, 
# prime cube, and prime fourth power?

############
# Solution #
############

import math

def isPrime(n):
	# skip multiples of two
	m = int(math.sqrt(n) + 1)
	for i in range(3, m):
		if n % i == 0:
			return False
	return True

prime_squares = [4]
prime_cubes = [8]
prime_quads = [16]

# We set the upper prime search limit to 7080,
# as 7080^2 > fifty million.
upper_limit = 100
for i in range(3, upper_limit, 2):
	if not isPrime(i):
		continue
	i2 = i * i
	i3 = i2 * i
	i4 = i3 * i
	prime_squares.append(i2)
	prime_cubes.append(i3)
	prime_quads.append(i4)

ans = []
dups = 0

for a in prime_squares:
	for b in prime_cubes:
		s = a + b
		for c in prime_quads:
			s += c
			if s <= 50000000:
				if (s in ans):
					dups += 1
				ans.append(s)
				# ans.add(s + c)

print(dups)
print(len(ans))