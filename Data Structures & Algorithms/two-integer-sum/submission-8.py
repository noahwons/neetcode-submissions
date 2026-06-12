class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use hashmap to store value and smallest index
        # this is done by determining if the value already in map
        myMap = {}

        for i in range(len(nums)):
            if nums[i] not in myMap:
                myMap[nums[i]] = [i]
            else:
                myMap[nums[i]].append(i)
            # allows me to pop the end
            
        for i in range(len(nums)):
            curDiff = target - nums[i]
            if curDiff in myMap and i != myMap[curDiff][-1]:
                return [i, myMap[curDiff].pop()]
            
        return []
