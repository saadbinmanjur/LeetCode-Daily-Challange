class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)

        # Maximize: replace first non-9 digit with 9
        max_val = num
        for d in set(s):
            if d != '9':
                max_candidate = int(s.replace(d, '9'))
                max_val = max(max_val, max_candidate)

        # Minimize: replace first digit with 0 (unless it's already 0)
        min_val = num
        for d in set(s):
            if d != '0':
                min_candidate = int(s.replace(d, '0'))
                min_val = min(min_val, min_candidate)

        return max_val - min_val
