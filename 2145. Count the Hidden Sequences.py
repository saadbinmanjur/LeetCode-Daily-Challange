class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min_prefix = 0
        max_prefix = 0
        curr = 0
        
        for diff in differences:
            curr += diff
            min_prefix = min(min_prefix, curr)
            max_prefix = max(max_prefix, curr)
        
        min_start = lower - min_prefix
        max_start = upper - max_prefix
        return max(0, max_start - min_start + 1)