class Node(object):

    def __init__(self,data, next = None, previous = None):
        self.data = data
        self.next = next
        self.previous = previous

    def setData(self, data):
        self.data = data

    def setPrevious(self, previous):
        self.previous = previous

    def setNext(self, next):
        self.next = next

    def getData(self):
        return  self.data

    def getNext(self):
        return self.next

    def getPrevious(self):
        return  self.previous

class DoubleLinkedList(object):

    def __init__(self):
        self.head = None
        self.count = 0

    def addNodeAtEnd(self, data):
        new_node = Node(data)
        if self.count == 0:
            self.head = new_node
        else:
            current = self.head
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(new_node)
            new_node.setPrevious(current)
        self.count += 1

    def addNodeAtStart(self,data):
        new_node = Node(data)
        if self.count == 0:
            self.head = new_node
        else:
            current = self.head
            current.setPrevious(new_node)
            new_node.setNext(current)
            self.head = new_node
        self.count += 1


    def addNodeAtPosition(self,data,position):
        if position > self.count or position < 0:
            print('Print Invalid Position')
        else:
            if position == self.count:
                self.addNodeAtEnd(data)
            elif position == 1:
                self.addNodeAtStart(data)
            else:
                current = self.head
                new_node = Node(data)
                current_position = 1

                while current_position != position:
                    current = current.getNext()
                    current_position += 1

                next = current.getNext() #Getting next node
                current.setNext(new_node) #setting current->next = new_node
                new_node.setPrevious(current) #setting new_node->previous = current
                new_node.setNext(next) #setting new_node -> next = next
                next.setPrevious(new_node) #next->previous = new_node
            self.count+=1



    def deleteNodeAtStart(self):
        if self.count == 0:
            print('List Is Empty')
        else:
            current = self.head
            next = current.getNext()
            current.setNext(None)
            next.setPrevious(None)
            self.head = next
            self.count -= 1


    def deleteNodeAtEnd(self):
        if self.count == 0:
            print('List is empty')
        else:
            current = self.head
            while current.getNext() != None:
                current = current.getNext()
            previous = current.getPrevious()
            current.setPrevious(None)
            previous.setNext(None)
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
                current = current.getNext()
                current_position += 1
            previous = current.getPrevious()
            next = current.getNext()
            previous.setNext(next)
            next.setPrevious(previous)
            current.setPrevious(None)
            current.setNext(None)
        self.count -= 1


    def reverseDoubleLinkedList(self):
        pass

    def printAllNode(self):
        current = self.head
        while current != None:
            print('---------------------------------')
            print('Data {0}'.format(current.getData()))
            print('Current {0}'.format(current))
            print('Previous {0}'.format(current.getPrevious()))
            print('Next {0}'.format(current.getNext()))
            print('---------------------------------')
            current = current.getNext()

    def getCount(self):
        return self.count

d = DoubleLinkedList()
d.addNodeAtEnd(12)
d.addNodeAtEnd(13)
d.addNodeAtEnd(15)
d.addNodeAtEnd(19)
d.addNodeAtStart(10)
d.addNodeAtPosition(14,3)
d.printAllNode()
d.deleteNodeAtStart()
d.deleteNodeAtEnd()
d.deleteNodeAtPosition(2)
d.printAllNode()