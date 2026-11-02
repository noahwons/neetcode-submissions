class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        w1, w2 = defaultdict(int), defaultdict(int)

        for c in s:
            w1[c] += 1
        
        for c in t:
            w2[c] += 1
        
        return w1 == w2

