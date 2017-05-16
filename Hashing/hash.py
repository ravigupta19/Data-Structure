class HashTable(object):

    def __init__(self,size):
        self.size = size
        self.slots = [None] * self.size
