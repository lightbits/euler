import math
# The Fibonacci sequence is defined by the recurrence relation:

# Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:

# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.

# What is the first term in the Fibonacci sequence to contain 1000 digits?
##############################

# Gives us at most 1001 digits (10000^201 has 1001 digits)
COEFFICIENT_COUNT = 201
BASE = 100000

# Returns a base 10000 number
def BigNumber():
	coefficients = [0] * COEFFICIENT_COUNT
	return coefficients

# Adds two BigNumbers (coefficients are ordered from least to most significant)
def add(lhs, rhs):
	result = BigNumber()
	carry = 0
	for i in range(0, COEFFICIENT_COUNT):
		result[i] = carry
		result[i] += lhs[i] + rhs[i]
		carry = int(result[i] > BASE - 1)
		result[i] = result[i] % BASE
	return result

# Returns the digit count of a BigNumber
def digitCount(b):
	maxDigits = 1001
	digitsPerCoefficient = 5 # A coefficient is between 0 and 99999

	# Find the first non-zero coefficient.
	# The digit count will then be 1001 - the index where that coefficient
	# starts.
	for i in reversed(range(0, COEFFICIENT_COUNT)):
		if b[i] > 0:
			return maxDigits - (COEFFICIENT_COUNT - 1 - i) * digitsPerCoefficient + int(math.log10(b[i]))
	return 0

def getString(b):
	ret = "%d" % b[COEFFICIENT_COUNT - 1]
	for i in reversed(range(0, COEFFICIENT_COUNT - 1)):
		digits = len("%d" % b[i])
		pad = "0" * (5 - digits)
		ret += "%s%d" % (pad, b[i])
	return ret

f0 = BigNumber()
f1 = BigNumber()
f0[0] = 0
f1[0] = 1
for i in range(2, 5001):
	f2 = add(f0, f1)
	f0 = f1[:] # copy
	f1 = f2[:] # copy
	if(digitCount(f2) >= 1000):
		print("The first fibonacci term to have 1000 digits is %d" % i)
		break