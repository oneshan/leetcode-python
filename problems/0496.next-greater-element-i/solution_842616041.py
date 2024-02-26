# 0496 - Next Greater Element I
# Date: 2022-11-13
# Runtime: 50 ms, Memory: 14.1 MB
# Submission Id: 842616041


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                prev_num = stack.pop()
                next_greater[prev_num] = num
            stack.append(num)
        
        return [next_greater.get(num, -1) for num in nums1]