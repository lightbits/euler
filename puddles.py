# In this picture we have walls of different heights. 
# This picture is represented by an array of integers, 
# where the value at each index is the height of the wall. 
# The picture above is represented with an array as [2,5,1,2,3,4,7,7,6].

# Now imagine it rains. 
# How much water is going to be accumulated in puddles between walls

# wall_heights = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
wall_heights = [2, 5, 1, 3, 1, 2, 1, 7, 7, 6]
max_height = max(wall_heights)

def waterLevels(wall_heights):
	n = len(wall_heights)
	result = [0] * n
	left_max = 0
	right_max = 0
	for i in range(n // 2 + 1):
		left_max = max(left_max, wall_heights[i])
		right_max = max(right_max, wall_heights[n - 1 - i])
		level = min(left_max, right_max)
		result[i] = level
		result[n - 1 - i] = level
	return result

water_levels = waterLevels(wall_heights)
graph = []
for y in range(1, max_height + 1):
	row = ""
	for i in range(len(wall_heights)):
		if y == wall_heights[i]:
			row += str(y)
		elif y < wall_heights[i]:
			row += " "
		elif y <= water_levels[i]:
			row += "x"
		else:
			row += " "
	graph.append(row)

graph = reversed(graph)
for row in graph:
	print(row)