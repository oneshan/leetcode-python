# 2532 - Remove Letter To Equalize Frequency
# Date: 2022-10-07
# Runtime: 58 ms, Memory: 14 MB
# Submission Id: 817190607


from collections import Counter
class Solution:
    def equalFrequency(self, word: str) -> bool:
        
        counter = Counter(word)
        # aaaaa, abcde
        if len(counter) == len(word) or len(counter) == 1:
            return True
        
        freq = Counter(counter.values())
        if len(freq) > 2:
            return False
        
        max_freq = max(freq)
        # abcc
        if freq[max_freq] == 1 and freq[max_freq-1]:
            return True

        min_freq = min(freq)
        # abbcc
        if freq[min_freq] == 1 and min_freq == 1:
            freq.pop(min_freq)
            return len(freq) == 1
        return False