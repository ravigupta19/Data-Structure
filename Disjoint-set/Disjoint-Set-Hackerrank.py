class Node(object):

    def __init__(self, data):
        self.data = data
        self.parent = None
        self.size = 1


class DisjointSet(object):

    def __init__(self):
        self.set = {}

    def makeSet(self,data):
        new_node = Node(data)
        new_node.parent = new_node
        self.set[data] = new_node

    def union(self,data1, data2):

        node1 = self.set[data1]
        node2 = self.set[data2]

        parent1 = self.findSetByCompression(node1)
        parent2 = self.findSetByCompression(node2)

        if parent1.data == parent2.data:
            return
        else:
            if parent1.size >= parent2.size:
                parent2.parent = parent1
                parent1.size = parent1.size + parent2.size
            else:
                parent1.parent = parent2
                parent2.size = parent2.size + parent1.size

    def findSetByCompression(self,node):
        if node.parent == node:
            return node
        else:
            node.parent = self.findSetByCompression(node.parent)
            return node.parent

    def findSizeOfCommunity(self,data):
        return self.findSetByCompression(self.set[data]).size

ds = DisjointSet()
n,q = list(map(int,input().split()))
for i in range(1,n+1):
    ds.makeSet(i)
for _ in range(q):
    input_list = list(input().split())
    if input_list[0] == 'Q':
        print(ds.findSizeOfCommunity(int(input_list[1])))
    elif input_list[0] == 'M':
        ds.union(int(input_list[1]),int(input_list[2]))