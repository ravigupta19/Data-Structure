class Heap(object):

    HEAP_SIZE = 10

    def __init__(self):
        self.heap = [0] * Heap.HEAP_SIZE
        self.currentPosition = -1

    def insert(self, item):
        if self.isFull():
            return
        self.currentPosition += 1
        self.heap[self.currentPosition] = item
        self.fixUp(self.currentPosition)

    def isFull(self):
        return self.currentPosition == Heap.HEAP_SIZE

    def fixUp(self, index):
        parentIndex = (index-1) //2

        while parentIndex >= 0 and self.heap[parentIndex] < self.heap[index]:
            (self.heap[parentIndex],self.heap[index]) = (self.heap[index],self.heap[parentIndex])
            parentIndex = (index - 1) // 2

    def heapSort(self):
        for i in range(0,self.currentPosition+1):
            temp = self.heap[0]
            self.heap[0] = self.heap[self.currentPosition-i]
            self.heap[self.currentPosition-i] = temp
            self.fixDown(0, self.currentPosition-i-1)

    def fixDown(self, index, upto):
        while index <= upto:
            leftChild = 2 * index + 1
            rightChild = 2 * index + 2

            if leftChild < upto:
                swapChild = None

                if rightChild > upto:
                    swapChild = leftChild
                else:
                    if self.heap[leftChild] > self.heap[rightChild]:
                        swapChild = leftChild
                    else:
                        swapChild = rightChild

                if self.heap[index] < self.heap[swapChild]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[swapChild]
                    self.heap[swapChild] = temp
                else:
                    break
                index = swapChild
            else:
                break

heap = Heap()
heap.insert(10)
heap.insert(-20)
heap.insert(0)
heap.insert(2)
heap.heapSort()
print(heap.heap)



