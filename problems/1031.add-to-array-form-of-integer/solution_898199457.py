# 1031 - Add to Array-Form of Integer
# Date: 2023-02-15
# Runtime: 292 ms, Memory: 15 MB
# Submission Id: 898199457


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        idx_n = len(num)-1
        carry = 0
        ans = []
        while idx_n >= 0 or k:
            k, digit = divmod(k, 10)
            digit += (num[idx_n] if idx_n >= 0 else 0) + carry
            carry, digit = divmod(digit, 10)
            idx_n -= 1
            ans.append(digit)
        if carry:
            ans.append(carry)
        return ans[::-1]