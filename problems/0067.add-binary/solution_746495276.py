# 0067 - Add Binary
# Date: 2022-07-14
# Runtime: 31 ms, Memory: 14 MB
# Submission Id: 746495276


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = []
        pa, pb = len(a), len(b)
        carry = 0
        while pa and pb:
            digit = int(a[pa-1]) + int(b[pb-1]) + carry
            carry, digit = divmod(digit, 2)
            ans.append(digit)
            pa -= 1
            pb -= 1
        
        if pb:
            pa, a = pb, b
        while pa and carry:
            digit = int(a[pa-1]) + carry
            carry, digit = divmod(digit, 2)
            ans.append(digit)
            pa -= 1
            
        if carry:
            ans.append(1)
        return a[:pa] + ''.join(map(str, ans))[::-1]