

import itertools as it

def non_divisible_subset(S, k):

    #S = list(S)
    pairs = {x: [] for x in S}
    for x, y in it.combinations(S, 2):
        if (x+y) % k == 0:
            pairs[x].append(y)
            pairs[y].append(x)

    while any((x+y) % k == 0 for x, y in it.combinations(pairs, 2)):
        most_pairs = None
        longest = float('-inf')
        for (x, ls) in pairs.items():
            if len(ls) > longest:
                most_pairs = x
                longest = len(ls)

        del pairs[most_pairs] 
        for x, ls in pairs.items():
            if most_pairs in ls:
                ls.remove(most_pairs)

    return len(pairs)

def test():
    S = set([1, 7, 2, 4])
    print('assert non_divisible_subset([1, 7, 2, 4]) == 3')
    assert non_divisible_subset(S, 3) == 3
    S = set([1, 7, 2, 4, 8])
    print('assert non_divisible_subset([1, 7, 2, 4, 8]) == 3')
    assert non_divisible_subset(S, 3) == 3
    S = set([9, 5, 7, 1, 3, 2, 6])
    print('assert non_divisible_subset([9, 5, 7, 1, 3, 2, 6]) == 3')
    assert non_divisible_subset(S, 3) == 3
    print('tests passed.')

if __name__ == '__main__':
    test()
    n, k = list(map(int, input().split(' ')))
    S = set(map(int, input().split(' ')))
    print(non_divisible_subset(S, k))
