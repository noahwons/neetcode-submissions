class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch.lower() for ch in s if ch.isalnum())


        if len(s) % 2 != 0:
            l = r = len(s) // 2
        else:
            mid = len(s) // 2
            l, r = mid - 1, mid

        while l >= 0 and r < len(s):
            if s[r] != s[l]:
                return False
            l -= 1
            r += 1 
        
        return True