class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countT, window = {}, {}

        for c in t:
            # if c does not exist, get will return 0
            countT[c] = 1 + countT.get(c, 0)
        
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float('inf')
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                # if the count is exactly equal, we can update our have count
                have += 1
            
            # does have equal need exactly?
            while have == need:
                # update result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)

                # pop from left of window
                window[s[l]] -= 1

                # since we removed a char, it is possible our have is not equal to met
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    # if by removing a char and we made it less than we need it to be
                    have -= 1
                
                l += 1
        
        l, r = res

        return s[l:r+1] if resLen != float('inf') else ""



