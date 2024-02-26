# 1212 - Sequential Digits
# Date: 2024-02-02
# Runtime: 32 ms, Memory: 16.5 MB
# Submission Id: 1163597210


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        
        for i in range(1, 10):
            num = 0
            digit = i
            while num < high and digit < 10:
                num = num * 10 + digit
                digit += 1
                if low <= num <= high:
                    ans.append(num)
                    
        return sorted(ans)