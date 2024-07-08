# 1044 - Find Common Characters
# Date: 2024-06-02
# Runtime: 51 ms, Memory: 16.6 MB
# Submission Id: 1275100417


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