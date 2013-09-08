# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral
# is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

import math

# Note that the last out number on the top-right of the square is the length of the diagonal squared
# The numbers on the top-right half-diagonal are 3^2, 5^2, 7^2, ...
# The numbers on the top-left half-diagonal are 3^2 - 2, 5^2 - 4, 7^2 - 6
# The numbers on the bottom-left half-diagonal are 3^2 - 2 - 2, 5^2 - 4 - 4, 7^2 - 6 - 6, ...
# The numbers on the bottom-right half-diagonal are 3^2 - 2 - 2 - 2, 5^2 - 4 - 4 - 4, 7^2 - 6 - 6 - 6, ...

diagSum = 1
for i in range(1, math.floor(1001 / 2) + 1):
	n = 2 * i + 1
	topRight = n * n
	topLeft = topRight - (n - 1)
	bottomLeft = topLeft - (n - 1)
	bottomRight = bottomLeft - (n - 1)
	diagSum += topRight + topLeft + bottomLeft + bottomRight

print(diagSum)