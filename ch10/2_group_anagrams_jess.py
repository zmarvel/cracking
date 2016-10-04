#Jessie

initial = ["abc", "dog", "cba", "god"]
# ["abc", "cba", "dog", "god"]

def group_anagrams(words):
	return sorted(words, cmp=lambda x,y: cmp(x, y))

print group_anagrams(initial)
