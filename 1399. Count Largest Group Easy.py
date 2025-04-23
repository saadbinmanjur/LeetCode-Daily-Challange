from collections import defaultdict

class Solution:
    def countLargestGroup(self, n: int) -> int:
        def digit_sum(x):
            return sum(int(d) for d in str(x))
        
        group_counts = defaultdict(int)
        
        for i in range(1, n + 1):
            s = digit_sum(i)
            group_counts[s] += 1
        
        max_size = max(group_counts.values())
        return sum(1 for count in group_counts.values() if count == max_size)