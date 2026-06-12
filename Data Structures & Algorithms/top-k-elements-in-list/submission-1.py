class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket sort
        # Most number of times a value can occur is len(s)
        # Count spans from 0 - len(s)
        
        count = {} # Hash map to count occurences
        freq = [[] for i in range(len(nums)+ 1) ] # Index is frequency element appears

        # Count how many times each number occurs
        for n in nums:
            count[n] = 1 + count.get(n, 0) # Default return of 0 if doesnt exist

        for n, c in count.items(): # Returns all key value pairs
            freq[c].append(n) # n occurs c number of times

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        
        
        