# 1549 - Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
# Date: 2022-10-01
# Runtime: 916 ms, Memory: 23.3 MB
# Submission Id: 812693311


from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_queue = deque()
        min_queue = deque()
        left = ans = 0
        for right in range(len(nums)):
            while max_queue and nums[max_queue[-1]] < nums[right]:
                max_queue.pop()
            while min_queue and nums[min_queue[-1]] > nums[right]:
                min_queue.pop()
                
            max_queue.append(right)
            min_queue.append(right)
        
            while nums[max_queue[0]] - nums[min_queue[0]] > limit:
                if max_queue[0] == left:
                    max_queue.popleft()
                if min_queue[0] == left:
                    min_queue.popleft()
                left += 1
            
            ans = max(ans, right - left + 1)
        return ans