

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
