# 0013 - Roman to Integer
# Date: 2022-11-11
# Runtime: 97 ms, Memory: 13.9 MB
# Submission Id: 841440262


class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        
        ans = 0
        for i in range(1, len(s)):
            if mapping[s[i-1]] < mapping[s[i]]:
                ans -= mapping[s[i-1]]
            else:
                ans += mapping[s[i-1]]
        ans += mapping[s[-1]]
        return ans