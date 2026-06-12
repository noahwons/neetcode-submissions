class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []

        for i in range(len(nums)):
            if i == 0:
                prefix.append(nums[i])
            else:
                prefix.append(nums[i] * prefix[i - 1])
        
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                postfix.append(nums[i])
            else:
                postfix.append(postfix[-1] * nums[i])

        postfix.reverse()
        
        # to generate the output, we multiply the postfix at i + 1 and prefix at i  1'
        print(postfix)
        print(prefix)
        out = []
        for i in range(len(nums)):
            if i == 0:
                out.append(postfix[i + 1])
            elif i == len(nums) - 1:
                out.append(prefix[i - 1])
            else:
                out.append(prefix[i - 1] * postfix[i + 1])
        
        return out