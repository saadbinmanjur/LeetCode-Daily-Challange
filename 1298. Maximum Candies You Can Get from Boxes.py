from collections import deque
from typing import List

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        visited = [False] * n  # To avoid reprocessing boxes
        has_key = set()
        queue = deque()
        
        # Initially, try to open the boxes you have
        for box in initialBoxes:
            queue.append(box)

        total_candies = 0
        
        while queue:
            size = len(queue)
            did_progress = False
            for _ in range(size):
                box = queue.popleft()
                if visited[box]:
                    continue
                # Can open if we have key or it's already open
                if status[box] == 1 or box in has_key:
                    visited[box] = True
                    total_candies += candies[box]
                    did_progress = True
                    
                    # Collect keys
                    for key in keys[box]:
                        has_key.add(key)
                    
                    # Add contained boxes to queue
                    for contained in containedBoxes[box]:
                        queue.append(contained)
                    
                    # Some boxes may become open because of newly added keys
                    status[box] = 1
                else:
                    # Cannot open yet, try later
                    queue.append(box)
            if not did_progress:
                break

        return total_candies
