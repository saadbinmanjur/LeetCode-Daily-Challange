class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (max(n + 1, 4))  # ensure length at least 4 to handle base cases
        dp[0], dp[1], dp[2] = 1, 1, 2

        for i in range(3, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2] + 2 * sum(dp[0:i - 3 + 1])) % MOD
        
        return dp[n]
