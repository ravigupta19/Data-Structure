import heapq
INF = 1000000
class PriorityQueueMap(object):
    def __init__(self):
        self.eq = []
        self.entry_finder = {}

    def add(self, key, prioprity = INF):
        if key in self.entry_finder:
             raise KeyError("Key already exists")
        self.entry_finder[key] = prioprity
        heapq.heappush(self.eq,[prioprity, key])

    def delete(self, task):
        if not task in self.entry_finder:
            raise KeyError("Key doesnt exist")
        self.entry_finder.pop(task)

    def getMin(self):
        minVertex = heapq.heappop(self.eq)[1]
        self.entry_finder.pop(minVertex)
        return minVertex

    def descrease(self, key, priority):
        previousPriority = self.entry_finder[key]
        self.entry_finder[key] = priority
        index = self.eq.index([previousPriority, key])
        del self.eq[index]
        heapq.heappush(self.eq,[priority, key])

class Vertex(object):

    def __init__(self, data):
        self.name = data
        self.adjanceyList = []
        self.visited = False

    def addNeighbours(self,neighbour):
        self.adjanceyList.append(neighbour)

class Graph():

    def __init__(self):
        self.vertexList = {}
        self.edgeList = []

    def addEdge(self,u,v,w):
        self.edgeList.append([u,v,w])
        self.vertexList[u].addNeighbours(v)
        self.vertexList[v].addNeighbours(u)

    def addVertex(self,data):
        self.vertexList[data] = Vertex(data)

    def PrimsAlgorithm(self, startVertex):
        resultEdge = []
        vertexEdge = {}
        queue = PriorityQueueMap()
        for key in self.vertexList.keys():
            queue.add(key)
        queue.descrease(startVertex, 0)
        while len(queue.entry_finder) > 0:
            vertex = queue.getMin()
            if vertex in vertexEdge:
                resultEdge.append(vertexEdge[vertex])
            for neighbours in self.vertexList[vertex].adjanceyList:
                

                





        






graph = Graph()
for i in range(ord("A"), ord("G")):
    graph.addVertex(chr(i))
graph.addEdge("A","D",1)
graph.addEdge("A","B",3)
graph.addEdge("B","D",3)
graph.addEdge("B","C",1)
graph.addEdge("C","E",5)
graph.addEdge("C","D",1)
graph.addEdge("C","F",4)
graph.addEdge("D","E",6)
graph.addEdge("F","E",2)
graph.PrimsAlgorithm("A")