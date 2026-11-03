class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we're gonna use a minheap organized by num occurences

        hashMap = defaultdict(int)

        for n in nums:
            hashMap[n] += 1
        maxHeap = []
        for key, v in hashMap.items():
            heapq.heappush_max(maxHeap, (v, key))

        # return top k most frequent
        res = []
        while k > 0:
            res.append(heapq.heappop_max(maxHeap)[1])
            k -= 1
        
        return res
