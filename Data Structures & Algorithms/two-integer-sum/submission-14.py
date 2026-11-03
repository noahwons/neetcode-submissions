class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # if nums[j] == target - nums[i] return i, j

        hashMap = {} # value -> index

        for i in range(len(nums)):
            if target - nums[i] in hashMap:
                return [hashMap[target - nums[i]], i]
            
            # otherwise, map value to index
            hashMap[nums[i]] = i
        
