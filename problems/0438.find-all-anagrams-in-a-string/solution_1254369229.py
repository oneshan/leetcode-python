# 0438 - Find All Anagrams in a String
# Date: 2024-05-10
# Runtime: 104 ms, Memory: 17.8 MB
# Submission Id: 1254369229


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pattern = Counter(p)

        ans = []
        counter = defaultdict(int)
        left = 0
        for right, ch in enumerate(s):
            counter[ch] += 1
            if right - left + 1 > len(p):
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            if pattern == counter:
                ans.append(left)

        return ans