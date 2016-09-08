A = [1, 3, 4, 6, None,  None]
B = [2, 5]

def merge_two_sorted(list1, list2):
    list1_len = len(list1)
    index1 = list1_len - len(list2) - 1 #end of list1
    index2 = len(list2) - 1 #end of list2
    index3 = list1_len #beginning of placement
    for i in range(list1_len, -1, -1):
        if list1[index1] > list2[index2]:
            tmp = list1[index3]
            list1[index3] = list1[index2]
            list1[index2] = tmp
        else:
            tmp = list1[index3]
            list1[index3] = list1[index2]
            list1[index2] = tmp
    return list1

print merge_two_sorted(A,B)
