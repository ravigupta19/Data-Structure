class Node(object):

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class BST(object):

    def __init__(self):
        self.root = None

    def insert(self,data):
        node = Node(data)
        if self.root is None:
            self.root = node
        else:
            self.insertNode(self.root, node)

    def insertNode(self, root, node):
        if node.data <= root.data:
            if root.left is None:
                root.left = node
            else:
                self.insertNode(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                self.insertNode(root.right, node)

    def traverse(self):
        if self.root:
            self.inOrder(self.root)

    def inOrder(self, root):
        if root is None:
            return
        else:
            self.inOrder(root.left)
            print(root.data)
            self.inOrder(root.right)

    def getMax(self):
        if self.root :
            return self.findMaxValue(self.root)

    def findMaxValue(self,root):
        if root.right is None:
            return self.findMax(root.right)
        return root.data

    def getMin(self):
        if self.root:
            return self.findMaxValue(self.root)

    def findMinValue(self,root):
        if root.left:
            return self.findMin(root.left)
        return root.data

    def delete(self,data):
        if self.root:
            self.root = self.deleteNode(self.root,data)

    def deleteNode(self,root, data):
        if root is None:
            return root
        elif data <= root.data:
            root.left =  self.deleteNode(root.left,data)
        elif data > root.data:
            root.right = self.deleteNode(root.right,data)
        else:

            if root.right is None and root.left is None:
                del root
                return None
            elif root.left is None:
                tempNode = root.right
                del root
                return  tempNode
            elif root.right is None:
                tempNode = root.left
                del root
                return  tempNode
            else:
                tempdata = self.getMin(root.right)
                root.data = data
                self.deleteNode(root.right,tempdata)
                return root

    def getPredecessor(self, root):
        if root.right:
            return self.getPredecessor(root.left)
        return root


