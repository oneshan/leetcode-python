# 0360 - Sort Transformed Array
# Date: 2023-10-03
# Runtime: 48 ms, Memory: 16.3 MB
# Submission Id: 1066006841


class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        
        def transform(x):
            return a * x * x + b * x + c
        
        n = len(nums)
        ans = [0] * n
        left, right = 0, n-1
        if a < 0:
            for i in range(n):
                left_val, right_val = transform(nums[left]), transform(nums[right])
                if left_val < right_val:
                    ans[i] = left_val
                    left += 1
                else:
                    ans[i] = right_val
                    right -= 1
        else:
            for i in range(n-1, -1, -1):
                left_val, right_val = transform(nums[left]), transform(nums[right])
                if left_val > right_val:
                    ans[i] = left_val
                    left += 1
                else:
                    ans[i] = right_val
                    right -= 1

        return ans