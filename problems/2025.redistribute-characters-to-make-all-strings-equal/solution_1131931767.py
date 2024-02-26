# 2025 - Redistribute Characters to Make All Strings Equal
# Date: 2023-12-30
# Runtime: 115 ms, Memory: 17.3 MB
# Submission Id: 1131931767


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counter = defaultdict(int)
        
        n = len(words)
        for word in words:
            for ch in word:
                counter[ch] += 1
                
        for count in counter.values():
            if count % n != 0:
                return False
        return True