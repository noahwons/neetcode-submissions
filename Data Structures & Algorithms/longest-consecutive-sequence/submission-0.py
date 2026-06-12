class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) # convert nums to set
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet: # indicates start of sequence
                length = 0
                while (n + length) in numSet:
                    length += 1
                # update longest with max val
                longest = max(length, longest)
        
        return longest