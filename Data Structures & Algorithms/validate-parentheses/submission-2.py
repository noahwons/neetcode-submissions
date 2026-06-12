class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        i = 0
        k = 0 # use k to iterate arr
        while i < len(s):
            if s[i] == ')' or s[i] == '}' or s[i] == ']':
                if len(arr) > 0:
                    if s[i] == ')' and arr[len(arr) - 1] == '(':
                        arr.pop(len(arr) - 1)
                    elif s[i] == '}' and arr[len(arr) - 1] == '{':
                        arr.pop(len(arr) - 1)
                    elif s[i] == ']' and arr[len(arr) - 1] == '[':
                        arr.pop(len(arr) - 1)
                    else:
                        return False
                else:
                    return False
            else:
                arr.append(s[i])
            i += 1
        return len(arr) == 0

