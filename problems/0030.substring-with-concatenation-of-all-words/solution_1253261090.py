# 0030 - Substring with Concatenation of All Words
# Date: 2024-05-09
# Runtime: 65 ms, Memory: 17.5 MB
# Submission Id: 1253261090


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        k = len(words)
        len_w = len(words[0])

        counter = Counter(words)
        ans = []
        size = k * len_w

        def search(left):
            right = left
            curr = {}
            while left + size <= n:
                word = s[right:right+len_w]
                right += len_w
                if word not in counter:
                    left = right
                    curr = {}
                    continue

                curr[word] = curr.get(word, 0) + 1
                while curr[word] > counter[word]:
                    curr[s[left:left+len_w]] -= 1
                    left += len_w
                if right - left == size:
                    ans.append(left)

        for i in range(len_w):
            search(i)
        return ans