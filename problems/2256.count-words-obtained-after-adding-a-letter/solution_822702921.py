# 2256 - Count Words Obtained After Adding a Letter
# Date: 2022-10-15
# Runtime: 3990 ms, Memory: 34.1 MB
# Submission Id: 822702921


class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        
        def encode(word):
            num = 0
            for ch in word:
                num |= (1 << (ord(ch)-97))
            return num
    
        table = set(encode(word) for word in startWords)
        
        ans = 0
        for word in targetWords:
            num = encode(word)
            for i in range(26):
                mask = 1 << i
                if num & mask and num ^ mask in table:
                    ans += 1
                    break
        return ans