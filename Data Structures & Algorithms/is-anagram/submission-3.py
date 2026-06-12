class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        w1 = {}
        w2 = {}

        for i in range(len(s)):
            if s[i] not in w1:
                w1[s[i]] = 1
            else:
                w1[s[i]] += 1
            
        for j in range(len(t)):
            if t[j] not in w2:
                w2[t[j]] = 1
            else:
                w2[t[j]] += 1
        
        return w1 == w2