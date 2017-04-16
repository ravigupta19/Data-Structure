class Queue(object):

    def __init__(self):
        self.queue = []
        self.top = None
        self.end = None

    def enqueue(self,data):
        self.queue.append(data)
        self.top = self.queue[0]
        if self.end is None:
            self.end = self.queue[-1]

    def dequeue(self):
        try:
            res = self.queue.pop(0)
            self.top = self.queue[0]
        except IndexError:
            self.top = None
            self.end = None

    def getTop(self):
        return self.top

    def display(self):
        print(' '.join(list(map(str,self.queue))))

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(4)
q.enqueue(7)
q.display()
q.dequeue()
q.display()
print(q.getTop())