class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for w in strs:
            length = len(w)
            res += str(length) + '|' + w
        return res

    def decode(self, s: str) -> List[str]:
        out = []
        i = 0
        strLen = len(s)

        while i < strLen:
            j = i
            while s[j] != '|':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            out.append(s[i:j])
            i = j

        return out