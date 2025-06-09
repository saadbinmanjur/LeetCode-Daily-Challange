class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_prefix(prefix, n):
            count = 0
            curr = prefix
            next_prefix = prefix + 1
            while curr <= n:
                count += min(n + 1, next_prefix) - curr
                curr *= 10
                next_prefix *= 10
            return count
        
        curr = 1
        k -= 1  # Because we start from 1

        while k > 0:
            steps = count_prefix(curr, n)
            if steps <= k:
                # Skip this whole prefix tree
                curr += 1
                k -= steps
            else:
                # Go deeper into the tree
                curr *= 10
                k -= 1
        return curr
