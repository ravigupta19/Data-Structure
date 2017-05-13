class Node(object):

    def __init__(self,name):
        self.name = name
        self.adjacentList = []
        self.visited = False

    def addNeighbours(self, node):
        self.adjacentList.append(node)


class DepthFirstSearch(object):

    def dfs(self,node):

        node.visited = True
        print(node.name)
        for n in node.adjacentList:
            if not n.visited:
                self.dfs(n)


node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")
node7 = Node("G")
node8 = Node("H")


node1.addNeighbours(node2)
node1.addNeighbours(node6)
node1.addNeighbours(node7)
node2.addNeighbours(node1)
node2.addNeighbours(node3)
node2.addNeighbours(node4)
node3.addNeighbours(node2)
node4.addNeighbours(node5)
node4.addNeighbours(node2)
node5.addNeighbours(node4)
node6.addNeighbours(node1)
node7.addNeighbours(node1)
node7.addNeighbours(node8)
node8.addNeighbours(node7)

dfs = DepthFirstSearch()
dfs.dfs(node1)


