class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        r, c = len(text1), len(text2)

        dp = [[0] * (c+1) for _ in range(r+1)]


        for x in reversed(range(r)):
            for y in reversed(range(c)):
                if text1[x] == text2[y]:
                    dp[x][y] = 1 + dp[x+1][y+1]
                else:
                    dp[x][y] = max(dp[x+1][y], dp[x][y+1])

        return dp[0][0]
