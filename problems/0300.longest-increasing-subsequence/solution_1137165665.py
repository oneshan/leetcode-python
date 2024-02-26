# 0300 - Longest Increasing Subsequence
# Date: 2024-01-05
# Runtime: 63 ms, Memory: 17.6 MB
# Submission Id: 1137165665


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = []
        for num in nums:
            
            left, right = 0, len(ans)
            while left < right:
                mid = (left + right) // 2
                if ans[mid] < num:
                    left = mid + 1
                else:
                    right = mid
                
            if left == len(ans):
                ans.append(num)
            else:
                ans[left] = num

        return len(ans)