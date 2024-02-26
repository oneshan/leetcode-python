# 2337 - Remove Digit From Number to Maximize Result
# Date: 2022-10-13
# Runtime: 55 ms, Memory: 13.9 MB
# Submission Id: 821651648


class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        remove_idx = 0
        
        for idx in range(len(number)-1):
            if number[idx] == digit:
                remove_idx = idx
                if number[idx+1] > number[idx]:
                    return number[:remove_idx] + number[remove_idx+1:]
        if number[-1] == digit:
            remove_idx = len(number)-1

        return number[:remove_idx] + number[remove_idx+1:]