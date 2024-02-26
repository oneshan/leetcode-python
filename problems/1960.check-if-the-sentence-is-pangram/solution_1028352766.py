# 1960 - Check if the Sentence Is Pangram
# Date: 2023-08-22
# Runtime: 36 ms, Memory: 16.3 MB
# Submission Id: 1028352766


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = set(sentence)
        return len(seen) == 26