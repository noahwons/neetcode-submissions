class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # +1 to account for extra row and col of 0s (out of bounds)
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        # starting at bottom right of matrix
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        
        # O(m * n)
        return dp[0][0]