# 0068 - Text Justification
# Date: 2023-08-24
# Runtime: 40 ms, Memory: 16.2 MB
# Submission Id: 1030218505


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        if not words:
            return []

        n, i = len(words), 0
        ans = []
        
        while i < n:
            
            # find start and end of word indexes
            j, curr_len = i, 0
            while j < n and curr_len + len(words[j]) <= maxWidth:
                curr_len += len(words[j]) + 1
                j += 1
            curr_len -= 1
            
            # left justified -- last line or one word
            if j == n or j == i+1:
                line = ' '.join(words[i:j]) + ' ' * (maxWidth - curr_len)
            # fully justified -- multi-words
            else:
                space_per_words, need_extra_space = divmod(maxWidth - curr_len, j - i - 1)
                line = [words[i]]
                spaces = ' ' * (space_per_words+1)
                need_extra_space += i
                for k in range(i+1, j):
                    if k <= need_extra_space:
                        line.append(' ')
                    line.append(spaces)
                    line.append(words[k])
                line = ''.join(line)

            ans.append(line)
            i = j

        return ans