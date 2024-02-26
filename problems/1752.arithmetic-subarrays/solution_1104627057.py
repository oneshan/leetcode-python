# 1752 - Arithmetic Subarrays
# Date: 2023-11-23
# Runtime: 217 ms, Memory: 16.5 MB
# Submission Id: 1104627057


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        n = len(l)
        ans = [0] * n
        
        def check(left, right):
            arr = set()
            for i in range(left, right+1):
                arr.add(nums[i])
                
            n = len(arr)
            
            if n == 1:
                return True
            if n != right-left+1:
                return False
            
            diff = (max(arr) - min(arr)) // (n-1)
            curr = min(arr)
            for i in range(n):
                if curr not in arr:
                    return False
                curr += diff
            return True
        
        
        for idx, (left, right) in enumerate(zip(l, r)):
            ans[idx] = check(left, right)
        return ans