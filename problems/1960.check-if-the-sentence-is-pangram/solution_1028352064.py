# 1960 - Check if the Sentence Is Pangram
# Date: 2023-08-22
# Runtime: 42 ms, Memory: 16.4 MB
# Submission Id: 1028352064


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = set()
        for ch in sentence:
            seen.add(ch)
        return len(seen) >= 26