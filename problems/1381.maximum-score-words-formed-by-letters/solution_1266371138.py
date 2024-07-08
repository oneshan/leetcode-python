# 1381 - Maximum Score Words Formed by Letters
# Date: 2024-05-24
# Runtime: 48 ms, Memory: 16.7 MB
# Submission Id: 1266371138


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        counter = Counter(letters)

        n = len(words)
        word_score = []
        word_count = []
        for word in words:
            word_count.append(Counter(word))
            word_score.append(sum(score[ord(ch)-ord('a')] for ch in word))
        
        self.ans = 0

        def is_valid(i, curr_used):
            for ch in word_count[i]:
                if curr_used[ch] + word_count[i][ch] > counter[ch]:
                    return False
            return True

        def backtrack(i, curr_used, curr_score):
            self.ans = max(self.ans, curr_score)
            for j in range(i, n):
                if is_valid(j, curr_used):
                    curr_used += word_count[j]
                    backtrack(j+1, curr_used, curr_score + word_score[j])
                    curr_used -= word_count[j]

        backtrack(0, Counter(), 0)
        return self.ans