# 1555 - Number of Ways of Cutting a Pizza
# Date: 2023-03-31
# Runtime: 176 ms, Memory: 16 MB
# Submission Id: 925351670


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        MOD = 10 ** 9 + 7
        len_r, len_c = len(pizza), len(pizza[0])
        
        apples = [[0] * (len_c + 1) for r in range(len_r + 1)]
        for row in range(len_r-1, -1, -1):
            for col in range(len_c-1, -1, -1):
                apples[row][col] = ((pizza[row][col] == 'A')
                                     + apples[row+1][col]
                                     + apples[row][col+1]
                                     - apples[row+1][col+1])

        @cache
        def dfs(row, col, cuts_left):
            if cuts_left == 0:
                return apples[row][col] > 0
            ans = 0
            for next_r in range(row+1, len_r):
                if apples[row][col] > apples[next_r][col]:
                    ans += dfs(next_r, col, cuts_left - 1)
            for next_c in range(col+1, len_c):
                if apples[row][col] > apples[row][next_c]:
                    ans += dfs(row, next_c, cuts_left - 1)
            return ans
        
        return dfs(0, 0, k-1) % MOD