class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        que = []
        for i in range(len(tokens)):
            if tokens[i].lstrip("-").isdigit():
                que.append(int(tokens[i]))
            else:
                if tokens[i] == "+":
                    total = que[-1] + que[-2]
                    que.pop()
                    que.pop()
                    que.append(total)
                elif tokens[i] == "-":
                    total = que[-2] - que[-1]
                    que.pop()
                    que.pop()
                    que.append(total)
                elif tokens[i] == "*":
                    total = que[-1] * que[-2]
                    que.pop()
                    que.pop()
                    que.append(total)
                elif tokens[i] == "/":
                    total = int(que[-2] / que[-1])
                    que.pop()
                    que.pop()
                    que.append(total)
        return que[-1]
            