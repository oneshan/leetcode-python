# 1044 - Find Common Characters
# Date: 2024-06-05
# Runtime: 63 ms, Memory: 16.7 MB
# Submission Id: 1278068564


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counter = Counter(words[0])
        for i in range(1, len(words)):
            curr = Counter(words[i])
            for ch in counter:
                counter[ch] = min(counter[ch], curr[ch])
        
        ans = []
        for ch in counter:
            if counter[ch]:
                ans += [ch] * counter[ch]
        return ans