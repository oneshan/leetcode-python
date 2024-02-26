# 0952 - Word Subsets
# Date: 2022-09-29
# Runtime: 1170 ms, Memory: 18.6 MB
# Submission Id: 811353072


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def count(word):
            freq = [0] * 26
            for ch in word:
                freq[ord(ch)-97] += 1
            return freq
        
        bmax = [0] * 26
        for word in words2:
            for idx, freq in enumerate(count(word)):
                bmax[idx] = max(bmax[idx], freq)
                
        ans = []
        for word in words1:
            for idx, freq in enumerate(count(word)):
                if freq < bmax[idx]:
                    break
            else:
                ans.append(word)
        
        return ans