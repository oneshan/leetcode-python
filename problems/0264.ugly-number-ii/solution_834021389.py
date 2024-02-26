# 0264 - Ugly Number II
# Date: 2022-10-31
# Runtime: 134 ms, Memory: 13.9 MB
# Submission Id: 834021389


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [0] * n
        nums[0] = 1
        
        i2 = i3 = i5 = 0
        for i in range(1, n):
            n2, n3, n5 = nums[i2]*2, nums[i3]*3, nums[i5]*5
            nums[i] = min(n2, n3, n5)
            if nums[i] == n2:
                i2 += 1
            if nums[i] == n3:
                i3 += 1
            if nums[i] == n5:
                i5 += 1
        return nums[-1]