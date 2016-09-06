

def insert(N, M, i, j):
    N = N & ~(!(1 << (j-1)) << i)
    return N | (M << i)
