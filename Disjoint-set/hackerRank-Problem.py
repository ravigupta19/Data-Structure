import sys


class Node(object):
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.rank = 0


class DisjointSet(object):
    def __init__(self):
        self.setdict = {}

    def makeSet(self, data):
        new_node = Node(data)
        new_node.parent = new_node
        self.setdict[data] = new_node

    def union(self, data1, data2):
        node1 = self.setdict[data1]
        node2 = self.setdict[data2]

        parent1 = self.findByCompression(node1)
        parent2 = self.findByCompression(node2)

        if parent1 == parent2:
            return False
        else:
            if parent1.rank >= parent2.rank:
                parent2.parent = parent1
                parent1.rank = parent1.rank + 1 if parent1.rank == parent2.rank else parent1.rank
            else:
                parent1.parent = parent2
            return True

    def findByCompression(self, node):

        if node.parent == node:
            return node
        else:
            node.parent = self.findByCompression(node.parent)
            return node.parent

    def find(self, data):
        return self.findByCompression(self.setdict[data]).name


class City(object):

    def __init__(self, numberCity, noOfRoad, costLibrary, costRoad):
        self.numberCity = numberCity
        self.edges = []
        self.costRoad = costRoad
        self.costLibrary = costLibrary
        self.noOfRoad = noOfRoad

    def calculateCostofLibrary(self, numberCity):
        return self.costLibrary * numberCity

    def calculateNoOfRoad(self):
        count = 0
        ds = DisjointSet()
        for i in range(1, self.numberCity + 1):
            ds.makeSet(i)
        for edge in self.edges:
            if ds.union(edge[0], edge[1]):
                count += 1
        return count

    def addEdge(self, startingVertex, endVertex):
        self.edges.append([startingVertex, endVertex])

    def totalCost(self):
        noOFtotalroad = self.numberCity - 1
        actualRoadBuild = self.calculateNoOfRoad()
        noOfLibaray = noOFtotalroad - actualRoadBuild
        totalCostOfroad = self.calculateCostofLibrary(noOfLibaray+1) + actualRoadBuild * self.costRoad
        totalCostOfLibaray = self.calculateCostofLibrary(self.numberCity)
        print(min(totalCostOfroad,totalCostOfLibaray))


q = int(input().strip())
for a0 in range(q):
    n, m, x, y = input().strip().split(' ')
    n, m, x, y = [int(n), int(m), int(x), int(y)]
    city = City(n, m, x, y)
    for a1 in range(m):
        city_1, city_2 = input().strip().split(' ')
        city_1, city_2 = [int(city_1), int(city_2)]
        city.addEdge(city_1,city_2)
    city.totalCost()


