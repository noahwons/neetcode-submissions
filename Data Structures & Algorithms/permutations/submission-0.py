class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # n! total permutations
        # Insertion is n^2 operation (inserting n elements into each permutation)
        # T: O(n!) or O(n! * n^2)
        # S: n! * n
        if len(nums) == 0:
            # base case
            return [[]]
        
        # recursive call excluding first element
        perms = self.permute(nums[1:]) # gets permutations
        res = []

        # add nums[0] to all possible positions
        for p in perms:
            for i in range(len(p) + 1): # + 1 because we can add to end of permutation
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)

        return res