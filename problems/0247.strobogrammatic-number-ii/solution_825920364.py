# 0247 - Strobogrammatic Number II
# Date: 2022-10-19
# Runtime: 444 ms, Memory: 30 MB
# Submission Id: 825920364


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        candidates = {
            '1': '1',
            '0': '0',
            '8': '8',
            '6': '9',
            '9': '6',
        }
        
        ans = []
        if n == 1:
            return ["0","1","8"]
        
        def generate(curr, idx):
            if idx == n:
                if curr[0] != '0': ans.append(curr)
                return
            for x, y in candidates.items():
                generate(x+curr+y, idx+2)
        
        if n & 1:
            generate('1', 1)
            generate('0', 1)
            generate('8', 1)
        else:
            generate('', 0)
        return ans