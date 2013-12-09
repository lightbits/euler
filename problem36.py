# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, 
# which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, 
# may not include leading zeros.)

# Solution
# There are probably fewer palindromic binary numbers below one million, than decimal.
# 20 bits give a maximum value of slightly more than one million. 
# So we can go through all permutations 10 bits, 
# reflect the bits to form a 20 bit palindromic binary number, 
# and see if the number in decimal is also palindromic.

# For example: 1101 becomes 11011011, 110101011 or 110111011.

def toBinary(dec):
	bin = []
	while dec > 0:
		bin.append(dec % 2)
		dec = dec // 2
	bin.reverse()
	return bin

def isPalindrome(bin):
	length = len(bin)
	lim = len(bin) // 2
	for i in range(lim):
		if bin[i] != bin[length - i - 1]:
			return False
	return True

answer = 0

for n in range(1000):
	# Reflect digits
	tens = 1
	left = n
	right = 0
	m = n
	while m > 0:
		tens *= 10
		right *= 10
		right += m % 10
		m = m // 10

	# We can form the palindrome left + right, or left+i+right,
	# where i is between 0 and 9.
	left = left * tens
	pal_dec = left + right
	pal_bin = toBinary(pal_dec)
	if isPalindrome(pal_bin):
		answer += pal_dec

	left *= 10
	if left > 1000000:
		continue
	for i in range(10):
		pal_dec = left + i * tens + right
		pal_bin = toBinary(pal_dec)
		if isPalindrome(pal_bin):
			answer += pal_dec

print(answer)