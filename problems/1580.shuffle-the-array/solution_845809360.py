# 1580 - Shuffle the Array
# Date: 2022-11-18
# Runtime: 360 ms, Memory: 14.1 MB
# Submission Id: 845809360


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        yi = n
        for xi in range(1, 2*n-1):
            if xi & 1:
                reverse(xi, yi)
                reverse(xi+1, yi)
                yi += 1
        return nums