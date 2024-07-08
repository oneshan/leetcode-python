# 1381 - Maximum Score Words Formed by Letters
# Date: 2024-05-24
# Runtime: 302 ms, Memory: 16.6 MB
# Submission Id: 1266374447


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        counter = Counter(letters)

        n = len(words)
        word_score = []
        word_count = []
        for word in words:
            word_count.append(Counter(word))
            word_score.append(sum(score[ord(ch)-ord('a')] for ch in word))
        
        def is_valid(i, curr_used):
            for ch in word_count[i]:
                if curr_used[ch] + word_count[i][ch] > counter[ch]:
                    return False
            return True

        ans = 0
        for mask in range(1, 1 << n):
            curr_used = Counter()
            max_score = 0
            for i in range(n):
                if mask & (1 << i):
                    if not is_valid(i, curr_used):
                        break
                    curr_used += word_count[i]
                    max_score += word_score[i]
            else:
                ans = max(ans, max_score)

        return ans