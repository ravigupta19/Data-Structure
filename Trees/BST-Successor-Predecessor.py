class Node(object):

    def __init__(self,data):
        self.key = data
        self.right = None
        self.left = None
        self.parent = None


class BST(object):

    def __init__(self):
        self.root = None

    def insert(self,data):
        node = Node(data)
        if self.root is None:
            self.root = node
            self.root.parent = self.root
        else:
            self.insertNode(self.root,node)

    def insertNode(self, root, node):
        if node.key <= root.key:
            if root.left is None:
                root.left = node
                node.parent = root
            else:
                self.insertNode(root.left, node)
        else:
            if root.right is None:
                root.right = node
                node.parent = root
            else:
                self.insertNode(root.right, node)

    def getMinTree(self):
        if self.root is None:
            return self.root
        else:
            return self.getMin(self.root)


    def getMin(self, root):
        if root.left is not None:
            return self.getMin(root.left)
        return root

    def getMaxTree(self):
        if self.root is None:
            return self.root
        else:
            return self.getMax(self.root)

    def getMax(self, root):
        if root.right:
            return self.getMax(root.right)
        return root

    def successor(self, root):
        if root.right:
            return self.getMin(root.right)
        y = root.parent
        while y is not None and root == y.right:
            root = y
            y = y.parent
        return y

    def predecessor(self, root):
        if root.left:
            return self.getMax(root.left)
        y = root.parent
        while y is not None and root == y.left:
            root = y
            y = y.parent
        return y


    def delete(self, data):
        if self.root:
            self.root = self.removeNode(self.root, data)

    def removeNode(self, root, data):
        if root is None:
            return root
        elif data < root.key:
            root.left = self.removeNode(root.left, data)
        elif data > root.key:
            root. right = self.removeNode(root.right, data)
        else:
            if root.right is None and root.left is None:
                del root
                return None
            elif root.right is None:
                tempNode = root.left
                del root
                return tempNode
            elif root.left is None:
                tempNode = root.right
                del root
                return tempNode
            else:
                tempNode = self.successor(root)
                root.key = tempNode.key
                root.right = self.removeNode(root.right,tempNode.key)
        return root

    def traverse(self):
        if self.root is not None:
            self.traverseInOrder(self.root)

    def traverseInOrder(self, root):
        if root is None:
            return
        else:
            self.traverseInOrder(root.left)
            print(root.key)
            self.traverseInOrder(root.right)

    def heightOfTree(self, root):
        if root is None:
            return -1
        return max(self.heightOfTree(root.left), self.heightOfTree(root.right)) + 1

tree = BST()
tree.insert(15)
tree.insert(6)
tree.insert(18)
tree.insert(3)
tree.insert(7)
tree.insert(17)
tree.insert(20)
tree.insert(2)
tree.insert(4)
tree.insert(13)

#tree.insert(9)
#print(tree.root.key)
tree.traverse()
#node = tree.successor()
#print(node.key)
tree.delete(6)
print('-----------')
print('')
tree.traverse()
node = tree.predecessor(tree.root)
print(node.key)
#for _ in range(int(input())):
#    user_oper = list(map(int,input().split()))
#    if user_oper[0] == 1: # insert new node in tree
#        tree.insert(int(user_oper[1]))
#    elif user_oper[0] == 2: # delete node in tree
#        tree.delete()
#    elif user_oper[0] == 3: # get the Min of Tree
#        tree.getMinTree()
#    elif user_oper[0] == 4: #get the Max of Tree
#        tree.getMaxTree()
#    elif user_oper[0] == 5: #get the Successor of tree
#        tree.successor(tree.root)
#    elif user_oper[0] == 6:
#        node = tree.successor(tree.root)
#        print(node.data)
#    elif user_oper[0] == 7:
#        tree.traverse()



