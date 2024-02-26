# 0807 - Custom Sort String
# Date: 2023-08-31
# Runtime: 46 ms, Memory: 16.3 MB
# Submission Id: 1036096837


from collections import defaultdict
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        table = defaultdict(int)
        for idx, ch in enumerate(order):
            table[ch] = idx
        
        chars = list(s)
        chars.sort(key=lambda x: table[x])
        return ''.join(chars)