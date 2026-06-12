class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        
        while i < len(s):
            # find delim
            j = i
            while s[j] != "#":
                j+= 1
            length = int(s[i:j]) # gets int before # (i to j not including j)
            res.append(s[j + 1 : j + 1 + length]) # j + 1 is first char, j + 1 + length is end of str
            i = j + 1 + length

        return res
