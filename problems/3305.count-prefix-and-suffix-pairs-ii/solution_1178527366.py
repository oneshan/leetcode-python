# 3305 - Count Prefix and Suffix Pairs II
# Date: 2024-02-18
# Runtime: 1465 ms, Memory: 209.7 MB
# Submission Id: 1178527366


class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        count = 0
        for (prefix, suffix) in zip(word, reversed(word)):
            if (prefix, suffix) not in curr.children:
                curr.children[(prefix, suffix)] = TrieNode()
            curr = curr.children[(prefix, suffix)]
            count += curr.count
        curr.count += 1
        return count

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        trie = Trie()
        ans = 0
        for word in words:
            ans += trie.insert(word)
        return ans