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
            parent2.parent = parent1
        else:
            parent1.parent = parent2

    def findSet(self,node):
        if node.parent == node:
            return node
        node.parent = self.findSet(node.parent)
        return  node.parent

    def findSetData(self,data):
        return self.findSet(self.listOfSet[data]).data

ds = DisjointSet()
ds.makeSet(1)
ds.makeSet(2)
ds.makeSet(3)
ds.makeSet(4)
ds.makeSet(5)
ds.makeSet(6)
ds.makeSet(7)

ds.union(1,2)
ds.union(2,3)
ds.union(4,5)
ds.union(6,7)
ds.union(5,6)
ds.union(3,7)

print(ds.findSetData(7))


print(ds.listOfSet)