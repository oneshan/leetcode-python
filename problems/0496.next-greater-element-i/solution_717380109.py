# 0496 - Next Greater Element I
# Date: 2022-06-08
# Runtime: 40 ms, Memory: 14.2 MB
# Submission Id: 717380109


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        table = {}
        stack = []
        
        for num in nums2:
            while stack and stack[-1] < num:
                table[stack.pop()] = num
            stack.append(num)
        
        return [table.get(num, -1) for num in nums1]