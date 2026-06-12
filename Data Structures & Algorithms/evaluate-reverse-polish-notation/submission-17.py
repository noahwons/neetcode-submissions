class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # use a stack to store values
        s = [int(tokens[0])]
        operations = {'+', '-', '*', '/'}

        for i in range(1, len(tokens)):
            t = tokens[i]
            if t in operations:
                o1 = int(s.pop())
                o2 = int(s.pop())
                res = 0
                if t == '+':
                    res = o2 + o1
                elif t == '-':
                    res = o2 - o1
                elif t == '*':
                    res = o2 * o1
                else:
                    res = int(o2 / o1)
                    print(res)

                s.append(res)

            else:
                s.append(t)
        
        return s.pop()