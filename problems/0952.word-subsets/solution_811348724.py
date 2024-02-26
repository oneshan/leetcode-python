# 0952 - Word Subsets
# Date: 2022-09-29
# Runtime: 1966 ms, Memory: 18.4 MB
# Submission Id: 811348724


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
        
        patterns = set()
        for word in words2:
            pattern = 1
            for ch in word:
                pattern *= prime[ord(ch) - 97]
            patterns.add(pattern)
        
        ans = []
        for word in words1:
            products = 1
            for ch in word:
                products *= prime[ord(ch)-97]
            for pattern in patterns:
                if products % pattern != 0:
                    break
            else:
                ans.append(word)
        
        return ans