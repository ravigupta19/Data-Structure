class Vertex(object):

    def __init__(self, data):
        self.data = data
        self.neighbours = []
        self.visited = False

    def addNeighbours(self, v):
        self.neighbours.append(v)
        self.neighbours.sort()

class Graph(object):

    def __init__(self):
        self.vertices = {}

    def addVertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex not in self.vertices:
            self.vertices[vertex.data] = vertex
            return True
        return False

    def addEdge(self,v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].addNeighbours(v2)
            self.vertices[v2].addNeighbours(v1)
            return True
        return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + " -> "+str(self.vertices[key].neighbours))

graph = Graph()
for i in range(ord("A"), ord("K")):
    graph.addVertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
    graph.addEdge(edge[:1],edge[1:])
graph.print_graph()