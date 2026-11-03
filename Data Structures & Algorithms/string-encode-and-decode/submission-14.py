class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += (str(len(s)) + '|' + s)
        return res
        
    def decode(self, s: str) -> List[str]:
        l, r = 0, 1
        res = []
        # until r == |, we have our number
        while r < len(s):
            while s[r] != '|':
                r += 1
            # now s[l:r] == number
            strLen = int(s[l:r])
            res.append(s[r + 1: r + strLen + 1])
            l = r + strLen + 1
            r = l + 1
        return res

