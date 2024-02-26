# 0067 - Add Binary
# Date: 2024-02-06
# Runtime: 36 ms, Memory: 16.6 MB
# Submission Id: 1167684476


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        idx_a, idx_b = len(a)-1, len(b)-1
        ans = []
        carry = 0
        while idx_a >= 0 or idx_b >= 0:
            if idx_a >= 0:
                carry += a[idx_a] == '1'
                idx_a -= 1
            if idx_b >= 0:
                carry += b[idx_b] == '1'
                idx_b -= 1
            ans.append('1' if carry & 1 else '0')
            carry >>= 1
        
        if carry:
            ans.append('1')
        return ''.join(ans[::-1])