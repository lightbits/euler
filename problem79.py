# A common security method used for online banking 
# is to ask the user for three random characters from a passcode. 
# For example, if the passcode was 531278, they may ask for the 2nd, 
# 3rd, and 5th characters; the expected reply would be: 317.

# The text file, keylog.txt, contains fifty successful login attempts.

# Given that the three characters are always asked for in order, 
# analyse the file so as to determine the shortest possible secret passcode of unknown length.

############
# Solution #
############

# The file contains 50 successful logins for the same password.
# We want to determine the shortest possible passcode that is
# consistent with the file.

# For example:
# 319
# 680
# 180
# 3 appears before 1, thus we can deduce that 8 should go somewhere after 3.

# We can assume (?) that the string is comprised of unique numbers, if we don't
# have entries like 780 and 807 (which would imply multiple sevens).

# Example:
# 190 | 1 9 0
# 574 | 5 7 4 1 9 0 (guess that 574 goes before)
# 794 | 5 7 1 9 4 0 (7 precedes 9 OK; move 4 until 9 precedes 4;)
# 510 | 5 7 1 9 4 0 (nothing to do)
# 174 | 5 1 7 9 4 0 (move 7 until 1 precedes 7;)

def addInfo(current, new):

	# Add non-existing items
	for i in range(len(new)):
		l = new[len(new) - 1 - i]
		if l not in current:
			current.insert(0, l)

	# Go through each item except the last, 
	# controlling that its successor in the new string
	# is consistent with the current string (modifying
	# it if not).
	for i in range(len(new) - 1):
		node = new[i]
		successor = new[i + 1]
		nodeIndex = current.index(node)
		succIndex = current.index(successor)
		if nodeIndex > succIndex:
			current.insert(nodeIndex + 1, successor)
			del current[succIndex]
	return current

current = []
# Test 1: 517940
# print(addInfo(current, [1, 9, 0]))
# print(addInfo(current, [5, 1, 0]))
# print(addInfo(current, [7, 9, 4]))
# print(addInfo(current, [1, 7, 4]))
# print(addInfo(current, [5, 7, 4]))

# Test 2: 9453120
# print(addInfo(current, [9, 3, 1]))
# print(addInfo(current, [4, 5, 3]))
# print(addInfo(current, [5, 1, 0]))
# print(addInfo(current, [5, 1, 2]))
# print(addInfo(current, [9, 2, 0]))
# print(addInfo(current, [9, 5, 1]))
# print(addInfo(current, [9, 4, 5]))

f = open("keylog.txt")
current = []
for line in f:
	new = []
	for num in line.strip():
		new.append(num)
		addInfo(current, new)
print(current)