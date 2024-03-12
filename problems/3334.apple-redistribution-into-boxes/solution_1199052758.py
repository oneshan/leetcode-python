# 3334 - Apple Redistribution into Boxes
# Date: 2024-03-10
# Runtime: 54 ms, Memory: 16.5 MB
# Submission Id: 1199052758


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        total = sum(apple)
        
        for i, c in enumerate(capacity, 1):
            total -= c
            if total <= 0:
                return i