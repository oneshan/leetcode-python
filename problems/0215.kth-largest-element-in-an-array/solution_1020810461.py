# 0215 - Kth Largest Element in an Array
# Date: 2023-08-14
# Runtime: 448 ms, Memory: 29.6 MB
# Submission Id: 1020810461


import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
        
        def quick_select(left, right):
            pivot_idx = random.randrange(left, right+1)
            pivot = nums[pivot_idx]
            swap(pivot_idx, right)
            
            store_i = left
            for i in range(left, right):
                if nums[i] < pivot:
                    swap(i, store_i)
                    store_i += 1
                    
            swap(store_i, right)
            return store_i
        
        left, right = 0, n-1
        while True:
            p = quick_select(left, right)
            if n - k == p:
                return nums[p]
            if n - k > p:
                left = p + 1
            else:
                right = p - 1