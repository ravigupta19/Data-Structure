class Node(object):

    def __init__(self, data = None, color = None, parent = None,left = None, right = None):
        self.data = data
        self.parent = parent
        self.color = color
        self.left = left
        self.right = right


class RedBlackTree(object):

    def __init__(self):
        self.root = None

    def createNilNode(self):
        node = Node()
        node.color = "B"
        return node

    def createNode(self,data):
        node = Node()
        node.data = data
        node.color = "R"
        return node

    def leftRotate(self, node):
        pass

    def rightRotate(self, node):
        pass

    def insert(self,data):
        node = self.createNode(data)
        if self.root is None:
            self.root = node
            self.root.color = "B"
            self.root.right = self.createNilNode()
            self.root.left = self.createNilNode()
        else:
            self.root = self.insertNode(self.root, node)

    def insertNode(self,root,node):
        if node.data <= root.data:
            if root.left.data is None:
                root.left = node
                node.parent = root
            else:
                root.left = self.insertNode(root.left,node)
        else:
            if root.right.data is None:
                root.right = node
                node.parent = root
            else:
                root.right = self.insertNode(root.right, node)
        return root

    def inOrderTraversal(self,root):
        if root is None:
            return
        self.inOrderTraversal(root.left)
        print(root.data)
        self.inOrderTraversal(root.right)

    def getUncle(self,root):
        if root =

    def predecessor(self,root):
        pass

    def successor(self,root):
        pass

    def heightOfTree(self,root):
        pass


tree = RedBlackTree()
tree.insert(10)
tree.insert(-10)
tree.insert(20)
tree.inOrderTraversal(tree.root)
