# 1719 - Put Boxes Into the Warehouse II
# Date: 2024-06-15
# Runtime: 442 ms, Memory: 35.6 MB
# Submission Id: 1288897621


class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes.sort(reverse=True)

        ans = 0
        left, right = 0, len(warehouse)-1
        for box in boxes:
            if box <= warehouse[left]:
                left += 1
                ans += 1
            elif box <= warehouse[right]:
                right -= 1
                ans += 1
            
            if left > right:
                break

        return ans