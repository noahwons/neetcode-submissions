class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = 0
        i = 0

        while i < len(nums):
            if nums[i] == val:
                # remove the value
                del nums[i]
            else:
                # only increment i if we are not 
                # deleting the current element
                i += 1
        
        # i represents the count
        return i