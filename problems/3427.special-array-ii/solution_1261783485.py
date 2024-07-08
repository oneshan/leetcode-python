# 3427 - Special Array II
# Date: 2024-05-19
# Runtime: 1142 ms, Memory: 56 MB
# Submission Id: 1261783485


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        
        intervals = [[0, 0]]
        for i in range(1, n):
            if nums[i] & 1 == nums[intervals[-1][1]] & 1:
                intervals.append([i, i])
            else:
                intervals[-1][1] = i
        
        ans = []
        for _from, _to in queries:

            idx = -1
            left, right = 0, len(intervals) -1
            while left <= right:
                mid = (left + right) // 2
                if intervals[mid][0] <= _from <= intervals[mid][1]:
                    idx = mid
                    break
                if _from < intervals[mid][0]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            ans.append(_to <= intervals[idx][1])
            
        return ans
                