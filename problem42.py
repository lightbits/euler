# The nth term of the sequence of triangle numbers is given by, 
# tn = ½n(n+1); so the first ten triangle numbers are:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# By converting each letter in a word to a number corresponding 
# to its alphabetical position and adding these values we form a word value.
# For example, the word value for SKY is 19 + 11 + 25 = 55 = t_10.
# If the word value is a triangle number then we shall call the word a triangle word.

# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing
# nearly two-thousand common English words, how many are triangle words?

############
# Solution #
############

# The longest word is of length 14
# val(Z) * 14 = 390
# The lowest triangle number greater than 390 is t_28
MAX_N = 28

def triangleNumber(n):
	return n * (n + 1) // 2

def wordToValue(word):
	ret = 0
	for char in word:
		ret += ord(char) - 64
	return ret

is_triangle_number = [False] * triangleNumber(MAX_N + 1)
for n in range(MAX_N + 1):
	is_triangle_number[triangleNumber(n)] = True

words = []
with open("./words.txt") as f:
	content = f.readlines()[0]
	words = content.split("\",\"")
	words[0] = words[0][1:]
	words[len(words) - 1] = words[len(words) - 1][:-1]

num_triangle_words = 0
for word in words:
	word_value = wordToValue(word)
	if is_triangle_number[word_value]:
		num_triangle_words += 1

print(num_triangle_words)