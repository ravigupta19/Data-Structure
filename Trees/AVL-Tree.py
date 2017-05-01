class AVLNode(object):

    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
        self.height = 0

class AVLTree(object):

    def __init__(self):
        self.root = None

    def calHeight(self, root):
        if root is None:
            return -1
        return root.height

    def calcBalance(self, root):
        if root is None:
            return 0
        return self.calHeight(root.left) - self.calHeight(root.right)

    def rightRotation(self, root):
        print("Rotating to the right " + str(root.data))
        templeft = root.left
        t = templeft.right
        templeft.right = root
        root.left = t
        root.height = max(self.calHeight(root.left), self.calHeight(root.left)) +1
        templeft.height = max(self.calHeight(templeft.left), self.calHeight(templeft.left)) +1
        return templeft

    def leftRotation(self, root):
        print("Rotating to the left " + str(root.data))
        tempright = root.right
        t = tempright.left
        tempright.left = root
        root.right = t
        root.height = max(self.calHeight(root.left), self.calHeight(root.left)) +1
        tempright.height = max(self.calHeight(tempright.left), self.calHeight(tempright.left)) +1
        return tempright

    def insert(self, data):
        self.root = self.insertNode(self.root, data)

    def insertNode(self,root, data):
        if root is None:
            return AVLNode(data)
        if data <= root.data:
            root.left = self.insertNode(root.left, data)
        elif data > root.data:
            root.right = self.insertNode(root.right, data)

        root.height = max(self.calHeight(root.left), self.calHeight(root.right)) + 1

        return self.settleBalance(root, data)

    def settleBalance(self, root, data):
        balance = self.calcBalance(root)
        #Case 1 tree is heavily left unbalanced
        if balance > 1 and data < root.left.data:
           return self.rightRotation(root)

        if balance < -1 and data > root.right.data:
            return self.leftRotation(root)

        if balance > 1 and data > root.left.data:
            root.left = self.leftRotation(root.left)
            return self.rightRotation(root)

        if balance < -1 and data < root.right.data:
            root.right = self.rightRotation(root.right)
            return self.leftRotation(root)

        return root


    def inOrder(self, root):
        if root is None:
            return
        else:
            self.inOrder(root.left)
            print(root.data)
            self.inOrder(root.right)

tree = AVLTree()
tree.insert(21)
tree.insert(26)
tree.insert(30)
tree.insert(9)
tree.insert(4)
tree.insert(14)
tree.insert(28)
tree.insert(18)
tree.insert(15)
tree.insert(10)
tree.insert(2)
tree.insert(3)
tree.insert(7)
tree.inOrder(tree.root)