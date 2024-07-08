# 1381 - Maximum Score Words Formed by Letters
# Date: 2024-05-24
# Runtime: 40 ms, Memory: 16.7 MB
# Submission Id: 1266699207


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

        def backtrack(i, curr_used):
            if i == n:
                return 0
            res = backtrack(i+1, curr_used)
            if is_valid(i, curr_used):
                for ch in word_count[i]:
                    curr_used[ch] += word_count[i][ch]
                res = max(res, word_score[i] + backtrack(i+1, curr_used))
                for ch in word_count[i]:
                    curr_used[ch] -= word_count[i][ch]

            return res

        return backtrack(0, Counter())