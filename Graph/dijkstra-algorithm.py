INF = 100000
import heapq
class PriorityQueueMap(object):

    def __init__(self):
        self.eq = []
        self.eq_finder = {}

    def add(self, key, priority=INF):
        self.eq_finder[key] = priority
        heapq.heappush(self.eq, [priority,key])

    def getMin(self):
        minVertex = heapq.heappop(self.eq)[1]
        self.eq_finder.pop(minVertex)
        return minVertex

    def decrease(self,key, priority):
        previousPriority = self.eq_finder[key]
        self.eq_finder[key] = priority
        index = self.eq.index([previousPriority, key])
        del self.eq[index]
        heapq.heappush(self.eq,[priority,key])

class Edge(object):

    def __init__(self, startVertex, endVertex, weight):
        self.startVertex = startVertex
        self.endVertex = endVertex
        self.weight = weight

class Vertex(object):

    def __init__(self,name):
        self.name = name
        self.neighbours = []
        self.visited = False
        self.edges = []

    def addNeighbour(self,v):
        self.neighbours.append(v)


class Graph(object):

    def __init__(self, numVertex):
        self.numberVertex = numVertex
        self.vertexs = {}
        self.edges = []

    def addVertex(self, name):
        vertex = Vertex(name)
        self.vertexs[name] = vertex

    def addEdge(self, u, v, w):
        edge = Edge(u,v,w)
        self.vertexs[u].addNeighbour(v)
        self.vertexs[v].addNeighbour(u)
        self.vertexs[u].edges.append(edge)
        self.vertexs[v].edges.append(edge)
        self.edges.append(edge)

    def DijkstraAlgorithm(self, sourceVertex = 0):
        vertexParent = {}
        vertexDistance = {}
        queue = PriorityQueueMap()
        for key in self.vertexs.keys():
            queue.add(key)
        queue.decrease(sourceVertex,0)
        vertexParent[sourceVertex] = None
        vertexDistance[sourceVertex] = 0

        while len(queue.eq_finder) > 0:
            currentVertex = queue.getMin()
            print("CurrentVertex ",currentVertex)
            for edge in self.vertexs[currentVertex].edges:
                print("Start vertex", edge.startVertex)
                print("End Vertex", edge.endVertex)
                print("Weight ",edge.weight)
                otherVertex = self.get_other_vertex_for_edge(currentVertex, edge)
                if not otherVertex in queue.eq_finder:
                    continue

                new_distance = int(edge.weight) + int(vertexDistance[currentVertex])
                if queue.eq_finder[otherVertex] > new_distance:
                    vertexParent[otherVertex] = currentVertex
                    vertexDistance[otherVertex] = new_distance
                    queue.decrease(otherVertex, new_distance)
        print(vertexParent)
        print(sorted(vertexDistance.items(), key=lambda s: s[0]))

    def get_other_vertex_for_edge(self, vertex, edge):
        if edge.startVertex == vertex:
            return edge.endVertex
        else:
            return edge.startVertex

graph = Graph(9)
for i in range(graph.numberVertex):
    graph.addVertex(i)
graph.addEdge(0,1,4)
graph.addEdge(0,7,8)
graph.addEdge(1,2,8)
graph.addEdge(1,7,11)
graph.addEdge(2,3,7)
graph.addEdge(2,8,2)
graph.addEdge(2,5,4)
graph.addEdge(3,4,9)
graph.addEdge(3,5,14)
graph.addEdge(4,5,10)
graph.addEdge(5,6,2)
graph.addEdge(6,7,1)
graph.addEdge(6,8,6)
graph.addEdge(7,8,7)

graph.DijkstraAlgorithm()




