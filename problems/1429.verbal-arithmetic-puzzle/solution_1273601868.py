# 1429 - Verbal Arithmetic Puzzle
# Date: 2024-06-01
# Runtime: 58 ms, Memory: 17.2 MB
# Submission Id: 1273601868


class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        max_len = 0
        non_zero_set = set()
        scale = defaultdict(int)

        for word in words:
            n = 1
            for i in range(len(word)-1, -1, -1):
                scale[word[i]] += n
                n *= 10
            if len(word) > 1:
                non_zero_set.add(word[0])
            max_len = max(max_len, len(word))

        if max_len > len(result) or max_len < len(result) - 1:
            return False

        n = 1
        for i in range(len(result)-1, -1, -1):
            scale[result[i]] -= n
            n *= 10
        if len(result) > 1:
            non_zero_set.add(result[0])

        chars = [ch for ch in scale if scale[ch] != 0] 
        chars = sorted(chars, key=lambda ch: abs(scale[ch]), reverse=True)

        @cache
        def bound(i, mask, is_pos):
            left, right, zero, res = 1, 9, -1, 0
            if mask & 1 == 0:
                for j in range(i, len(chars)):
                    if chars[j] in non_zero_set:
                        continue
                    if (scale[chars[j]] > 0) ^ is_pos:
                        zero = j
                        break
            
            for j in range(i, len(chars)):
                if j == zero:
                    continue
                if (scale[chars[j]] > 0) ^ is_pos:
                    while mask & (1 << left):
                        left += 1
                    res += scale[chars[j]] * left
                    left += 1
                else:
                    while mask & (1 << right):
                        right -= 1
                    res += scale[chars[j]] * right
                    right -= 1
            return res

        def dfs(i, mask, val):
            if val < bound(i, mask, False) or val > bound(i, mask, True):
                return False

            if i == len(chars):
                return True

            for d in range(10):
                if 1 << d & mask:
                    continue
                if d == 0 and chars[i] in non_zero_set:
                    continue
                if dfs(i+1, 1 << d | mask, val - d * scale[chars[i]]):
                    return True
            return False

        return dfs(0, 0, 0)