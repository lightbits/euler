# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

############
# Solution #
############

# Dust off the discrete maths notebook and remember that
# (a + b) mod n = (a mod n) + (b mod n) mod n

def pow(a, b):
	ret = a
	for i in range(1, b):
		ret *= a
	return ret

mod_sum = 0
tens = 10000000000 # mod'ing with this gives ten digits
for n in range(1, 1001):
	mod_sum += pow(n, n) % tens
print(mod_sum % tens)