from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        current_sum = 0
        result = 0

        for right in range(n):
            current_sum += nums[right]
            
            # Shrink the window while the score is >= k
            while current_sum * (right - left + 1) >= k:
                current_sum -= nums[left]
                left += 1

            # All subarrays ending at 'right' and starting between 'left' and 'right' are valid
            result += right - left + 1

        return result
