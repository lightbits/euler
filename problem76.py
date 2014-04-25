# It is possible to write five as a sum in exactly six different ways:

# 4 + 1
# 3 + 2
# 3 + 1 + 1
# 2 + 2 + 1
# 2 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1

# How many different ways can one hundred be written as a sum of at least two positive integers?

############
# Solution #
############

# 4 + 1: - || -
# 3 + 2: has two distinct digits, and only two digits, nothing to do
# 3 + 1 + 1: has two distinct digits, -||-
# 2 + 2 + 1: has two distinct digits, - || -
# 2 + 1 + 1 + 1: has two distinct digits, can either add two similar or add two unlike
# 1 + 1 + 1 + 1 + 1: has one distinct digit, can add two similiar

digits = [1, 1, 1, 1, 1]
while len(digits) > 2:
	# Add first two
	# Add second two?
	new_a = [digits[0] + digits[1]]
	new_a.append(digits[2:])
	new_b = [digits[0], digits[1] + digits[2]]
	new_b.append(digits[3:])
	
	print(new_a, new_b)