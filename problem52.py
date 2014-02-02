# It can be seen that the number, 125874, and its double, 251748, 
# contain exactly the same digits, but in a different order.

# Find the smallest positive integer, x,
# such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

############
# Solution #
############

def digitsInNumber(n):
	digits = [False] * 10
	while n > 0:
		digits[n % 10] = True
		n = n // 10
	return digits

def containsSameDigits(digits_a, digits_b):
	for i in range(10):
		if (digits_a[i] != digits_b[i]):
			return False
	return True

def getAnswer():
	n = 1
	while n < 200000:
		d_n = digitsInNumber(n)
		answer = True
		for i in range(2, 7):
			d_i_n = digitsInNumber(i * n)
			if not containsSameDigits(d_n, d_i_n):
				answer = False
				break
		if answer:
			return n
		n += 1
	return 0

print(getAnswer())