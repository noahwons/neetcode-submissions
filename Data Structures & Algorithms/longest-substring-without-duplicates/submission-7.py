class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q = deque()
        window = set()
        l = 0
        res = 0
        for r in range(0, len(s)):
            while s[r] in window:
                window.remove(q.popleft())
            
            q.append(s[r])
            window.add(s[r])
            
            res = max(res, len(q))
        
        return res
