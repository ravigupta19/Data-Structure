class AVLNode(object):

    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
        self.balance_factor = 0