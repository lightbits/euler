# The first known prime found to exceed one million digits was discovered in 1999, 
# and is a Mersenne prime of the form 2^6972593 − 1; it contains exactly 2,098,960 
# digits. Subsequently other Mersenne primes, of the form 2^p − 1, have been found 
# which contain more digits.

# However, in 2004 there was found a massive non-Mersenne prime which contains 
# 2,357,207 digits: 28433 × 2^7830457 + 1.

# Find the last ten digits of this prime number.

############
# Solution #
############

# From number theory:
# 	a + b (mod n) = a (mod n) + b (mod n) (mod n)
# which that we can do m * a (mod n) by adding a,
# taking the modulo, adding a, taking the modulo again,
# etc...

# Also:
# a × b (mod n) ~ (a mod n) × (b mod n) (mod n)
# For example: The last two digits of 2^64 is 16.
# We can find them this way:
# 2^32 mod 100 is 96
# so 2^64 mod 100 = 2^32 × 2^32 mod 100 = 96 × 96 mod 100 = 16

tens = 10000000000

m = 2 # The digits
e = 2 # Initial exponent

# Slightly speedier route
while (e + 10 < 7830457 + 1):
	m = (m * 1024) % tens
	e += 10

# The last stretch
while (e < 7830457 + 1):
	m = (m + m) % tens
	e += 1

n = m % tens
for i in range(28433 - 1):
	m = ((m % tens) + n) % tens

m = (m + 1) % tens
print(m)