# 0038 - Count and Say
# Date: 2024-06-05
# Runtime: 38 ms, Memory: 16.6 MB
# Submission Id: 1278206406


class Solution:

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        
        res = []

        prev, count = '', 0
        for ch in self.countAndSay(n-1):
            if ch == prev:
                count += 1
            else:
                res.append(f'{count}{prev}')
                prev, count = ch, 1
        
        res.append(f'{count}{prev}')

        return ''.join(res[1:])