# Jessie
# time complexity - o(n)
# space complexity - O(1)

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

link_list = Node(3, (Node(4, Node(5, Node(6)))))
link_list2 = Node(1, Node(2, Node(3, (Node(4, Node(5, Node(6, Node(7))))))))
        
def k_to_last(link_list, k):
    if link_list is None:
        return None
    j = link_list
    i = link_list
    while j.next != None:
        j = j.next
        if k == 0:
            i = i.next
        elif k > 0:
             k -= 1        
    if k != 0:
        return None
    return i.value


#tests
print str(k_to_last(link_list, 1)) + " = 5"
print str(k_to_last(link_list2, 3)) + " = 4"
print str(k_to_last(link_list2, 7)) + " = 4"
