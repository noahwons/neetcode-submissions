class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operators = set({'*', '+', '-', '/'})

        for n in tokens:

            if n in operators:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                res = 0

                if n == '*':
                    res = num1 * num2

                if n == '+':
                    res = num1 + num2

                if n == '-':
                    res = num2 - num1
                
                if n == '/':
                    res = num2 / num1

                stack.append(res)
                continue

            stack.append(n)
        
        return int(stack.pop())