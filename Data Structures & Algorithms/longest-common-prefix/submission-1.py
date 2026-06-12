class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = strs[0]
        for s in strs:
            i = 0
            # len of s can be smaller than pre.
            # in this case, pre must be set truncated to the same length
            if len(s) < len(pre):
                pre = pre[:len(s)]
                
            while i < len(pre):
                # compare
                if s[i] != pre[i]:
                    pre = pre[:i]
                i += 1

        return pre


