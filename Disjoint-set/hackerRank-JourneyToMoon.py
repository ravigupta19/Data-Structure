class Node(object):

    def __init__(self,name):
        self.name = name
        self.parent = None
        self.size = 1

    def setParent(self, parent):
        self.parent = parent

    def getParent(self):
        return  self.parent

