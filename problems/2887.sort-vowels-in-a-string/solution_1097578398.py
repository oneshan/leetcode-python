# 2887 - Sort Vowels in a String
# Date: 2023-11-13
# Runtime: 167 ms, Memory: 18.3 MB
# Submission Id: 1097578398


from collections import Counter

class Solution:
    def sortVowels(self, s: str) -> str:
        counter = Counter(s)
        vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
        vowels_set = set(vowels)
        idx = 0
        
        ans = []
        for ch in s:
            if ch not in vowels_set:
                ans.append(ch)
            else:
                while counter[vowels[idx]] == 0:
                    idx += 1
                counter[vowels[idx]] -= 1
                ans.append(vowels[idx])
        return ''.join(ans)