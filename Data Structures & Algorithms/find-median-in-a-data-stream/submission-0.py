class MedianFinder:

    def __init__(self):
        # two heaps, Large Heap (minHeap), Small Heap (maxHeap)
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # add to small heap by default
        heapq.heappush(self.small, -1 * num)

        # ensure all elements in small are <= every element in large
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            # when this condition is true, there is a value in the small heap
            # that is larger than a value in the large heap

            # pop from small heap and add to large heap
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # handle uneven size
        if len(self.small) > len(self.large) + 1:
            # pop from small, push to learge
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # difference is 2 or greater
        if len(self.large) > len(self.small) + 1:
            # opposite opperation
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        # Case: odd length
        if len(self.small) > len(self.large):
            # odd total elements, small has more
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            # odd total elements, large has more
            return self.large[0]
        
        # median operation for even elements
        return (-1 * self.small[0] + self.large[0]) / 2
        
        