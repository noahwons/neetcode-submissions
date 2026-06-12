class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a default dict where if the key does not
        # exist, map that key to an empty list
        groups = defaultdict(list)

        # this way, we can iterate through the array and append
        for s in strs:
            # example of sorted:
            # sorted("eat")  # ['a', 'e', 't']
            # note that an array of chars is created. To deal with this,
            # we have to join the chars
            key = "".join(sorted(s))
            groups[key].append(s)
    
        return list(groups.values())