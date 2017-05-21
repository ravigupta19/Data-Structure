class Node(object):

    def __init__(self,data):
        self.data = data
        self.parent = None
        self.rank = 0

class DisjointSet(object):

    def __init__(self):
        self.set = {}

    def makeSet(self, data):
        new_node = Node(data)
        new_node.parent = new_node
        self.set[data] = new_node

    def union(self, data1, data2):
        node1 = self.set[data1]
        node2 = self.set[data2]

        parent1 = self.findSetByCompersion(node1)
        parent2 = self.findSetByCompersion(node2)

        if parent1.data == parent2.data:
            return
        else:
            if parent1.rank >= parent2.rank:
                parent2.parent = parent1
                parent1.rank = parent1.rank + 1 if parent1.rank == parent2.rank else parent1.rank
            else:
                parent1.parent = parent2


    def findSetByCompersion(self,node):
        if node.parent == node:
            return node
        else:
            node.parent = self.findSetByCompersion(node.parent)
            return node.parent

    def findSet(self, data):
        return self.findSetByCompersion(self.set[data]).data

ds = DisjointSet()
for i in range(1,8):
    ds.makeSet(i)

ds.union(1, 2)
ds.union(2, 3)
ds.union(4, 5)
ds.union(6, 7)
ds.union(5, 6)
ds.union(3, 7)

for key in ds.set.keys():
    print(ds.findSet(key))

