# 0067 - Add Binary
# Date: 2023-02-14
# Runtime: 29 ms, Memory: 13.9 MB
# Submission Id: 897755904


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = []
        idx_a, idx_b = len(a)-1, len(b)-1
        carry = 0
        while idx_a >= 0 or idx_b >= 0:
            bit_a = int(a[idx_a]) if idx_a >= 0 else 0
            bit_b = int(b[idx_b]) if idx_b >= 0 else 0
            carry, digit = divmod(bit_a + bit_b + carry, 2)
            ans.append(str(digit))
            idx_a -= 1
            idx_b -= 1
        if carry:
            ans.append('1')
        return ''.join(ans[::-1])