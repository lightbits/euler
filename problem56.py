# A googol (10^100) is a massive number: one followed by one-hundred zeros; 
# 100^100 is almost unimaginably large: one followed by two-hundred zeros. 
# Despite their size, the sum of the digits in each number is only 1.

# Considering natural numbers of the form, ab, where a, b < 100, 
# what is the maximum digital sum?

############
# Solution #
############

def pow(a, b):
	result = 1
	while b > 0:
		result *= a
		b -= 1
	return result

def digitSum(n):
	result = 0
	while n > 0:
		result += n % 10
		n = n // 10
	return result

ans = 0
for a in range(1, 100):
	for b in range(1, 100):
		ds = digitSum(pow(a, b))
		if ds > ans:
			ans = ds
print(ans)