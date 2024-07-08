# 0060 - Permutation Sequence
# Date: 2024-06-07
# Runtime: 38 ms, Memory: 16.4 MB
# Submission Id: 1279728861


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n+1)]

        # n!
        factorial = 1
        for i in range(1, n+1):
            factorial *= i
        
        k -= 1
        ans = []

        for i in range(n, 0, -1):
            factorial //= i
            idx, k = divmod(k, factorial)

            ans.append(nums.pop(idx))  # O(N)

        return ''.join(ans)