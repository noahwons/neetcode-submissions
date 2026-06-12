class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # map char count to list of anagrams

        for s in strs:
            count = [0] * 26 # a ... z
            for c in s:
                # ord() gets the ascii value of the character
                # we subtract them to set bounds of chars from
                # 0 - 25
                count[ord(c) - ord("a")] += 1
            
            res[tuple(count)].append(s)
        
        return list(res.values())