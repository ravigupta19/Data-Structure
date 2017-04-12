class Node(object):

    def __init__(self,data):
        self.data = data
        self.next = None

    def getNext(self):
        return self.next

    def getData(self):
        return self.data

    def setNext(self, next):
        self.next = next

    def setData(self, data):
        self.data = data


class CircularSinglyLinkedList(object):

    def __init__(self):
        self.head = None
        self.count = 0

    def addNodeAtStart(self, data):
        new_node = Node(data)
        if self.count == 0:
            new_node.setNext(new_node)
        else:
            current = self.head
            while current.getNext() != self.head:
                current = current.getNext()
            current.setNext(new_node)
            new_node.setNext(self.head)
        self.head = new_node
        self.count += 1


    def addNodeAtEnd(self,data):
        new_node = Node(data)
        if self.count == 0:
            self.head = new_node
            new_node.setNext(new_node)
        else:
            current = self.head
            while current.getNext() != self.head:
                current = current.getNext()
            current.setNext(new_node)
            new_node.setNext(self.head)
        self.count += 1

    def addNodeAtPosition(self,data,position):
        if  position > self.count or position < 1:
            print('Invalid position')
            return
        elif position == self.count:
            self.addNodeAtEnd(data)
        elif position == 1:
            self.addNodeAtStart(data)
        else:
            new_node = Node(data)
            current = self.head
            current_position = 1
            while current_position != position:
                current = current.getNext()
                current_position += 1
            next = current.getNext()
            current.setNext(new_node)
            new_node.setNext(next)
        self.count += 1

    def deleteNodeAtStart(self):
        if self.count == 0:
            print('List is empty')
            return
        else:
            current = self.head
            while current.getNext() != self.head:
                current = current.getNext()
            next = self.head.getNext()
            current.setNext(next)
            self.head = next
            self.count -= 1

    def deleteNodeAtEnd(self):
        if self.count == 0:
            print('List is empty')
        else:
            current = self.head
            while current.getNext() != self.head:
                previous = current
                current = current.getNext()
            previous.setNext(self.head)
            current.setNext(None)
            self.count -= 1


    def deleteNodeAtPosition(self, position):
        if position > self.count or position < 1:
            print('Invalid position')
        elif position == self.count:
            self.deleteNodeAtEnd()
        elif position == 1:
            self.deleteNodeAtStart()
        else:
            current = self.head
            current_position = 1
            while current_position != position:
                previous = current
                current = current.getNext()
                current_position += 1
            next = current.getNext()
            previous.setNext(next)
            current.setNext(None)
            self.count -= 1

    def printAllNode(self):
        current = self.head
        count = 1
        while count <= self.count:
            print('---------------------------------')
            print('Data {0}'.format(current.getData()))
            print('Current {0}'.format(current))
            #print('Previous {0}'.format(current.getPrevious()))
            print('Next {0}'.format(current.getNext()))
            print('---------------------------------')
            current = current.getNext()
            count += 1



cll = CircularSinglyLinkedList()
cll.addNodeAtStart(10)
cll.addNodeAtEnd(12)
cll.addNodeAtEnd(14)
cll.addNodeAtEnd(19)
cll.addNodeAtStart(9)
cll.addNodeAtPosition(15,4)
#cll.printAllNode()
cll.deleteNodeAtStart()
#cll.printAllNode()
cll.deleteNodeAtEnd()
#cll.printAllNode()
cll.deleteNodeAtPosition(3)
cll.printAllNode()
