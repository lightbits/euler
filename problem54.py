# In the card game poker, a hand consists of five cards and are ranked, 
# from lowest to highest, in the following way:

# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

# If two players have the same ranked hands then the rank made up of the highest value wins; 
# for example, a pair of eights beats a pair of fives (see example 1 below). 
# But if two ranks tie, for example, both players have a pair of queens, then highest cards 
# in each hand are compared (see example 4 below); 

# if the highest cards tie then the next highest cards are compared, and so on.

# The file, poker.txt, contains one-thousand random hands dealt to two players. 
# Each line of the file contains ten cards (separated by a single space): 
# the first five are Player 1's cards and the last five are Player 2's cards. 
# You can assume that all hands are valid (no invalid characters or repeated cards), 
# each player's hand is in no specific order, and in each hand there is a clear winner.

# How many hands does Player 1 win?

#############
# Solution ##
#############

JACK = 11
QUEEN = 12
KING = 13
ACE = 14

HIGH_CARD = 0
ONE_PAIR = 1
TWO_PAIRS = 2
THREE_KIND = 3
STRAIGHT = 4
FLUSH = 5
FULL_HOUSE = 6
FOUR_KIND = 7
STRAIGHT_FLUSH = 8
ROYAL_FLUSH = 9

def cardValueToInt(v):
	if v == 'T':
		return 10
	if v == 'J':
		return JACK
	elif v == 'Q':
		return QUEEN
	elif v == 'K':
		return KING
	elif v == 'A':
		return ACE
	else:
		return ord(v) - int(ord("0"))

def getValue(card):
	return card[0]

def getSuit(card):
	return card[1]

# Number of different card values
def numDifferent(hand):
	diff = 1
	prev = getValue(hand[0])
	for card in hand[1:]:
		value = getValue(card)
		if value != prev:
			diff += 1
		prev = value
	return diff

# All cards of the same suit.
def isFlush(hand):
	prev_suit = getSuit(hand[0])
	for card in hand[1:]:
		suit = getSuit(card)
		if suit != prev_suit:
			return False
		prev_suit = suit
	return True

# Returns the rank value
def getHandRank(hand):
	flush = isFlush(hand)
	diff = numDifferent(hand)
	straight = diff == 5 and getValue(hand[4]) - getValue(hand[0]) == 4

	if straight and flush and getValue(hand[0]) == 10:
		return ROYAL_FLUSH
	elif straight and flush:
		return STRAIGHT_FLUSH
	elif diff == 2 and (getValue(hand[4]) != getValue(hand[3]) or getValue(hand[1]) != getValue(hand[0])):
		return FOUR_KIND
	elif diff == 2:
		return FULL_HOUSE
	elif flush:
		return FLUSH
	elif straight:
		return STRAIGHT
	elif numDifferent(hand[0:3]) == 1 or numDifferent(hand[1:4]) == 1 or numDifferent(hand[2:5]) == 1:
		return THREE_KIND
	elif diff == 3:
		return TWO_PAIRS
	elif diff == 4:
		return ONE_PAIR
	else:
		return HIGH_CARD

def getHandValue(hand, rank):
	if rank == ROYAL_FLUSH or rank == STRAIGHT_FLUSH or rank == FLUSH or rank == STRAIGHT:
		# Highest card
		return getValue(hand[4])
	elif rank == FOUR_KIND:
		# The value of the card occuring four times
		if numDifferent(hand[0:4]) == 1:
			return getValue(hand[0])
		else:
			return getValue(hand[4])
	elif rank == FULL_HOUSE or rank == THREE_KIND:
		# The value of the card occuring three times
		if numDifferent(hand[0:3]) == 1:
			return getValue(hand[0])
		elif numDifferent(hand[1:4]) == 1:
			return getValue(hand[1])
		else:
			return getValue(hand[2])
	elif rank == TWO_PAIRS or rank == ONE_PAIR:
		# The value of the card of the highest pair
		for i in range(len(hand) - 1, 0, -1):
			if getValue(hand[i]) == getValue(hand[i - 1]):
				return getValue(hand[i])
	else:
		# Highest card
		return getValue(hand[4]) 

def popHighest(hand):
	return getValue(hand[len(hand) - 1]), hand[:-1]

def compareHighest(hand_1, hand_2):
	while len(hand_1) > 0:
		highest_1, hand_1 = popHighest(hand_1)
		highest_2, hand_2 = popHighest(hand_2)
		if highest_1 > highest_2:
			return 1
		elif highest_1 < highest_2:
			return 2
	return 0

def sort(hand):
	return sorted(hand, key=lambda card: card[0]) # Sort by card value

lines = []
with open("poker.txt") as f:
	lines = f.readlines()

wins = 0
ties = 0
for line in lines:
	cards = line.split()
	hand = []
	for card in cards:
		value = cardValueToInt(card[0])
		suit = card[1]
		hand.append((value, suit))
	hand_1 = hand[:5]
	hand_2 = hand[5:]

	hand_1 = sort(hand_1)
	hand_2 = sort(hand_2)

	rank_1 = getHandRank(hand_1)
	rank_2 = getHandRank(hand_2)

	if rank_1 > rank_2:
		wins += 1
		# print("Player 1 rank:", rank_1, rank_2)
		continue
	elif rank_1 < rank_2:
		# print("Player 2 rank:", rank_1, rank_2)
		continue

	value_1 = getHandValue(hand_1, rank_1)
	value_2 = getHandValue(hand_2, rank_2)

	if value_1 > value_2:
		wins += 1
		# print("Player 1 value:", rank_1, rank_2, value_1, value_2)
		continue
	elif value_1 < value_2:
		# print("Player 2 value:", rank_1, rank_2, value_1, value_2)
		continue

	highest = compareHighest(hand_1, hand_2)
	if highest == 1:
		wins += 1
		# print("Player 1 highest:", rank_1, rank_2, value_1, value_2)
		continue
	elif highest == 2:
		# print("Player 2 highest:", rank_1, rank_2, value_1, value_2)
		continue
	else:
		ties += 1

print(wins, ties)