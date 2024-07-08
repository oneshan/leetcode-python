# 1703 - Put Boxes Into the Warehouse I
# Date: 2024-06-15
# Runtime: 442 ms, Memory: 35.6 MB
# Submission Id: 1288894732


class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes.sort(reverse=True)
        i = 0
        for box in boxes:
            if box <= warehouse[i]:
                i += 1
                if i == len(warehouse):
                    break
        return i