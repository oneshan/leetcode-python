# 0215 - Kth Largest Element in an Array
# Date: 2022-10-20
# Runtime: 1443 ms, Memory: 34.7 MB
# Submission Id: 826588789


from random import randint

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def partition(left, right):
            pivot_index = randint(left, right)
            pivot = nums[pivot_index]
            
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            sorted_i = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[i], nums[sorted_i] = nums[sorted_i], nums[i]
                    sorted_i += 1
            nums[right], nums[sorted_i] = nums[sorted_i], nums[right]
            return sorted_i

        
        def select(left, right, k_smallest):
            if left == right:
                return nums[left]
            
            pivot_index = partition(left, right)
            if k_smallest < pivot_index:
                return select(left, pivot_index-1, k_smallest)
            if k_smallest > pivot_index:
                return select(pivot_index+1, right, k_smallest) 
            return nums[k_smallest]
        
        return select(0, len(nums)-1, len(nums)-k)   