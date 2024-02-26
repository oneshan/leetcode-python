# 1046 - Max Consecutive Ones III
# Date: 2023-10-25
# Runtime: 544 ms, Memory: 17.2 MB
# Submission Id: 1083916612


from collections import deque

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = deque([-1])
        ans = 0
        for idx, num in enumerate(nums):
            if num == 0:
                zeros.append(idx)
            if len(zeros) > k+1:
                zeros.popleft()
            ans = max(ans, idx - (zeros[0] if zeros else 0))
        return ans