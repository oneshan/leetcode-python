# 0892 - Shortest Subarray with Sum at Least K
# Date: 2024-06-01
# Runtime: 872 ms, Memory: 30.9 MB
# Submission Id: 1273987412


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:

        prefix = [0] * (len(nums)+1)
        for i in range(len(nums)):
            prefix[i+1] = prefix[i] + nums[i]
        
        ans = float('inf')
        queue = deque() # mono-increasing

        for i in range(len(nums)+1):

            while queue and prefix[queue[-1]] >= prefix[i]:
                queue.pop()
            
            while queue and prefix[i] - prefix[queue[0]] >= k:
                ans = min(ans, i - queue.popleft())

            queue.append(i)

        return ans if ans != float('inf') else -1