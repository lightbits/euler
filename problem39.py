# If p is the perimeter of a right angle triangle with integral length sides, 
# {a,b,c}, there are exactly three solutions for p = 120.

# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p ≤ 1000, is the number of solutions maximised?

############
# Solution #
############

import math
from time import time
sqrt_2 = math.sqrt(2)

def numSolutions(p):
	a_lim = p // 3
	num_solutions = 0
	for a in range(1, a_lim + 1):
		b_lim = p - a
		for b in range(a, b_lim):
			c = b_lim - b
			c_sqrd = c * c
			aabb = a * a + b * b
			if aabb > c_sqrd:
				break
			elif aabb == c_sqrd:
				num_solutions += 1
	return num_solutions

t0 = time()

max_num_solutions = 0
solution = 0
for p in range(1, p_lim):
	num_solutions = numSolutions(p)
	if num_solutions > max_num_solutions:
		max_num_solutions = num_solutions
		solution = p

t = time() - t0
print("It took %ds" % t)
print(max_num_solutions)
print(solution)