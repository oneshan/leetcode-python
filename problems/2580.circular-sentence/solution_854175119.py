# 2580 - Circular Sentence
# Date: 2022-12-04
# Runtime: 37 ms, Memory: 13.9 MB
# Submission Id: 854175119


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        for i in range(len(words)-1):
            if words[i][-1] != words[i+1][0]:
                return False
        if words[0][0] != words[-1][-1]:
            return False
        return True