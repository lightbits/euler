# By replacing the 1st digit of the 2-digit number *3, 
# it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

# By replacing the 3rd and 4th digits of 56**3 with the same digit, 
# this 5-digit number is the first example having seven primes among the ten 
# generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, 
# and 56993. Consequently 56003, being the first member of this family, is the smallest prime 
# with this property.

# Find the smallest prime which, by replacing part of the number 
# (not necessarily adjacent digits) with the same digit, 
# is part of an eight prime value family.

############
# Solution #
############

# Stupid solution incoming!

import math

def genPatternsRecursive(patterns, base, length):
	if len(base) == length:
		return
	new_base_a = base[:] + "*"
	new_base_b = base[:] + "_"
	if len(new_base_a) == length:
		patterns.append(new_base_a)
		patterns.append(new_base_b)
		return
	else:
		genPatternsRecursive(patterns, new_base_a, length)
		genPatternsRecursive(patterns, new_base_b, length)

# Generates a list of patterns of the form "_**_" or "*_*_*_"
# of a given length
def genPatterns(length):
	base = ""
	patterns = []
	genPatternsRecursive(patterns, base, length)
	return patterns

# Takes a pattern (e.g. "_**_") and a list of digits
# (e.g. [1, 2, 2, 3]), and returns true if the stars
# in the pattern are occupied by the same digit.
# Also return a code to identify the family (e.g. "1**3" reversed)
def patternMatch(pattern, digits):
	replacement = -1
	code = ""
	for i in range(len(digits)):
		if pattern[i] == '_':
			code += str(digits[i])
			continue
		code += '*'
		if replacement == -1:
			replacement = digits[i]
		elif digits[i] != replacement:
			return (False, "")
	return (True, code)

def getDigits(n):
	digits = []
	while n > 0:
		digits.append(n % 10)
		n = n // 10
	return digits

def isPrime(n):
	# Ignore multiples of two
	for i in range(3, int(math.sqrt(n)) + 1, 2):
		if n % i == 0:
			return False
	return True

# Generate patterns for i-digit numbers
families = []
for i in range(1, 8):
	families.append(genPatterns(i))

# Go through each prime, find out what families it belongs to,
# and add one to each family's score
scores = {}
for n in range(3, 1000000, 2):
	if not isPrime(n):
		continue
	digits = getDigits(n)
	patterns = families[len(digits) - 1]
	for pattern in patterns:
		match, code = patternMatch(pattern, digits)
		if match:
			if code in scores:
				scores[code][1] += 1 # increment the score
			else:
				scores[code] = [n, 1] # n was the first prime

# Find the first family with a score >= 8
for code, (first, score) in scores.items():
	if score >= 8:
		print(first)
		break