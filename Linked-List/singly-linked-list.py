#PNR 8357948831, 2658321936
class Node(object):
    def __init__(self):
        self.data = None
        self.next = None

    def setData(self, data):
        self.data = data

    def setNext(self, next):
        self.next = next

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def hasNext(self):
        return self.next == None

class LinkedList(object):

    def __init__(self):
        self.head = None
        self.count = 0

    def addNodeAtEnd(self, data):
        newNode = Node()
        newNode.setData(data)
        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            while current.next != None:
                current = current.getNext()
            current.setNext(newNode)
        self.count += 1

    def addNodeAtStart(self,data):
        newNode = Node()
        newNode.setData(data)
        if self.head == None:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode

    def addNodeAtPosition(self,data,position):
        if position > self.count or position < 0:
            return None
        else:
            if position == self.count:
                self.addNodeAtEnd(data)
            elif position == 0:
                self.addNodeAtStart(data)
            else:
                newNode = Node()
                newNode.setData(data)
                current = self.head
                currentPosition = 1
                while position != currentPosition:
                    current = current.getNext()
                    currentPosition += 1
                temp = current.getNext()
                current.setNext(newNode)
                newNode.setNext(temp)
            self.count += 1

    def deleteNodeAtStart(self):
        if self.count == 0:
            print('The list is empty')
        else:
            self.head = self.head.getNext()
            self.count -= 1

    def deleteNodeAtEnd(self):
        if self.count == 0:
            print('The list is empty')
        else:
            currentNode = self.head
            previousNode = self.head
            while currentNode.next != None:
                previousNode = currentNode
                currentNode = currentNode.getNext()
            currentNode.setNext(None)
            previousNode.setNext(None)
            self.count -= 1

    def deleteNodeAtPosition(self, position):
        if position > self.count or position < 0:
            print('Invalid Position')
        else:
            if position == 1:
                self.deleteNodeAtStart()
            elif position == self.count:
                self.deleteNodeAtEnd()
            else:
                currentPosition = 1
                previous= self.head
                current = self.head
                while currentPosition != position:
                    previous = current
                    current = current.getNext()
                temp = current.getNext()
                previous.setNext(temp)
                current.setNext(None)
                self.count -= 1


    def printLinkedListInReverse(self):
        if self.count == 0:
            print('The list is empty')
        elif self.count == 1:
            print(self.head.getData())
        else:


    def reverseLinkedList(self):


    def printAllNode(self):
        current = self.head
        while current.next != None:
            print(current.getData())
            current = current.getNext()
        print(current.getData())

    def getCount(self):
        return self.count

newLinkedList = LinkedList()
newLinkedList.addNodeAtEnd(4)
newLinkedList.addNodeAtEnd(8)
newLinkedList.addNodeAtEnd(0)
newLinkedList.addNodeAtStart(10)
newLinkedList.addNodeAtPosition(25,2)
newLinkedList.addNodeAtPosition(23,3)
newLinkedList.printAllNode()
print('')
newLinkedList.deleteNodeAtEnd()
newLinkedList.printAllNode()
print('')

newLinkedList.deleteNodeAtStart()
newLinkedList.printAllNode()
print('')

newLinkedList.deleteNodeAtPosition(3)
newLinkedList.printAllNode()

