# 0749 - Shortest Completing Word
# Date: 2024-06-02
# Runtime: 86 ms, Memory: 16.8 MB
# Submission Id: 1274967358


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        require = Counter()
        for ch in licensePlate:
            if ch.isalpha():
                require[ch.lower()] += 1
        print(require)
        
        ans_len, ans_word = float('inf'), None
        for word in words:
            counter = Counter(word)
            if all(require[ch] <= counter[ch] for ch in require):
                if ans_len > len(word):
                    ans_len, ans_word = len(word), word
        
        return ans_word