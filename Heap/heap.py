class Heap(object):

    def __init__(self):
        self.arr = []
        self.heap_size = 0

    def build_max_heap(self):
        length = (len(self.arr) // 2)
        while length > 0:
            self.max_heapify(length)
            length -= 1


    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        largest = self.arr[i]
        if l > largest:
            largest = l
        if r > largest:
            largest = r
        l_index = self.arr.index(largest)
        if l_index != i:
            (self.arr[i],self.arr[l_index]) = (self.arr[l_index],self.arr[i])
            self.max_heapify(l_index)

    def min_heapify(self,i):
        l = self.left(i)
        r = self.right(i)
        smallest = self.arr[i]
        if self.arr.index(l) <= self.heap_size and l < smallest:
            smallest = l
        if self.arr.index(r) <= self.heap_size < smallest:
            smallest = r
        l_index = self.arr.index(smallest)
        if l_index != i:
            self.arr[i],self.arr[l_index] = self.arr[l_index],self.arr[i]
            self.min_heapify(l_index)

    def right(self,i):
        if i == 0:
            return self.arr[1]
        try:
            return self.arr[2*i]
        except IndexError:
            return 0

    def left(self,i):
        if i == 0:
            return self.arr[2]
        try:
            return self.arr[2*i + 1]
        except IndexError:
            return 0

    def setArr(self,arr):
        self.arr = arr
        self.heap_size = len(self.arr)

    def HeapSort(self):
        l = []
        self.build_max_heap()
        length = len(self.arr)
        for i in range(length-1, 2,-1):
            self.arr[i],self.arr[1] = self.arr[1],self.arr[i]
            l.append(self.arr.pop())
            self.heap_size -= 1
            self.max_heapify(1)
        l.extend(self.arr[1:])
        self.arr = l[::-1]


heap = Heap()
heap.setArr([0,4,1,3,2,16,9,10,14,8,7])
heap.HeapSort()
print(heap.arr)