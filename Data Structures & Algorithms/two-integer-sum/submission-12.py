class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # i + j = T
        # j - T = i

        # the idea: use hashmap to store our current difference

        hashMap = {}
        # 3,4,5,6 T = 7
        
        for i in range(len(nums)):
            if target - nums[i] in hashMap:
                return [hashMap[target - nums[i]], i]
            hashMap[nums[i]] = i