class Solution:
    def isValid(self, s: str) -> bool:
        opening = {'{', '[', '('}
        closing = {'}', ']', ')'}

        # s = '([{}])'
        # stack [(, [, {
        stack = []
        for c in s:
            if c in opening:
                stack.append(c)
            elif c in closing:
                if not stack:
                    return False
                top = stack.pop()
                if c == '}' and top != '{':
                    return False
                elif c == ']' and top != '[':
                    return False
                elif c == ')' and top != '(':
                    return False
        
        return True if len(stack) == 0 else False