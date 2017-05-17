class Vertex(object):
    class Vertex(object):

        def __init__(self, name):
            self.name = name
            self.neighbours = []
            self.visited = False

        def addNeighbours(self, vertex):
            self.neighbours.append(vertex)

    class Graph(object):

        def __init__(self):
            self.vertices = {}

        def addVertex(self, vertex):
            if isinstance(vertex, Vertex) and vertex not in self.vertices:
                self.vertices[vertex.name] = vertex
                return True
            return False

        def addEdge(self, u, v):
            self.vertices[u].addNeighbours(self.vertices[v])

        def DFS(self, v):
            v.visited = True
            print(v.name)
            for vertex in v.neighbours:
                if not vertex.visited:
                    self.DFS(vertex)

        def TopologicalUtil(self, vertex, sorted):
            if not vertex.visited:
                vertex.visited = True

            for v in vertex.neighbours:
                if not v.visited:
                    self.TopologicalUtil(v, sorted)

            sorted.append(vertex.name)

        def TopologicalSort(self):
            sorted = []
            for key in self.vertices.keys():
                if not self.vertices[key].visited:
                    self.TopologicalUtil(self.vertices[key], sorted)

            print(sorted)

    graph = Graph()
    graph = Graph()
    for i in range(ord("A"), ord("I")):
        graph.addVertex(Vertex(chr(i)))

    edges = ['AC', 'BC', 'BD', 'CE', 'DF', 'EH', 'EF', 'FG', ]
    for edge in edges:
        graph.addEdge(edge[:1], edge[1:])
    graph.TopologicalSort()