class Graph:

    def __init__(self, n):
        self.noOfVertex = n
        self.matrix = [[0 for _ in range(n)] for _ in range(n)]

    def addEdge(self, u,v):
        self.matrix[u-1][v-1] = 1
        self.matrix[v-1][u-1] = 1


    def dfs(self):
        pass

graph = Graph(6)
graph.addEdge(1,2)
graph.addEdge(1,3)
graph.addEdge(2,4)
graph.addEdge(4,5)
graph.addEdge(2,3)
graph.addEdge(6,1)
graph.addEdge(6,2)
print(graph.matrix)