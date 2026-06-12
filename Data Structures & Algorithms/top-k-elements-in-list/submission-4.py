class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
        
        heap = []
        for key, val in count.items():
            heapq.heappush(heap, (-val, key))
        
        print(heap)

        res = []
        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        
        return res