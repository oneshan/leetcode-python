# 2469 - Longest Subsequence With Limited Sum
# Date: 2022-10-11
# Runtime: 161 ms, Memory: 14.2 MB
# Submission Id: 820097295


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        def binary_search(arr, target):
            left, right = 0, len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        n, m = len(nums), len(queries)
        nums.sort()
        for i in range(1, n):
            nums[i] += nums[i-1]
        
        ans = [0] * m
        for i in range(m):
            ans[i] = binary_search(nums, queries[i]) # O(mlogn)
        return ans