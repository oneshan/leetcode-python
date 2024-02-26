# 0496 - Next Greater Element I
# Date: 2023-09-11
# Runtime: 48 ms, Memory: 16.5 MB
# Submission Id: 1046381283


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        table = {}
        stack = []
        for num in nums2:
            table[num] = -1
            while stack and stack[-1] < num:
                table[stack.pop()] = num
            stack.append(num)
            
        return [table[num] for num in nums1]