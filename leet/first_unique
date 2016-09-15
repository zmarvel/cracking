def first_unique(string):
	char_dict = {}
	for i, char in enumerate(string):
		if char in char_dict:
			char_dict[char] = [i, 1]
		else:
			char_dict[char] = [i, 0]
	min_index = len(string)
	print char_dict
	for key in char_dict.keys():
		if not char_dict[key][1] and char_dict[key][0] < min_index:
			min_index = char_dict[key][0]
	if min_index == len(string):
		return -1
	else:
		return min_index
print first_unique("llaabb")
