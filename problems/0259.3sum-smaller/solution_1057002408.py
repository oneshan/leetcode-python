# 0259 - 3Sum Smaller
# Date: 2023-09-23
# Runtime: 1010 ms, Memory: 16.1 MB
# Submission Id: 1057002408


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        
        ans = 0
        for i in range(n):
            j, k = i+1, n-1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < target:
                    ans += (k-j)
                    j += 1
                else:
                    k -= 1
        return ans