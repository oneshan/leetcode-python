# 2713 - Find the Divisibility Array of a String
# Date: 2023-09-24
# Runtime: 369 ms, Memory: 25.6 MB
# Submission Id: 1057871669


class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        n = len(word)
        div = [0] * n
        num = 0
        for idx, ch in enumerate(word):
            num = ((num * 10) + int(ch)) % m
            div[idx] = 1 if num == 0 else 0

        return div