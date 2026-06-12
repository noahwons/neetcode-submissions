class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # map each instance of num
        my_map = {}

        for n in nums:
            if n not in my_map:
                my_map[n] = 1
            else:
                my_map[n] += 1
        
        return sorted(my_map, key=my_map.get, reverse=True)[:k]
        