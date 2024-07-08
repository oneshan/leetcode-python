# 0746 - Prefix and Suffix Search
# Date: 2024-06-20
# Runtime: 888 ms, Memory: 52 MB
# Submission Id: 1294329199


class WordFilter:

    def __init__(self, words: List[str]):
        self.prefix = defaultdict(set)
        self.suffix = defaultdict(set)
        self.index = {}

        for idx, word in enumerate(words):
            for i in range(len(word)):
                self.prefix[word[:i+1]].add(word)
                self.suffix[word[i:]].add(word)
            self.index[word] = idx

    def f(self, pref: str, suff: str) -> int:
        res = - 1
        for word in self.prefix[pref] & self.suffix[suff]:
            res = max(res, self.index[word])
        return res

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)