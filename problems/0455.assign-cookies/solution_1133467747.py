# 0455 - Assign Cookies
# Date: 2024-01-01
# Runtime: 126 ms, Memory: 19.3 MB
# Submission Id: 1133467747


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        len_g, len_s = len(g), len(s)
        idx_g = idx_s = 0
        
        ans = 0
        while idx_g < len_g and idx_s < len_s:
            if g[idx_g] <= s[idx_s]:
                idx_g += 1
                idx_s += 1
                ans += 1
            else:
                idx_s += 1
        return ans