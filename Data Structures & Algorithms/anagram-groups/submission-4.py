class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we know words are anagrams of eachother if they contain the same key
        # act -> {
        #   a: 1
        #   b: 0
        #   c: 1
        #   ...
        #   t: 1
        #   u: 0
        #   ...
        # }
        # in this case, both act and cat have the same key and are thus anagrams
        # We use the result from the convert method as the key for the hashmap
        print(self.getWordHash(strs[0]))
        hashMap = {} # map wordHash to list of words
        for s in strs:
            wordHash = self.getWordHash(s)
            if wordHash in hashMap:
                hashMap[wordHash].append(s)
            else:
                hashMap[wordHash] = [s]
        return list(hashMap.values())
        
    
    def getWordHash(self, s):
        s = s.lower()
        w1 = [0] * 26
        for c in s:
            w1[ord(c) - ord('a')] += 1
        return tuple(w1)

