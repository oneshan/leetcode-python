# 0911 - Profitable Schemes
# Date: 2023-04-21
# Runtime: 3561 ms, Memory: 648.5 MB
# Submission Id: 937288161


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        mod = 10 ** 9 + 7
        len_g = len(group)
        
        @cache
        def dfs(i, current_profit, people):
            if i >= len_g:
                return current_profit >= minProfit
            res = dfs(i+1, current_profit, people)
            if people + group[i] <= n:
                # avoid TLE
                current_profit = min(minProfit, current_profit + profit[i])
                res += dfs(i+1, current_profit, people + group[i])
            return res
        
        return dfs(0, 0, 0) % mod