# 1381 - Maximum Score Words Formed by Letters
# Date: 2024-06-11
# Runtime: 46 ms, Memory: 16.7 MB
# Submission Id: 1284333465


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
            # skip
            res = backtrack(i+1, curr_used)
            # pick
            if is_valid(i, curr_used):
                curr_used += word_count[i]
                res = max(res, word_score[i] + backtrack(i+1, curr_used))
                curr_used -= word_count[i]

            return res

        return backtrack(0, Counter())