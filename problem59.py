# Each character on a computer is assigned a unique code and the 
# preferred standard is ASCII (American Standard Code for Information Interchange). 
# For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

# A modern encryption method is to take a text file, convert the bytes to ASCII, 
# then XOR each byte with a given value, taken from a secret key. 
# The advantage with the XOR function is that using the same encryption key on the cipher text,
 # restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

# For unbreakable encryption, the key is the same length as the plain text message,
# and the key is made up of random bytes. The user would keep the encrypted message 
# and the encryption key in different locations, and without both "halves", 
# it is impossible to decrypt the message.

# Unfortunately, this method is impractical for most users, 
# so the modified method is to use a password as a key. 
# If the password is shorter than the message, which is likely, 
# the key is repeated cyclically throughout the message. 
# The balance for this method is using a sufficiently long password key for security, 
# but short enough to be memorable.

# Your task has been made easy, as the encryption key consists of three lower case characters. 
# Using cipher1.txt (right click and 'Save Link/Target As...'), 
# a file containing the encrypted ASCII codes, 
# and the knowledge that the plain text must contain common English words, 
# decrypt the message and find the sum of the ASCII values in the original text.

############
# Solution #
############

# Read file
text_file = open("cipher1.txt")
text = text_file.read()
text_file.close()
text = text.split(',')

def decrypt(text, cipher):
	xor_pattern = [ord(char) for char in cipher]
	i = 0
	imax = len(xor_pattern)
	result = ""
	for ascii in text:
		xor_val = xor_pattern[i]
		i = (i + 1) % imax
		result += chr( xor_val ^ int(ascii) )
	print(i)
	return result

# Guessing there is a space at the 12th and 14th character
# That is 68 (the 12th char) xor n = 32 (' ')
# Which gives n = 100 ('d')
# Counting backwards makes this the last character in the cipher,
# assuming rotation starts at first character (xyzxyzxyz...).

# for i in range(ord('a'), ord('z') + 1):
# 	if i ^ 73 == ord('.'):
# 		print(i)
# print(chr(103))

# We can assume that the text ends on a punctuation mark
# So 73 (the last ascii) xor n must equal 46 ('.'),
# which gives n = 103 ('g')
# Counting symbols shows that this is the first character of the cipher.

# Just need to find the second character in the cipher!

# for i in range(97, 123):
# 	print(decrypt(text, ['g', chr(i), 'd']))
# 	print(i)
# 	s = input("...")

# And it was 111 ('o'), so the cipher was "god"

decrypted = decrypt(text, "god")
answer = 0
for char in decrypted:
	answer += ord(char)
print(answer)