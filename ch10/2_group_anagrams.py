

store = {}
def anagram_key(s):
    if s not in store:
        store[s] = sorted(s)
    return store[s]

def group_anagrams(ls):
    ls = sorted(ls, key=lambda s: anagram_key)
    return ls

def test():
    from random import shuffle

    l = [
        "ascot",
        "coats",
        "coast",
        "sushi",
        "tacos",
        "angel",
        "breakfast",
        "angle",
        "glean",
        "deist",
        "coffee",
        "diets",
        "edits",
        "sited",
        "tides",
        ]
    shuffle(l)

    print(group_anagrams(l))

if __name__ == '__main__':
    test()
