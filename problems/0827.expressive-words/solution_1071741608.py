# 0827 - Expressive Words
# Date: 2023-10-10
# Runtime: 47 ms, Memory: 16.2 MB
# Submission Id: 1071741608


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        
        def group_str(s):
            res = []
            prev, count = None, 0
            for ch in s:
                if ch != prev:
                    res.append((ch, count))
                    prev, count = ch, 0
                count += 1
            res.append((ch, count))
            return res
        
        def is_strectchy(s1, s2):
            if len(s1) != len(s2):
                return False
            for (ch1, count1), (ch2, count2) in zip(s1, s2):
                if ch1 != ch2:
                    return False
                if count1 == count2:
                    continue
                if count1 < 3 or count2 > count1:
                    return False
            return True
        
        ans = 0
        s = group_str(s)
        for word in words:
            word = group_str(word)
            if is_strectchy(s, word):
                ans += 1
        return ans