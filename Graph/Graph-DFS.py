class Vertex(object):

    def __init__(self, name):
        self.name = name
        self.neighbours = []
        self.visited = False

    def addNeighbours(self, vertex):
        self.neighbours.append(vertex)

class Graph(object):

    def __init__(self, n):
        self.vertices = {}
        self.noOfVertices = n

    def addVertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        return False

    def addEdge(self,u,v):
        self.vertices[u].addNeighbours(self.vertices[v])

    def DFS(self,v):
        v.visited = True
        print(v.name)
        for vertex in v.neighbours:
            if not vertex.visited:
                self.DFS(vertex)

    def TopologicalSort(self):

        visited = []
        sorted = []

        for key in self.vertices:
            if


graph = Graph()
graph = Graph()
for i in range(ord("A"), ord("K")):
    graph.addVertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
    graph.addEdge(edge[:1],edge[1:])
graph.DFS(graph.vertices["A"])