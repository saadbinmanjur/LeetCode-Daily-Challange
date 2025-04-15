from typing import List

class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 2)
        self.size = size + 2

    def update(self, i, delta):
        i += 1
        while i < self.size:
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        i += 1
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        pos_in_nums2 = [0] * n
        for i, val in enumerate(nums2):
            pos_in_nums2[val] = i

        transformed = [pos_in_nums2[val] for val in nums1]

        left_tree = FenwickTree(n)
        right_tree = FenwickTree(n)

        # Prepopulate right tree with all values
        for val in transformed:
            right_tree.update(val, 1)

        result = 0

        for val in transformed:
            right_tree.update(val, -1)  # Remove current value from right
            left_count = left_tree.query(val - 1)  # Count of values < val on the left
            right_count = right_tree.query(n - 1) - right_tree.query(val)  # Count of values > val on the right
            result += left_count * right_count
            left_tree.update(val, 1)  # Add current value to left

        return result