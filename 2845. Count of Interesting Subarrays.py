from collections import defaultdict
from typing import List

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        count = 0
        prefix = 0
        freq = defaultdict(int)
        freq[0] = 1  # to handle when prefix % modulo == k directly
        
        for num in nums:
            if num % modulo == k:
                prefix += 1
            # target value we're looking for in the map
            target = (prefix - k) % modulo
            count += freq[target]
            freq[prefix % modulo] += 1
        
        return count
