class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []
        for i, op in enumerate(operations):
            if op == "+" and i > 1:
                s.append(s[-1] + s[-2])
            elif op == "C":
                s.pop()
            elif op == "D":
                s.append(s[-1] * 2)
            else:
                s.append(int(op))
        
        res = 0
        for op in s:
            res += op
        
        return res
