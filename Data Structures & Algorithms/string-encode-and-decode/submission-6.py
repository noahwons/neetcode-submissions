class Solution:

    def encode(self, strs: List[str]) -> str:
        # encode list of strs to one string
        res = ""
        for s in strs:
            # get len of s, create new striung
            cur = str(len(s)) + "|" + s
            res = res + cur
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            numChars = 0
            # finds the delimeter
            while s[j] != "|":
                # gets us the index of the end of the digit.
                j += 1
            numChars = int(s[i:j]) # j is delim, i -> j - 1 is the length
            res.append(s[j+1: j+1+numChars])
            i = numChars + 1 + j

        return res