class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []

        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, v in count.items():
            print(n, v)
            heapq.heappush_max(heap, (v, n))
        
        res = []
        while k > 0:
            res.append(heapq.heappop_max(heap)[1])
            k -= 1
        
        return res