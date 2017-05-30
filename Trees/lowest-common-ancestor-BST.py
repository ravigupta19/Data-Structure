class Node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def addData(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            self.addUtil(self.root,new_node)

    def addUtil(self, startingNode, node):
        if node.data <= startingNode.data:
            if startingNode.left is None:
                startingNode.left = node
            else:
                self.addUtil(startingNode.left, node)
        else:
            if startingNode.right is None:
                startingNode.right = node
            else:
                self.addUtil(startingNode.right, node)

    def searchkey(self,key, node):
        if node is None:
            return False
        if node.data == key:
            return True
        else:
            if node.data < key:
                self.searchkey(key, node.right)
            else:
                self.searchkey(key, node.left)

    def getMax(self, node):
        if node.right is None:
            return node.data
        else:
            self.getMax(node.right)

    def getMin(self, node):
        if node.left is None:
            return node.data
        else:
            self.getMin(node.left)

    def getLowestCommonAncestor(self,data1,data2, node):
        if node.data > data1 and node.data > data2:
            self.getLowestCommonAncestor(data1, data2, node.left)
        elif node.data < data1 and node.data < data2:
            self.getLowestCommonAncestor(data1, data2, node.right)
        else:
            print(node.data)

    def inOrder(self, node):
        if node is None:
            return
        else:
            self.inOrder(node.left)
            print(node.data)
            self.inOrder(node.right)

BST = BinarySearchTree()
BST.addData(10)
BST.addData(-10)
BST.addData(30)
BST.addData(25)
BST.addData(60)
BST.addData(28)
BST.addData(78)
BST.getLowestCommonAncestor(28,78,BST.root)

