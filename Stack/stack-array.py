class Stack(object):

    def __init__(self, limit=10):
        self.stk = []
        self.top = None
        self.limit = limit

    def push(self,data):
        if len(self.stk) == self.limit:
            print('Stack Overflow')
            return
        self.stk.append(data)

    def length(self):
        return len(self.stk)

    def pop(self):
        if self.isEmpty():
            print('Stack is Underflow')
            return
        return self.stk.pop()

    def isEmpty(self):
        return len(self.stk) == 0

    def display(self):
        if self.isEmpty():
            print('Stack is Empty')
            return
        print(' '.join(list(map(str,self.stk))))

    def getTop(self):
        try:
            return self.stk[-1]
        except IndexError:
            print('Stack is Empty')

stk = Stack()
stk.push(3)
stk.push(4)
print(stk.getTop())
stk.pop()
stk.push(9)
stk.push(10)
stk.pop()
stk.display()
print(stk.getTop())
