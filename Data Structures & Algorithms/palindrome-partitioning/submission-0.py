class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = [] # store all partitions
        part = [] # store current partition

        # i represents the index of the character we are at
        def dfs(i):
            if i >= len(s):
                # we have a valid partition and no more characters
                # left to add
                # NOTE: make sure you copy and dont pass reference
                res.append(part.copy())
                return
            
            # iterate through every other character in the string
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    # s[i: j + 1] represents current palindrome
                    part.append(s[i:j + 1])
                    dfs(j + 1) # call dfs on next character
                    part.pop()
        
        dfs(0)
        return res
    
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True