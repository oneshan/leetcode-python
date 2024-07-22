# 3462 - Vowels Game in a String
# Date: 2024-07-21
# Runtime: 73 ms, Memory: 17.4 MB
# Submission Id: 1327909180


class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        count = 0
        for ch in s:
            if ch in vowels:
                count += 1

        if count == 0:
            return False
        return True