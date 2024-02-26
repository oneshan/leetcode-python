# 1031 - Add to Array-Form of Integer
# Date: 2023-02-15
# Runtime: 272 ms, Memory: 15.1 MB
# Submission Id: 898203254


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        carry = k
        for i in range(len(num)-1, -1, -1):
            if not carry:
                return num
            carry, num[i] = divmod(carry + num[i], 10)
            
        prev = []
        while carry:
            carry, digit = divmod(carry, 10)
            prev.append(digit)

        return prev[::-1] + num