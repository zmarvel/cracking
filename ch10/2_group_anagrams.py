

def group_anagrams(ls):
    store = {}
    ls = sorted(ls, key=lambda s: store[s] if s in store else sorted(s))
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
