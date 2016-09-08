# 0 - (1) [0]
# 1 - (1) [1]
# 2 - (2) [1, 1], [2] 
# 3 - (4) [1, 1, 1], [1, 2], [2, 1], [3]
# 4 - 

#subtract 1
#subtract 2
#subtract 3

ways = {0: 0, 1:1, 2: 2, 3: 4}

#time complexity: O(n)
#space complexity: O(n)
def calculate_ways(steps):
    if steps < 4:
        return ways[steps]
    for i in range(4, steps + 1):
        ways[i] = ways[i-1] + ways[i-2] + ways[i-3]
    return ways[steps]

#time complexity: O(3^n)
#space complexity: O(3^n) in terms of stack size. Consider tail recursion?
def ways_recurse(steps):
    if steps < 4:
        return ways[steps]
    return ways_recurse(steps-1) + ways_recurse(steps-2) + ways_recurse(steps-3)

#time complexity: O(n)
#space complexity: O(n)
def ways_recurse(steps):
    if steps not in ways:
        ways[steps] = ways_recurse(steps-1) + ways_recurse(steps-2) + ways_recurse(steps-3)
    return ways[steps]

for i in range(29):
    print str(i) + ' ' +  str(ways_recurse(i))

# 0 0 
# 1 1 
# 2 2 
# 3 4 
# 4 7 
# 5 13 
# 6 24 
# 7 44 
# 8 81 
# 9 149 
# 10 274 
# 11 504 
# 12 927 
# 13 1705 
# 14 3136 
# 15 5768 
# 16 10609 
# 17 19513 
# 18 35890 
# 19 66012 
# 20 121415 
# 21 223317 
# 22 410744 
# 23 755476 
# 24 1389537 
# 25 2555757 
# 26 4700770 
# 27 8646064 
# 28 15902591 
