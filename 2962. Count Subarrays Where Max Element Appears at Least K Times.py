from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        left = 0
        count = 0  # number of times max_val appears in current window
        result = 0

        for right in range(len(nums)):
            if nums[right] == max_val:
                count += 1
            
            while count >= k:
                if nums[left] == max_val:
                    count -= 1
                left += 1

            # All subarrays ending at right and starting before or at (left - 1) are valid
            result += left

        return result
