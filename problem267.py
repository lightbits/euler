# -*- coding: utf-8 -*-
# You are given a unique investment opportunity.
# Starting with £1 of capital, you can choose a fixed proportion, f, 
# of your capital to bet on a fair coin toss repeatedly for 1000 tosses.

# Your return is double your bet for heads and you lose your bet for tails.

# For example, if f = 1/4, for the first toss you bet £0.25, and if heads 
# comes up you win £0.5 and so then have £1.5. You then bet £0.375 and 
# if the second toss is tails, you have £1.125.

# Choosing f to maximize your chances of having at least £1,000,000,000 
# after 1,000 flips, what is the chance that you become a billionaire?

# All computations are assumed to be exact (no rounding), 
# but give your answer rounded to 12 digits behind the decimal point in the form 0.abcdefghijkl.

############
# Solution #
############

import random
import math

# Returns minimum x (the number of heads) that is required for
#	[(1 + 2f) ^ (x)] * [(1 - f) ^ (n - x)] >= m.
# That is, for x heads and n - x tails of n coin tosses to yield
# money greater than m.
def result(f, n, m):
	incr = 1 + f * 2
	decr = 1 - f
	for x in range(0, n + 1):
		money = pow(incr, x) * pow(decr, n - x)
		if money >= m:
			return x
	return n + 1

# Find best f
f = 0.01
m_f = f
m_x = result(f, 1000, 1000000000)
while f <= 0.3:
	x = result(f, 1000, 1000000000)
	if x < m_x:
		m_x = x
		m_f = f
	f += 0.001

print(m_f)

# Gave f = 0.1300000 with x = 432.
# That is, if f = 0.13 and you get atleast 432 heads,
# you become a billionaire?
# Assuming that lowest x <=> best chance of getting
# enough heads in a given sequence.
# Maybe bad assumption?

# Now then, what is the probability of getting atleast 432 heads
# in 1000 tosses?

# P = sum from x=432 to 1000 { (1000 C x) * (0.5) ^ 1000 }
# Kinda hard to calculate though...
# Could do 1 - sum from x = 0 to 431 { P(x) } = 1 - P(X <= 431)

# Calculate (n C x) / (2 ^ n) and return it as a fraction (num, den)
def P(n, x):
	# For example: n = 10, x = 5
	# 			 	10 9 8 7 6
	#	result = ---------------
	#			 [5 4 3 2 1] * 2^10
	n0 = n
	x0 = x
	numerator = 1
	denominator = 1
	for i in range(x0):
		numerator *= n
		denominator *= x
		if numerator % denominator == 0:
			numerator = numerator // denominator
			denominator = 1
		n -= 1
		x -= 1
	for i in range(n0):
		if numerator % 2 == 0:
			numerator = numerator // 2
		else:
			denominator *= 2
	return numerator, denominator

answer = 1.0
for x in range(0, 431 + 1):
	n, d = P(1000, x)
	answer -= n / d
print(answer)

# 0.999 99 283 618 671 36
# 0.999 99 283 618 7
# Right answer!!! :D

# def prob(x):
# 	num_x = 0
# 	for i in range(1000):
# 		num_heads = 0
# 		for j in range(10):
# 			coin = random.randint(0, 1)
# 			if coin == 0:
# 				num_heads += 1
# 		if num_heads == x:
# 			num_x += 1
# 	return num_x / 1000.0

# def plot(x_min, x_max, width, P):
# 	max_p = P(x_min)
# 	p_list = {}
# 	for x in range(x_min, x_max + 1):
# 		p = P(x)
# 		max_p = max(p, max_p)
# 		p_list[x] = p
# 	for (x, p) in p_list.items():
# 		row = "#" * math.ceil(width * (p / max_p))
# 		print("%d\t%s%.2f" % (x, row, p))


# plot(0, 10, 20, prob)

