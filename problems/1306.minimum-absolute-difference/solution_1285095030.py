# 1306 - Minimum Absolute Difference
# Date: 2024-06-12
# Runtime: 309 ms, Memory: 31 MB
# Submission Id: 1285095030


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        
        min_diff = float('inf')
        ans = []
        
        for i in range(1, len(arr)):
            curr_diff = arr[i] - arr[i-1]
            
            if curr_diff < min_diff:
                min_diff = curr_diff
                ans = []
                
            if curr_diff == min_diff:
                ans.append([arr[i-1], arr[i]])
                
        return ans
            
            