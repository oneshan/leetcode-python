# 1752 - Arithmetic Subarrays
# Date: 2023-11-23
# Runtime: 168 ms, Memory: 16.8 MB
# Submission Id: 1104625868


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        n = len(l)
        ans = [0] * n
        
        def check(left, right):
            arr = nums[left:right+1]
            arr.sort()
            diff = arr[1] - arr[0]
            for i in range(2, len(arr)):
                if arr[i] - arr[i-1] != diff:
                    return False
            return True
        
        
        for idx, (left, right) in enumerate(zip(l, r)):
            ans[idx] = check(left, right)
        return ans