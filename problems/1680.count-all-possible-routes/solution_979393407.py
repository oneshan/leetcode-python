# 1680 - Count All Possible Routes
# Date: 2023-06-25
# Runtime: 2016 ms, Memory: 41.2 MB
# Submission Id: 979393407


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        mod = 10 ** 9 + 7
        
        @cache
        def dfs(pos, remains):
            if remains < 0:
                return 0
            
            ans = 0
            if pos == finish:
                ans = 1
            for next_pos in range(n):
                if pos == next_pos:
                    continue
                ans += dfs(next_pos, remains - abs(locations[pos] - locations[next_pos]))
            
            return ans % mod
        
        return dfs(start, fuel)