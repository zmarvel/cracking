# 0 - (1) [0]
# 1 - (1) [1]
# 2 - (2) [1, 1], [2] 
# 3 - (4) [1, 1, 1], [1, 2], [2, 1], [3]
# 4 - 

#subtract 1
#subtract 2
#subtract 3

ways = {0: 0, 1:1, 2: 2, 3: 4}

def calculate_ways(steps):
    if steps < 4:
        return ways[steps]
    for i in range(4, steps + 1):
        ways[i] = ways[i-1] + ways[i-2] + ways[i-3]
    return ways[steps]

ways = {0: 0, 1:1, 2: 2, 3: 4}

def ways_recurse(steps):
    if steps < 4:
        return ways[steps]
    return ways_recurse(steps-1) + ways_recurse(steps-2) + ways_recurse(steps-3)

def ways_recurse(steps):
    if steps not in ways:
        ways[steps] = ways_recurse(steps-1) + ways_recurse(steps-2) + ways_recurse(steps-3)
    return ways[steps]

for i in range(29):
    print str(i) + ' ' +  str(ways_recurse(i))
