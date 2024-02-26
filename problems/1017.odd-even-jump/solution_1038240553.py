# 1017 - Odd Even Jump
# Date: 2023-09-02
# Runtime: 285 ms, Memory: 22.9 MB
# Submission Id: 1038240553


class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        
        # next-greater-number
        next_greater = [-1] * n        
        stack = []
        for i, num in sorted(enumerate(arr), key=lambda x: (x[1], x[0])):
            while stack and stack[-1] < i:
                idx = stack.pop()
                next_greater[idx] = i
            stack.append(i)

        # next-smaller-number
        next_smaller = [-1] * n
        stack = []
        for i, num in sorted(enumerate(arr), key=lambda x: (-x[1], x[0])):
            while stack and stack[-1] < i:
                idx = stack.pop()
                next_smaller[idx] = i
            stack.append(i)

        # [odd, even], the 0th jump is even
        dp = [[0,1] for _ in range(n)]
        for i in range(n):
            if next_greater[i] != -1:
                dp[next_greater[i]][0] += dp[i][1]
            if next_smaller[i] != -1:
                dp[next_smaller[i]][1] += dp[i][0]
				
        return dp[-1][0] + dp[-1][1]