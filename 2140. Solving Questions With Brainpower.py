from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)  # DP array to store maximum points
        
        for i in range(n - 1, -1, -1):  # Iterate from last to first question
            points, brainpower = questions[i]
            next_index = i + brainpower + 1  # The next available question after solving this one
            
            # If next_index is within bounds, add its DP value, otherwise just take current points
            solve = points + (dp[next_index] if next_index < n else 0)
            skip = dp[i + 1]  # Skipping this question
            
            dp[i] = max(solve, skip)  # Choose the optimal action
        
        return dp[0]