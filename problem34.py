# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

# Solution
# Finding an upper bound:
# Note that with an 8-digit upper bound, the maximum result can be 9! * 8 = 2903040, which is less than the number itself.
# With a 7-digit upper bound, the maximum result can be 9! * 7 = 2540160,
# thus we can choose 2 540 160 as an upper bound.

# We can also graph y=10^x together with y=9!x, and decide their intersection (2 309 171). 10^x will grow much larger than 9!x after this point, which means a number after this point will be guaranteed larger than the sum of the factorials of its digits.

# 0!, 1!, 2!, ..., 9!
factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

def isCurious(n):
	m = n
	while m > 0:
		digit = m % 10
		m = m // 10
		n -= factorials[digit]
	return n == 0

# Slow solution, we can probably be more clever about this...
answer = 0
for n in range(10, 2309171):
	if isCurious(n):
		answer += n
print(answer)

