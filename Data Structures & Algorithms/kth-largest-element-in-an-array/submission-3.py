class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = [-n for n in nums]
        heapq.heapify(minHeap)

        while k > 1:
            heapq.heappop(minHeap)
            k -= 1
        
        return -1 * minHeap[0]