class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Worst case O(nlogn), turn into heap in O(n) time
        # we have to pop until we only have k elements
        # this operation is potentially n-k, so we have
        # O((n-k)logn) time or O(nlogn)

        # create minHeap with k largest ints
        self.minHeap, self.k = nums, k
        
        # turn minHeap into heap
        heapq.heapify(self.minHeap)
        
        # remove extra elements
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        

    def add(self, val: int) -> int:
        # O(logn) operation
        # add val to minheap regardless
        heapq.heappush(self.minHeap, val)
        
        # EDGE CASE: Heap may be initialized with less than
        # k elements. Then we should not be popping from the heap
        if len(self.minHeap) > self.k:
            # pop smallest, could be input val or different
            heapq.heappop(self.minHeap)

        return self.minHeap[0] # 0th index represents the root
