# 2256 - Count Words Obtained After Adding a Letter
# Date: 2022-10-15
# Runtime: 3125 ms, Memory: 42 MB
# Submission Id: 822705389


class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        
        # O(S 26 log(26))
        sorted_s = set(''.join(sorted(list(word))) for word in startWords)

        # O(T 26 log(26))
        sorted_t = [sorted(list(word)) for word in targetWords]
        
        ans = 0
        
        # O(26T)
        for target in sorted_t:
            for i in range(len(target)):
                word = ''.join(target[:i] + target[i+1:])
                if word in sorted_s:
                    ans += 1
                    break
        
        return ans