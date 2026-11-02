class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()

        for n in nums:
            if n not in s:
                s.add(n)
                continue
            return True
        
        return False