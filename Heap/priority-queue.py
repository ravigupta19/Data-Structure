import heapq
INF = 100000
class PriorityQueueMap(object):
    def __init__(self):
        self.eq = []
        self.entry_finder = {}

    def add(self, key, prioprity=INF):
        if key in self.entry_finder:
            raise KeyError("Key already exists")
        self.entry_finder[key] = prioprity
        heapq.heappush(self.eq, [prioprity, key])

    def delete(self, task):
        if not task in self.entry_finder:
            raise KeyError("Key doesnt exist")
        self.entry_finder.pop(task)

    def getMin(self):
        minVertex = heapq.heappop(self.eq)[1]
        self.entry_finder.pop(minVertex)
        return minVertex

    def descrease(self, key, priority):
        previousPriority = self.entry_finder[key]
        self.entry_finder[key] = priority
        index = self.eq.index([previousPriority, key])
        del self.eq[index]
        heapq.heappush(self.eq, [priority, key])


