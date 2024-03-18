# 0484 - Find Permutation
# Date: 2024-03-17
# Runtime: 53 ms, Memory: 18 MB
# Submission Id: 1206238742


class Solution:
    def findPermutation(self, s: str) -> List[int]:
        n = len(s)
        ans = []

        stack = []
        for i in range(n+1):
            stack.append(i+1)
            if i == n or s[i] == 'I':
                while stack:
                    ans.append(stack.pop())
        return ans