# 0408 - Valid Word Abbreviation
# Date: 2024-05-01
# Runtime: 41 ms, Memory: 16.7 MB
# Submission Id: 1246112383


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        wi = ai = 0
        while wi < len(word) and ai < len(abbr):
            # char
            if not abbr[ai].isdigit():
                if word[wi] != abbr[ai]:
                    return False
                wi += 1
                ai += 1
                continue

            # int
            if abbr[ai] == '0':
                return False
            num = 0
            while ai < len(abbr) and abbr[ai].isdigit():
                num = num * 10 + int(abbr[ai])
                ai += 1
            wi += num

        return wi == len(word) and ai == len(abbr)