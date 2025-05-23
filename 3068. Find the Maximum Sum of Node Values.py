class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        no, yes = 0, -inf
        for n in nums:
            no, yes = max(n + no, (n^k) + yes), max((n^k) + no, n + yes)
        return no