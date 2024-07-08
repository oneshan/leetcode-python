# 1017 - Odd Even Jump
# Date: 2024-06-10
# Runtime: 248 ms, Memory: 22.3 MB
# Submission Id: 1283799164


class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        arr = [(idx, num) for idx, num in enumerate(arr)]
        n = len(arr)
        
        next_greater = [-1] * n
        stack = []
        for idx, num in sorted(arr, key=lambda x: (x[1], x[0])):
            while stack and stack[-1] < idx:
                next_greater[stack.pop()] = idx
            stack.append(idx)

        next_smaller = [-1] * n
        stack = []
        for idx, num in sorted(arr, key=lambda x: (-x[1], x[0])):
            while stack and stack[-1] < idx:
                next_smaller[stack.pop()] = idx
            stack.append(idx)

        # [odd, even], the 0th jump is even
        dp = [[0,1] for _ in range(n)]

        for i in range(n):
            if next_greater[i] != -1:
                dp[next_greater[i]][0] += dp[i][1]
            if next_smaller[i] != -1:
                dp[next_smaller[i]][1] += dp[i][0]
				
        return dp[-1][0] + dp[-1][1]