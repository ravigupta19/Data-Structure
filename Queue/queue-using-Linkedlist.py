class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

    def setNext(self,next):
        self.next = next

    def setData(self, data):
        self.data = data

    def getNext(self):
        return self.next

    def getData(self):
        return self.data

class Queue(object):

    def __init__(self):
        self.top = None
        self.end = None

    def enqueue(self,data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            current = self.top
            while current.next is not None:
                current = current.next
            current.setNext(new_node)
        self.end = new_node

    def dequeue(self):
        self.top = self.top.next
        if self.top is None:
            self.end = None

    def getTop(self):
        return self.top

    def display(self):
        current = self.top
        while current is not None:
            print(current.data)
            current = current.next


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(5)
q.enqueue(8)
q.enqueue(9)
q.dequeue()
q.display()