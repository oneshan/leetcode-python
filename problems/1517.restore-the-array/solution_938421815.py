# 1517 - Restore The Array
# Date: 2023-04-23
# Runtime: 1264 ms, Memory: 176.2 MB
# Submission Id: 938421815


class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        mod = 10 ** 9 + 7
        n = len(s)
        
        @cache
        def recur(i):
            if i == n:
                return 1
            if s[i] == '0':
                return 0
            res = num = 0
            for j in range(i, n):
                num = num * 10 + ord(s[j]) - ord('0')
                if num > k:
                    break
                res += recur(j+1)
            return res % mod
        
        return recur(0)