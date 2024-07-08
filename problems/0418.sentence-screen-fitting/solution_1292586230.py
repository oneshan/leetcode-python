# 0418 - Sentence Screen Fitting
# Date: 2024-06-19
# Runtime: 62 ms, Memory: 16.6 MB
# Submission Id: 1292586230


class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        s = ' '.join(sentence) + ' '
        n = len(s)

        mapping = [0] * n  # number shift to the beginning of word
        for i in range(1, n):
            mapping[i] = 1 if s[i] == ' ' else mapping[i-1]-1

        count = 0
        for i in range(rows):
            count += cols
            count += mapping[count % n]
            
        return count // n