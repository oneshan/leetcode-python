# 1381 - Maximum Score Words Formed by Letters
# Date: 2024-05-24
# Runtime: 52 ms, Memory: 16.6 MB
# Submission Id: 1266364922


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        counter = [0] * 26
        for ch in letters:
            counter[ord(ch) - ord('a')] += 1
        
        n = len(words)
        word_scores = {}
        word_idx = []
        for word in words:
            val = 0
            arr = [0] * 26
            for ch in word:
                key = ord(ch) - ord('a')
                arr[key] += 1    
                val += score[key]
            
            word_scores[tuple(arr)] = val
            word_idx.append(tuple(arr))

        self.ans = 0

        def is_valid(i, curr):
            arr = word_idx[i]
            for i in range(26):
                if curr[i] + arr[i] > counter[i]:
                    return False
            return True

        def backtrack(i, curr_used, curr_score):
            self.ans = max(self.ans, curr_score)
            for j in range(i, n):
                if is_valid(j, curr_used):
                    arr = word_idx[j]
                    for k in range(26):
                        curr_used[k] += arr[k]
                    backtrack(j+1, curr_used, curr_score + word_scores[word_idx[j]])
                    for k in range(26):
                        curr_used[k] -= arr[k]

        backtrack(0, [0] * 26, 0)
        return self.ans