# 3395 - Minimum Length of Anagram Concatenation
# Date: 2024-05-21
# Runtime: 161 ms, Memory: 17.6 MB
# Submission Id: 1263237740


class Solution:
    def minAnagramLength(self, s: str) -> int:
        
        n = len(s)
        counter = Counter(s)
        if len(counter) == 1:
            return 1

        curr = Counter()

        def check(i):
            for j in range(i+1, n, i+1):
                temp = Counter(s[j:j+i+1])
                if curr != temp:
                    return False
            return True

        for i in range(n):
            curr[s[i]] += 1
            if n % (i+1):
                continue
            if len(counter) != len(curr):
                continue

            possible = True
            for ch in counter:
                if counter[ch] % curr[ch] or counter[ch] // curr[ch] != n // (i+1):
                    possible = False
                    break

            if possible and check(i):
                return i+1
        return n