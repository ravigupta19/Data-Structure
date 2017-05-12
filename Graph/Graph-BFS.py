class Node(object):

    def __init__(self, name):
        self.name = name
        self.neighbours = []
        self.visited = False

    def addNeighbours(self,node):
        self.neighbours.append(node)


class BreadthFirstSearch(object):


    def bfs(self,startNode):

        queue = []
        queue.append(startNode)
        startNode.visited = True
        while queue:
            actualNode = queue.pop(0)
            print(actualNode.name)

            for n in actualNode.neighbours:
                if not n.visited:
                    n.visited = True
                    queue.append(n)

node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")

node1.addNeighbours(node2)
node1.addNeighbours(node3)
node1.addNeighbours(node4)
node2.addNeighbours(node1)
node3.addNeighbours(node1)
node3.addNeighbours(node4)
node4.addNeighbours(node1)
node4.addNeighbours(node3)
node4.addNeighbours(node5)
node5.addNeighbours(node4)

bfs = BreadthFirstSearch()
bfs.bfs(node1)



