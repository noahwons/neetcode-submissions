class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # determine if s and t are valid anagram

        w1 = {}
        w2 = {}

        # O(n)
        for c in s:
            if c not in w1:
                w1[c] = 1
            else:
                w1[c] += 1
        
        # O(m)
        for c in t:
            if c not in w1:
                return False
            elif c not in w2:
                w2[c] = 1
            else:
                w2[c] += 1
        
        # O(n + m)
        if len(w1.keys()) != len(w2.keys()):
            return False

        for k in w1.keys():
            if w2[k] != w1[k]:
                return False
        
        return True
            