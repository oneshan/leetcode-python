# 2469 - Longest Subsequence With Limited Sum
# Date: 2023-09-17
# Runtime: 102 ms, Memory: 16.6 MB
# Submission Id: 1051898082


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        m = len(queries)
        
        nums.sort()
        for i in range(1, n):
            nums[i] += nums[i-1]
        
        def binary_search(target):
            left, right = 0, n
            while left < right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid
                else:
                    left = mid + 1
            return left
        
        ans = []
        for query in queries:
            ans.append(binary_search(query))
        return ans