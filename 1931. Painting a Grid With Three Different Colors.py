from typing import List
from functools import lru_cache

MOD = 10**9 + 7

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        # Generate all valid column states (no two adjacent cells same color)
        def generate_states(pos=0, prev=-1, state=()):
            if pos == m:
                states.append(state)
                return
            for color in range(3):
                if color != prev:
                    generate_states(pos + 1, color, state + (color,))
        
        states = []
        generate_states()
        
        # Map state tuple to index
        state_to_idx = {state: i for i, state in enumerate(states)}
        
        # Build compatibility graph
        compatible = [[] for _ in range(len(states))]
        for i, s1 in enumerate(states):
            for j, s2 in enumerate(states):
                if all(x != y for x, y in zip(s1, s2)):  # no same row has same color
                    compatible[i].append(j)
        
        # DP: dp[col][state_index]
        dp = [0] * len(states)
        for i in range(len(states)):
            dp[i] = 1  # Initial column

        for _ in range(1, n):
            new_dp = [0] * len(states)
            for i in range(len(states)):
                for j in compatible[i]:
                    new_dp[j] = (new_dp[j] + dp[i]) % MOD
            dp = new_dp

        return sum(dp) % MOD
