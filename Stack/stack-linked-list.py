class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

    def setNext(self,next):
        self.next = next

    def setData(self,data):
        self.data = data

    def getData(self):
        return self.data

    def getNext(self):
        return self.next


class Stack(object):

    def __init__(self, limit = 10):
        self.limit = limit
        self.top = None
        self.count = 0

    def push(self, data):
        if self.isFull():
            print('Stack is Overflow')
            return
        else:
            new_node = Node(data)
            if self.top is not None:
                new_node.next = self.top
            self.top = new_node
            self.count += 1

    def pop(self):
        if self.isEmpty():
            print('Stack is empty')
        else:
            next = self.top.next
            self.top.next = None
            self.top = next
            self.count -= 1

    def getTop(self):
        return self.top.getData()

    def isFull(self):
        return self.count == self.limit

    def isEmpty(self):
        return self.count == 0

    def display(self):
        current = self.top
        while current is not None:
            print(current.getData())
            current = current.getNext()


stklinked = Stack()
stklinked.push(10)
stklinked.push(9)
stklinked.push(11)
stklinked.push(15)
stklinked.pop()
stklinked.pop()
stklinked.pop()
stklinked.pop()
stklinked.pop()