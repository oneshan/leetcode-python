# 0746 - Prefix and Suffix Search
# Date: 2024-06-20
# Runtime: 3426 ms, Memory: 154.3 MB
# Submission Id: 1294322354


class TrieNode:
    def __init__(self):
        self.child = {}
        self.max_idx = -1

class TrieTree:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, idx):
        curr = self.root
        for ch in word:
            if ch not in curr.child:
                curr.child[ch] = TrieNode()
            curr = curr.child[ch]
            curr.max_idx = idx

    def search(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.child:
                return -1
            curr = curr.child[ch]
        return curr.max_idx


class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = TrieTree()
        for i, word in enumerate(words):
            for j in range(len(word)):
                suff_prefix = f'{word[j:]}+{word}'
                self.trie.insert(suff_prefix, i)

    def f(self, pref: str, suff: str) -> int:
        word = f'{suff}+{pref}'
        return self.trie.search(word)      


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)