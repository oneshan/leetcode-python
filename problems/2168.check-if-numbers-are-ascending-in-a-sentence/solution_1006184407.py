# 2168 - Check if Numbers Are Ascending in a Sentence
# Date: 2023-07-28
# Runtime: 37 ms, Memory: 16.1 MB
# Submission Id: 1006184407


class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev, curr = -1, 0
        
        for ch in s:
            if ch.isdigit():
                curr = curr * 10 + ord(ch) - 48
            elif curr:
                if prev >= curr:
                    return False
                prev, curr = curr, 0
        return curr == 0 or prev < curr