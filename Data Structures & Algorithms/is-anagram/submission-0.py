class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict = {}
        my_dict2 = {}
        for c in s:
            if c not in my_dict:
                my_dict[c] = 1
            else:
                my_dict[c] += 1
        
        for c in t:
            if c not in my_dict:
                return False
            elif c not in my_dict2:
                my_dict2[c] = 1
            else:
                my_dict2[c] += 1
    
        return my_dict == my_dict2
            