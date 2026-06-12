class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        res = ""
        for i in range(len(s)):
            cur = s[i]
            if len(cur) > len(res):
                    res = cur
            for j in range(i + 1, len(s)):
                cur += s[j]
                if self.isPalindrome(cur):
                    if len(cur) > len(res):
                        res = cur[::]
        
        return res
        
    
    def isPalindrome(self, s):
        l, r = 0, len(s) - 1

        if len(s) == 1:
            return True

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True
