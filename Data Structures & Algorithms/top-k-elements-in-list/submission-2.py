class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = {}

        # gets number of occurences for each num
        for num in nums:
            if num not in myMap:
                myMap[num] = 1
            else:
                myMap[num] += 1
        
        heap = [(-v, k) for k, v in myMap.items()]
        heapq.heapify(heap)

        res = []
        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        
        return res
        
        