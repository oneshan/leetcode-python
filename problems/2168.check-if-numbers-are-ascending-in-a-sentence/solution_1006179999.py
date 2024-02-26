# 2168 - Check if Numbers Are Ascending in a Sentence
# Date: 2023-07-28
# Runtime: 41 ms, Memory: 16.2 MB
# Submission Id: 1006179999


class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev, curr = -1, 0
        
        for ch in s:
            if ch.isdigit():
                curr = curr * 10 + int(ch)
            elif curr:
                if prev >= curr:
                    return False
                prev, curr = curr, 0
        return curr == 0 or prev < curr