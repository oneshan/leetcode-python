# 1297 - Maximum Number of Balloons
# Date: 2023-08-22
# Runtime: 42 ms, Memory: 16.4 MB
# Submission Id: 1028627867


from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = Counter(text)
        target = Counter('balloon')
        
        ans = float('inf')
        for ch, count in target.items():
            ans = min(ans, counter[ch] // count)
        return ans