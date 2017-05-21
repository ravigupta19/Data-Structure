class Node(object):

    def __init__(self, data):
        self.data = data
        self.parent = None
        self.rank = 0

class DisjointSet(object):

    def __init__(self):
        self.setDict = {}

    def makeSet(self,data):
        new_node = Node(data)
        new_node.parent = new_node
        self.setDict[data] = new_node

    def union(self, parent1, parent2):

        if parent1.rank >= parent2.rank:
            parent2.parent = parent1
            parent1.rank = parent1.rank + 1 if parent1.rank == parent2.rank else parent1.rank
        else:
            parent1.parent = parent2


    def findSetByCompression(self,node):
        if node.parent == node:
            return node
        else:
            node.parent = self.findSetByCompression(node.parent)
            return node.parent

    def findSet(self,data):
        return self.findSetByCompression(self.setDict[data])


class Graph(object):

    def __init__(self, num):
        self.edgeList = []
        self.numberVertices = num

    def addEdge(self, u, v, w,):
        self.edgeList.append([u,v,w])

    def sortEdge(self):
        self.edgeList = sorted(self.edgeList,key=lambda l: l[2])

    def kruskalAlgorithm(self):
        added_edge_list = []
        ds = DisjointSet()

        for i in range(0,self.numberVertices):
            ds.makeSet(i)
        self.sortEdge()
        for arr in self.edgeList:
            parent1 = ds.findSet(arr[0])
            parent2 = ds.findSet(arr[1])

            if parent1 == parent2:
                continue
            else:
                ds.union(parent1,parent2)
                added_edge_list.append(arr)
        return added_edge_list


g = Graph(9)
g.addEdge(0,7,8)
g.addEdge(0,1,4)
g.addEdge(1,2,8)
g.addEdge(1,7,11)
g.addEdge(2,5,4)
g.addEdge(2,3,7)
g.addEdge(3,4,9)
g.addEdge(3,5,14)
g.addEdge(5,4,10)
g.addEdge(6,5,2)
g.addEdge(7,8,7)
g.addEdge(7,6,1)
g.addEdge(8,6,6)
g.addEdge(8,2,2)

print(g.kruskalAlgorithm())


