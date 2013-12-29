def nextPermutation(p):
	# Find the longest non-increasing suffix
	seq_len = len(p)
	suffix = seq_len - 1
	while suffix > 0 and p[suffix - 1] >= p[suffix]:
		suffix -= 1

	# No pivot means we have reached the last permutation
	if suffix == 0:
		return p

	# Find the rightmost successor to the pivot
	pivot = suffix - 1
	successor = seq_len - 1
	while successor > 0 and p[successor] <= p[pivot]:
		successor -= 1

	# Swap them
	p[pivot], p[successor] = p[successor], p[pivot]

	# Sort suffix in non-descending order (reverse it)
	p[suffix:] = reversed(p[suffix:])
	return p

# Returns the next decreasing lexicographic permutation,
# and whether or not it is the lowest permutation.
def prevPermutation(p):
	# The idea is that we want to decrease the sequence as little as possible
	# Find the longest non-decreasing suffix (the longest, lowest permutation)
	seq_len = len(p)
	suffix = seq_len - 1
	while suffix > 0 and p[suffix - 1] <= p[suffix]:
		suffix -= 1

	# If there is no pivot then we have the lowest permutation and are done
	if suffix == 0:
		return p, True

	# Find first element from the right that is smaller than the pivot
	pivot = suffix - 1
	pred = seq_len - 1
	while pred > pivot and p[pred] >= p[pivot]:
		pred -= 1

	# Swap it with the pivot
	p[pivot], p[pred] = p[pred], p[pivot]

	# Reverse the suffix (giving the greatest permutation)
	p[suffix:] = reversed(p[suffix:])
	return p, False