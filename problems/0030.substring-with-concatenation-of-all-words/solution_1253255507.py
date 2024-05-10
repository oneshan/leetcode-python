# 0030 - Substring with Concatenation of All Words
# Date: 2024-05-09
# Runtime: 75 ms, Memory: 17.3 MB
# Submission Id: 1253255507


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        k = len(words)
        len_w = len(words[0])

        counter = Counter(words)
        ans = []
        size = k * len_w

        def search(left):
            curr = defaultdict(int)

            for right in range(left, n, len_w):

                sub = s[right:right+len_w]
                curr[sub] += 1

                if right - left == size:
                    prev_sub = s[left:left+len_w]
                    curr[prev_sub] -= 1
                    left += len_w
                    if curr[prev_sub] == 0:
                        del curr[prev_sub]

                if curr == counter:
                    ans.append(left)

        for i in range(len_w):
            search(i)
        return ans