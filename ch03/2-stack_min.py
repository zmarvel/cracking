

class StackMin():
    def __init__(self):
        self.stack = []

    def min(self):
        if self.stack == []:
            return None
        else:
            value, info = self.stack[-1]
            return info

    def push(self, value):
        smallest = self.min()
        self.stack.append((value, value if smallest is None else min(value, smallest)))

    def pop(self):
        if self.stack == []:
            return None
        else:
            value, info = self.stack.pop()
            return value

def test():
    stk = StackMin()
    items = [10, 9, 8, 7, 8, 9, 8, 7, 6, 5, 6, 1]
    for item in items:
        stk.push(item)
        print('pushed {}. current min: {}.'.format(item, stk.min()))
    for _ in items:
        item = stk.pop()
        print('popped {}. current min: {}.'.format(item, stk.min()))
    assert stk.pop() is None
        
if __name__ == '__main__':
    test()


#Jessie's solution
# 1 -> 2 -> 3

class StackMin:
    def __init__(self):
        self.stack = []
    def push(self, to_push):
        if not self.stack or self.stack[-1][1] > to_push:
            self.stack.append([to_push, to_push])
        else:
            self.stack.append([to_push, self.stack[-1][1]])
    def pop(self):
        if self.stack == []:
            return None
        return self.stack.pop()[0]
    def min(self):
        if self.stack == []:
            return None
        return self.stack[-1][1]
    
my_stack = StackMin()
my_stack.push(5)
print my_stack.stack, my_stack.min()
my_stack.push(6)
print my_stack.stack, my_stack.min()
my_stack.push(3)
print my_stack.stack, my_stack.min()
my_stack.push(7)
print my_stack.stack, my_stack.min()
