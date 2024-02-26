# 1418 - Fair Distribution of Cookies
# Date: 2023-07-01
# Runtime: 55 ms, Memory: 16.4 MB
# Submission Id: 983431337


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        curr = [0] * k
        
        def backtrack(i):
            if i == n:
                return max(curr)
            ans = float('inf')
            for child in range(k):
                curr[child] += cookies[i]
                ans = min(ans, backtrack(i+1))
                curr[child] -= cookies[i]
                if curr[child] == 0:  # trim dupes and permutations
                    break
            return ans
            
        return backtrack(0)