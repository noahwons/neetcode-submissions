class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use hashmap to store value and smallest index
        # this is done by determining if the value already in map
        myMap = {}
            
        for i in range(len(nums)):
            curDiff = target - nums[i]
            # determine if in map
            if curDiff in myMap:
                return [myMap[curDiff], i]
                
            myMap[nums[i]] = i
            
        return []
