class BinaryTreeNode(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def setLeft(self,left):
        self.left = left

    def setRight(self,right):
        self.right = right

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getData(self):
        return self.data


class BinaryTree(object):

    def __init__(self):
        self.root = None

    def getNewNode(self,data):
        new_node = BinaryTreeNode(data)
        return new_node

    def InsertNode(self, root, node):
        if root is None:
            self.root = node
        else:
            if root.data > node.data:
                if root.left is None:
                    root.left = node
                else:
                    self.InsertNode(root.left, node)
            elif root.data < node.data:
                if root.right is None:
                    root.right = node
                else:
                    self.InsertNode(root.right, node)

    def SearchNode(self,root, key):
        if root is None:
            return False
        elif root.data == key:
            return True
        elif key < root.data:
            return self.SearchNode(root.left, key)
        elif key > root.data:
            return self.SearchNode(root.right, key)

    def getMin(self,root):
        if root.left is None:
            return root.data
        else:
            return self.getMin(root.left)

    def getMax(self,root):
        if root.right is None:
            return root.data
        else:
            return self.getMax(root.right)

    def FindHeight(self, root):
        if root is None:
            return -1
        return max(self.FindHeight(root.left), self.FindHeight(root.right)) + 1

    def leveorder(self):
        if self.root is None:
            return
        else:
            l = []
            l.append(self.root)
            while len(l) != 0:
                node = l.pop(0)
                print(node.data)
                if node.left is not None:
                    l.append(node.left)
                if node.right is not None:
                    l.append(node.right)

    def preorder(self,root):
        if root is None:
            return
        print(root.data)
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)

    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data)



BT  = BinaryTree()
node = BT.getNewNode(15)
BT.InsertNode(BT.root,node)
node = BT.getNewNode(20)
BT.InsertNode(BT.root,node)
node = BT.getNewNode(30)
BT.InsertNode(BT.root,node)
node = BT.getNewNode(5)
BT.InsertNode(BT.root,node)
node = BT.getNewNode(10)
BT.InsertNode(BT.root,node)
node = BT.getNewNode(25)
BT.InsertNode(BT.root,node)
node = BT.getNewNode(28)
BT.InsertNode(BT.root,node)
node = BT.getNewNode(45)
BT.InsertNode(BT.root,node)
#print(BT.getMin(BT.root))
#print(BT.getMax(BT.root))
#print(BT.SearchNode(BT.root,45))
#print(BT.FindHeight(BT.root))
#BT.leveorder()
BT.preorder(BT.root)
BT.inorder(BT.root)
BT.postorder(BT.root)