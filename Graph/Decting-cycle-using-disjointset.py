class Node(object):

    def __init__(self,data):
        self.data = data
        self.parent = None
        self.rank = 0

class DisjointSet(object):
    listOfSet = {}

    def makeSet(self, data):
        new_node = Node(data)
        new_node.parent = new_node
        self.listOfSet[data] = new_node

    def union(self,data1, data2):

        node1 = self.listOfSet[data1]
        node2 = self.listOfSet[data2]

        parent1 = self.findSet(node1)
        parent2 = self.findSet(node2)

        if parent1.data == parent2.data:
            return
        if parent1.rank >= parent2.rank:
            parent1.rank = parent1.rank + 1 if parent1.rank == parent2.rank else parent1.rank
            #parent1.rank = parent1.rank  + 1
            parent2.parent = parent1
        else:
            parent2.rank = parent2.rank + 1
            parent1.parent = parent2

    def findSetByCompersion(self,node):
        if node.parent == node:
            return node
        node.parent = self.findSet(node.parent)
        return  node.parent

    def findSetData(self,data):
        return self.findSet(self.listOfSet[data]).data
        #return self.findSet(self.listOfSet[data]).rank

class Graph(object):

    def __init__(self):
        self.edges = []
        self.vertex = []
        self.ds = DisjointSet()

    def hasCycle(self):

        for i in self.getAllVertex():
            self.ds.makeSet(i)

    def getAllVertex(self):
        return self.vertex




