# 1212 - Sequential Digits
# Date: 2024-02-02
# Runtime: 35 ms, Memory: 16.6 MB
# Submission Id: 1163600111


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        
        digits = "123456789"
        for length in range(1, 10):
            for start in range(10-length):
                num = int(digits[start:start+length])
                if low <= num <= high:
                    ans.append(num)
        return ans