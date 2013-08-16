# An alien appears to two perfectly logical mathematicians who never lie, Sam and Polly.
# The alien says, “I’m thinking of two numbers, X and Y with 3 <= X <= Y <= 97.
# I will tell their sum to Sam and their product to Polly.”

# The alien does this and then disappears. Then, this conversation takes place.
# Sam: You don’t know what X and Y are.
# Polly: That’s true, but now I do.
# Sam: And now I do too.

# Find X and Y.

# http://blog.ultimatepronoun.com/?p=21

import math

def isPrime(n):
	for i in range(2, int(math.sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True

primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,
	97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,
	197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,
	313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,
	439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,
	571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,
	691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,
	829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,
	977,983,991,997]

def primeFactors(n):
	ret = []
	for p in primes:
		while n % p == 0:
			n = n / p
			ret.append(p)
	return ret

def possiblePairsFromSum(sum):
	ret = []
	x = int(sum / 2)
	y = int(sum / 2)
	if(sum % 2 != 0):
		y += 1
	
	while(x >= 3 and y <= 97):
			ret.append((x, y))
			x -= 1
			y += 1
	
	return ret

# returns the set of pairs (x, y), where 3<=x<=y<=97, such that x * y = p
def possiblePairsFromProduct(p):
	ret = []
	for m in range(3, int(p / 2)):
		if(p % m == 0):
			q = p / m
			if(q >= 3 and q <= m and m <= 97):
				ret.append((int(q), int(m)))

	return ret

sumsThatSamCanHave = []
for s in range(3 + 3, 97 + 97 + 1):
	pairs = possiblePairsFromSum(s)
	allProductsAmbiguous = True
	for x, y in pairs:
		if(len(possiblePairsFromProduct(x * y)) == 1):
			allProductsAmbiguous = False

	# Sam: "You do now know what x and y are."
	# Sam must be able to say this with absolute certainty.
	if(allProductsAmbiguous):
		sumsThatSamCanHave.append(s)

# assume p is the product. is there only one valid pair that multiply to p, and
# that add up to a sum in the list of sums that sam can have?
def doesPollyKnow(sumsThatSamCanHave, p):
	possibles = []
	for z, w in possiblePairsFromProduct(p):
		if((z + w) in sumsThatSamCanHave and (z, w) not in possibles):
			possibles.append((z, w))

	return (len(possibles) == 1)

for s in sumsThatSamCanHave:
	# Assume s is the sum told to Sam
	print("Sam (%d): You don't know what x and y are." % s)
	for x, y in possiblePairsFromSum(s):
		print("%d, %d, Polly (%d): " % (x, y, x * y), end="")
		
		if(doesPollyKnow(sumsThatSamCanHave, x * y)):
			print("That's true. But now I do.")
		else:
			print("That's true.")

	print()
	input()