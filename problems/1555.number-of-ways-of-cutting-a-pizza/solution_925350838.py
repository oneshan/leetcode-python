# 1555 - Number of Ways of Cutting a Pizza
# Date: 2023-03-31
# Runtime: 174 ms, Memory: 16 MB
# Submission Id: 925350838


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        MOD = 10 ** 9 + 7
        len_r, len_c = len(pizza), len(pizza[0])
        
        suffix_sums = [[0] * (len_c + 1) for r in range(len_r + 1)]
        for row, col in product(reversed(range(len_r)), reversed(range(len_c))):
            suffix_sums[row][col] = ((pizza[row][col] == 'A')
                                     + suffix_sums[row+1][col]
                                     + suffix_sums[row][col+1]
                                     - suffix_sums[row+1][col+1])

        @cache
        def dfs(row, col, cuts_left):
            if cuts_left == 0:
                return suffix_sums[row][col] > 0
            ans = 0
            for next_r in range(row+1, len_r):
                if suffix_sums[row][col] > suffix_sums[next_r][col]:
                    ans += dfs(next_r, col, cuts_left - 1)
            for next_c in range(col+1, len_c):
                if suffix_sums[row][col] > suffix_sums[row][next_c]:
                    ans += dfs(row, next_c, cuts_left - 1)
            return ans
        
        return dfs(0, 0, k-1) % MOD