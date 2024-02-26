# 1297 - Maximum Number of Balloons
# Date: 2022-10-14
# Runtime: 81 ms, Memory: 14 MB
# Submission Id: 822296896


from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        table = defaultdict(int)
        for ch in text:
            table[ch] += 1
        
        pattern = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
        ans = float('inf')
        for ch, count in pattern.items():
            ans = min(table[ch] // count, ans)
        return ans