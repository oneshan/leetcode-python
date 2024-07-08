# 2292 - Counting Words With a Given Prefix
# Date: 2024-06-03
# Runtime: 100 ms, Memory: 18 MB
# Submission Id: 1275857975


class TrieNode:
    def __init__(self):
        self.child = {}
        self.count = 0

class TrieTree:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.child:
                curr.child[ch] = TrieNode()
            curr = curr.child[ch]
            curr.count += 1

    def search(self, prefix):
        curr = self.root
        for ch in prefix:
            if ch not in curr.child:
                return 0
            curr = curr.child[ch]
        return curr.count

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        trie = TrieTree()
        for word in words:
            trie.insert(word)
        return trie.search(pref)