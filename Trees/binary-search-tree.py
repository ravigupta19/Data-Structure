class BinaryNode(object):

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def getRight(self):
        return self.right

    def getLeft(self):
        return  self.left

    def setRight(self, right):
        self.right = right

    def setLeft(self, left):
        self.left = left

class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def getNewNode(self, data):
        new_node = BinaryNode(data)
        return new_node

    def insertNode(self,root,node):
        if root is None:
            self.root = node
        else:
            if node.data <= root.data:
                if root.left is None:
                    root.left = node
                else:
                    self.insertNode(root.left,node)
            elif node.data > root.data:
                if root.right is None:
                    root.right = node
                else:
                    self.insertNode(root.right, node)

    def searchKey(self, root, key):
        if root is None:
            return False
        elif root.data == key:
            return True
        elif key < root.data:
            return self.searchKey(root.left, key)
        elif key > root.data:
            return  self.searchKey(root.right, key)

    def inOrder(self,root):
        if root is None:
            return
        self.inOrder(root.left)
        print(root.data)
        self.inOrder(root.right)

BST = BinarySearchTree()
node = BST.getNewNode(15)
BST.insertNode(BST.root,node)
node = BST.getNewNode(10)
BST.insertNode(BST.root,node)
node = BST.getNewNode(5)
BST.insertNode(BST.root,node)
node = BST.getNewNode(25)
BST.insertNode(BST.root,node)
node = BST.getNewNode(1)
BST.insertNode(BST.root,node)
node = BST.getNewNode(40)
BST.insertNode(BST.root,node)
node = BST.getNewNode(45)
BST.insertNode(BST.root,node)
node = BST.getNewNode(35)
BST.insertNode(BST.root,node)
node = BST.getNewNode(30)
BST.insertNode(BST.root,node)
node = BST.getNewNode(50)
BST.insertNode(BST.root,node)
print(BST.searchKey(BST.root, 50))
BST.inOrder(BST.root)
