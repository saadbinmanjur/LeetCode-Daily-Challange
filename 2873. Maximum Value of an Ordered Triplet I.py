from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_val = 0
        
        # Prefix max array to store max value of nums[i] seen so far
        prefix_max = [0] * n
        prefix_max[0] = nums[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], nums[i])
        
        # Suffix max array to store max value of nums[k] seen from the end
        suffix_max = [0] * n
        suffix_max[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], nums[i])
        
        # Iterate over the middle element (nums[j]) to find the max triplet value
        for j in range(1, n - 1):
            if prefix_max[j - 1] > nums[j]:  # Ensure (nums[i] - nums[j]) is positive
                max_val = max(max_val, (prefix_max[j - 1] - nums[j]) * suffix_max[j + 1])
        
        return max_val