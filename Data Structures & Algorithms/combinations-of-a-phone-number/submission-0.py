class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res, sol = [], ""
        LENGTH = len(digits)

        if LENGTH < 1:
            return []

        def backtrack(i, sol):
            # base case #1
            if i == LENGTH:
                # we have a combo
                res.append(sol)
                return
            
            # We need to know what position we are in in current digits
            curChars = self.getCharacters(digits[i])

            for ch in curChars:
                backtrack(i + 1, sol + ch)





        
        backtrack(0, sol)
        return res
            

    def getCharacters(self, digit):
        if digit == '2':
            return 'abc'
        elif digit == '3':
            return 'def'
        elif digit == '4':
            return 'ghi'
        elif digit == '5':
            return 'jkl'
        elif digit == '6':
            return 'mno'
        elif digit == '7':
            return 'pqrs'
        elif digit == '8':
            return 'tuv'
        elif digit =='9':
            return 'wxyz'