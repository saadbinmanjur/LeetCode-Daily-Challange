from math import comb
MOD = 10**9 + 7

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        from collections import defaultdict
        
        # dp[k][x]: number of valid sequences of length k ending in x
        max_len = 14  # since 2^14 > 10000
        dp = [defaultdict(int) for _ in range(max_len+1)]
        
        for x in range(1, maxValue+1):
            dp[1][x] = 1  # base case: sequences of length 1
        
        for k in range(1, max_len):
            for x in dp[k]:
                for multiple in range(x*2, maxValue+1, x):
                    dp[k+1][multiple] = (dp[k+1][multiple] + dp[k][x]) % MOD
        
        # Precompute factorials for combinations
        factorial = [1] * (n+1)
        for i in range(1, n+1):
            factorial[i] = factorial[i-1] * i % MOD
        
        inv = [1] * (n+1)
        inv[n] = pow(factorial[n], MOD-2, MOD)
        for i in range(n-1, -1, -1):
            inv[i] = inv[i+1] * (i+1) % MOD
        
        def comb_mod(a, b):
            if b < 0 or b > a:
                return 0
            return factorial[a] * inv[b] % MOD * inv[a - b] % MOD
        
        result = 0
        for k in range(1, max_len+1):
            c = comb_mod(n-1, k-1)
            for x in dp[k]:
                result = (result + dp[k][x] * c) % MOD
        
        return result
