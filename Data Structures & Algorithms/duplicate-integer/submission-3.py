class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        # Time complexity O(n)
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
        return False