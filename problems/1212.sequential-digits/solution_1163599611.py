# 1212 - Sequential Digits
# Date: 2024-02-02
# Runtime: 39 ms, Memory: 16.5 MB
# Submission Id: 1163599611


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        
        digits = "123456789"
        for length in range(2, 10):
            for start in range(10-length):
                num = int(digits[start:start+length])
                if low <= num <= high:
                    ans.append(num)
        return ans