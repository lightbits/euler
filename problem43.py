# The number, 1406357289, is a 0 to 9 pandigital number 
# because it is made up of each of the digits 0 to 9 in some order, 
# but it also has a rather interesting sub-string divisibility property.

# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.

############
# Solution #
############

# We permute the numbers 1023456789 to
# generate lexicographic orderings of all 0 to 9 pandigital numbers.
# (Note that numbers beginning with 0 do not count!)
# We then perform the divisibility check on each substring
# starting from the lowest (as it is the most stable)

def nextPermutation(p):
	n = len(p)
	i = n - 1
	while i > 0 and p[i - 1] >= p[i]:
		i -= 1

	if i == 0:
		return [] # done

	pivot = i - 1

	# Find smallest number that is greater than pivot
	j = n - 1
	while j > 0 and p[j] <= p[pivot]:
		j -= 1

	p[pivot], p[j] = p[j], p[pivot]
	p[i:] = reversed(p[i:])
	return p

primes = [2, 3, 5, 7, 11, 13, 17]
def hasProperty(p):
	i = 0
	j = 3
	while i <= 6:
		sub = p[j] + p[j - 1] * 10 + p[j - 2] * 100
		if sub % primes[i] != 0:
			break
		j += 1
		i += 1
	return i == 7

answer = 0
p = [1, 0, 2, 3, 4, 5, 6, 7, 8, 9]
while len(p) > 0:
	if not hasProperty(p):
		p = nextPermutation(p)
		continue

	n = 0
	for d in p:
		n *= 10
		n += d
	answer += n
	print(n)
	p = nextPermutation(p)

print(answer)