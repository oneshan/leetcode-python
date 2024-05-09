# 0567 - Permutation in String
# Date: 2024-05-08
# Runtime: 108 ms, Memory: 16.7 MB
# Submission Id: 1252669267


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        n = len(s1)
        count1 = Counter(s1)
        count2 = Counter()

        for i in range(len(s2)):
            count2[s2[i]] += 1
            if i >= n:
                count2[s2[i-n]] -= 1
            if count1 == count2:
                return True
        return False