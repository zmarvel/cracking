
# Jessie

A = [1, 3, 4, 6, None,  None]
B = [2, 5]

def merge_two_sorted(list1, list2):
    index1 = len(list1) - len(list2) - 1 #end of list1
    index2 = len(list2) - 1 #end of list2
    index3 = len(list1) - 1 #beginning of placement
    for i in range(index3, -1, -1):
        if index2 < 0 or list1[index1] > list2[index2]:
            list1[i] = list1[index1]
            index1 -= 1
        else:
            list1[i] = list2[index2]
            index2 -= 1
        index3 -= 1
    return list1
    
print merge_two_sorted(A,B)



# Zack, python3

def sorted_merge(A, B, n, m):
    assert len(B) == m
    assert (m + n) == len(A)

    idxA = n-1
    idxB = m-1
    head = len(A)-1
    while head >= 0:
        if idxB < 0 or A[idxA] > B[idxB]:
            A[head] = A[idxA]
            idxA -= 1
        else:
            A[head] = B[idxB]
            idxB -= 1
        head -= 1
    return A

assert sorted_merge([1, 2, 3, 4, 5, None, None], [6, 7], 5, 2) == [1, 2, 3, 4, 5, 6, 7]
assert sorted_merge([1, 3, 5, None, None], [2, 4], 3, 2) == [1, 2, 3, 4, 5]
assert sorted_merge([-2, 0, 0, 3, None, None, None], [-1, 2, 4], 4, 3) == [-2, -1, 0, 0, 2, 3, 4]
