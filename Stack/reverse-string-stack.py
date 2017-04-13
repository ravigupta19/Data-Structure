class Stack(object):

    def __init__(self):
        self.stk = []
        self.top = None

    def push(self,data):
        self.stk.append(data)
        self.top = self.stk[-1]

    def pop(self):
        res = self.stk.pop()
        self.top = self.stk[-1]
        return res


stack = Stack()
for char in input().split():
    stack.push(char)

stack.pop()
