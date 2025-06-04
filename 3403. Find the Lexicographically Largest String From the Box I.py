class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        from functools import lru_cache

        n = len(word)
        result = []

        @lru_cache(None)
        def dfs(start, k, path):
            if k == 1:
                if start < n:
                    part = word[start:]
                    result.extend(path + [part])
                return
            for i in range(start + 1, n - k + 2):  # ensure enough room for remaining k-1 parts
                dfs(i, k - 1, path + [word[start:i]])

        dfs(0, numFriends, [])

        return max(result)
