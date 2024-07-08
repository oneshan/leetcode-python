# 0522 - Longest Uncommon Subsequence II
# Date: 2024-06-02
# Runtime: 38 ms, Memory: 16.4 MB
# Submission Id: 1275459731


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        counter = Counter(strs)
        candidates = [word for word in counter if counter[word] == 1]
        candidates.sort(key=len, reverse=True)

        def is_sub(s1, s2):
            i = 0
            for ch in s1:
                while i < len(s2) and ch != s2[i]:
                    i += 1
                if i == len(s2):
                    return False
                i += 1
            return True

        for s1 in candidates:
            for s2 in counter:
                if s1 == s2:
                    continue
                if is_sub(s1, s2):
                    break
            else:
                return len(s1)
        return -1