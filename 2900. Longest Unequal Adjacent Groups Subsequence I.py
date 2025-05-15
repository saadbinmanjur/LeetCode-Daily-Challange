class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        dp = [[] for _ in range(n)]  # dp[i] stores the best sequence ending at i

        for i in range(n):
            dp[i] = [words[i]]  # start with only current word
            for j in range(i):
                if groups[i] != groups[j] and len(dp[j]) + 1 > len(dp[i]):
                    dp[i] = dp[j] + [words[i]]

        # Find the dp[i] with maximum length
        longest = max(dp, key=len)
        return longest
