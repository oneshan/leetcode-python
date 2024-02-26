# 2887 - Sort Vowels in a String
# Date: 2023-08-05
# Runtime: 155 ms, Memory: 18.4 MB
# Submission Id: 1012606447


from collections import defaultdict

class Solution:
    def sortVowels(self, s: str) -> str:
        s_list = list(s)
        v_chars = 'AEIOUaeiou'
        
        vowels = defaultdict(int)
        for ch in s:
            if ch in v_chars:
                vowels[ch] += 1
        
        v_idx = 0
        while v_idx < 10 and vowels[v_chars[v_idx]] == 0:
            v_idx += 1
        
        for idx, ch in enumerate(s_list):
            if ch in v_chars:
                s_list[idx] = v_chars[v_idx]
                vowels[v_chars[v_idx]] -= 1
                while v_idx < 10 and vowels[v_chars[v_idx]] == 0:
                    v_idx += 1
                    
        return ''.join(s_list)