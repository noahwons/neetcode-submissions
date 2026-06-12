class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Clean s

        # Remove , . ? !
        s = s.lower()
        exp = [",", ".", "?", "!", "'", ":"]
        for e in exp:
            if e in s:
                s = s.replace(e, "")
        s = s.replace(" ", "")


        ptr1 = 0
        ptr2 = len(s) - 1
        while ptr1 < ptr2:

            if (s[ptr1] != s[ptr2]):
                return False

            ptr1 += 1
            ptr2 -= 1
        
        return True