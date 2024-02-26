# 0496 - Next Greater Element I
# Date: 2023-09-11
# Runtime: 57 ms, Memory: 16.7 MB
# Submission Id: 1046380552


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        table = {}
        stack = []
        for idx, num in enumerate(nums2):
            table[num] = -1
            while stack and nums2[stack[-1]] < num:
                table[nums2[stack.pop()]] = num
            stack.append(idx)
            
        return [table[num] for num in nums1]