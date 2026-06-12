class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        # O(n) operation
        for x, y in points:
            # compute distance for each points
            dist = x**2 + y**2

            # append distance and coordinates
            minHeap.append([dist, x, y])
        
        # convert list to minheap
        heapq.heapify(minHeap)
        res = []

        # pop from minHeap k times
        while k > 0:
            # get values with unpacking
            dist, x, y = heapq.heappop(minHeap)

            # append coordinates
            res.append([x, y])

            # decrement k
            k -= 1
        
        return res