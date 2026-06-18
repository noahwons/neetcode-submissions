class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq = {}

        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1
        
        for key in list(freq.keys()):
            heapq.heappush_max(heap, (freq[key], key))
        
        res = []
        while k > 0:
            k -= 1
            res.append(heapq.heappop_max(heap)[1])
        
        return res
