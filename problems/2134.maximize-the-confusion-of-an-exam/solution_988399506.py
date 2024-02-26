# 2134 - Maximize the Confusion of an Exam
# Date: 2023-07-07
# Runtime: 237 ms, Memory: 16.7 MB
# Submission Id: 988399506


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ans = count_t = count_f = 0
        
        for idx in range(len(answerKey)):
            if answerKey[idx] == 'T':
                count_t += 1
            else:
                count_f += 1
            
            if min(count_t, count_f) <= k:
                ans += 1
            elif answerKey[idx - ans] == 'T':
                count_t -= 1
            else:
                count_f -= 1
        return ans
                