class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        indexed = [(-val, idx) for idx, val in enumerate(nums)]
        indexed.sort()
        chosen = sorted(indexed[:k], key=lambda x: x[1])
        return [nums[idx] for _, idx in chosen]