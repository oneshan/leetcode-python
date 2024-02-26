# 0451 - Sort Characters By Frequency
# Date: 2022-12-03
# Runtime: 78 ms, Memory: 15.2 MB
# Submission Id: 853734968


from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        
        pair = sorted([(count, ch) for ch, count in counter.items()], reverse=True)
        return ''.join([ch * count for count, ch in pair])