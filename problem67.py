# By starting at the top of the triangle below and 
# moving to adjacent numbers on the row below, the 
# maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom in triangle.txt

############
# Solution #
############

# Read file into list of rows
triangle = []
with open("triangle.txt") as f:
	for line in f:
		row = []
		for word in line.split():
			row.append(int(word))
		triangle.append(row)

# Collapses row a with row b,
# producing a new row with len(a) elements,
# containing the largest sums of adjacent elements
# in a and b.
def collapse(a, b):
	result = []
	for i in range(len(a)):
		result.append(max(a[i] + b[i], a[i] + b[i + 1]))
	return result

# Collapse triangle until we get solution
i = len(triangle) - 1
final = triangle[i]
while i > 0:
	final = collapse(triangle[i - 1], final)
	i -= 1
print(final)