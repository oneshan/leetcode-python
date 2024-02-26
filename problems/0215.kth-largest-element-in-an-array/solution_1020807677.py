# 0215 - Kth Largest Element in an Array
# Date: 2023-08-14
# Runtime: 426 ms, Memory: 29.6 MB
# Submission Id: 1020807677


import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        while True:
            pivot = random.choice(nums)
            left, mid, right = [], [], []
            for num in nums:
                if num > pivot:
                    left.append(num)
                elif num < pivot:
                    right.append(num)
                else:
                    mid.append(num)
            if k <= len(left):
                nums = left
            elif len(left) + len(mid) < k:
                nums, k = right, k - (len(left) + len(mid))
            else:
                return pivot