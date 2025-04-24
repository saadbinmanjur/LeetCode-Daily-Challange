from collections import defaultdict

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total_distinct = len(set(nums))
        n = len(nums)
        count = 0

        for left in range(n):
            freq = defaultdict(int)
            distinct = 0
            for right in range(left, n):
                if freq[nums[right]] == 0:
                    distinct += 1
                freq[nums[right]] += 1

                if distinct == total_distinct:
                    count += 1

        return count
