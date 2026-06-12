class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        w1 = defaultdict(int)
        w2 = defaultdict(int)

        for c in s:
            w1[c] += 1
        
        for c in t:
            w2[c] += 1
        
        if w2 == w1:
            return True
        
        return False