# 1112 - Find Words That Can Be Formed by Characters
# Date: 2023-12-02
# Runtime: 111 ms, Memory: 16.9 MB
# Submission Id: 1110659737


from collections import Counter, defaultdict

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter = Counter(chars)
        
        def is_good_str(word):
            count = defaultdict(int)
            for ch in word:
                count[ch] += 1
                if counter[ch] < count[ch]:
                    return False
            return True
        
        
        ans = 0
        for word in words:
            if is_good_str(word):
                ans += len(word)
        return ans