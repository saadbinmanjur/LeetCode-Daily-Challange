from typing import List
import bisect
from collections import deque

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()

        def can_assign(k):
            available_workers = deque(workers[-k:])
            i = k - 1
            pills_left = pills
            temp = []

            for j in reversed(range(k)):
                task = tasks[j]
                if available_workers and available_workers[-1] >= task:
                    available_workers.pop()
                elif pills_left > 0:
                    while available_workers and available_workers[0] + strength < task:
                        available_workers.popleft()
                    if not available_workers:
                        return False
                    pills_left -= 1
                    available_workers.popleft()
                else:
                    return False
            return True

        low, high = 0, min(len(tasks), len(workers))
        res = 0
        while low <= high:
            mid = (low + high) // 2
            if can_assign(mid):
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        return res
