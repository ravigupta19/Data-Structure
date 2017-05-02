class Heap(object):

    def __init__(self):
        self.heap = []
        self.size = 0



    def build_max_heap(self, arr):
        self.size = len(arr)
        self.heap = arr
        for i in range(self.size//2, -1,-1):
            print(i)
            self.max_heapify(i)

    def swap(self,i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def max_heapify(self, index):
        left = 2 * index + 1
        right = 2 * index +2
        largest = index
        if left < self.size and self.heap[largest] < self.heap[left]:
            largest = left
        if right < self.size and self.heap[largest] < self.heap[right]:
            largest = right

        if largest != index:
            self.swap(index,largest)
            self.max_heapify(largest)


    def heapSort(self, array):
        self.build_max_heap(array)
        for i in range(self.size-1,0,-1):
            self.swap(i,0)
            self.size -= 1
            self.max_heapify(0)


heap = Heap()
heap.heapSort([3,4,9,7,8,2,5,6,1])
print(heap.heap)