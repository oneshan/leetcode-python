# 1949 - Implement Trie II (Prefix Tree)
# Date: 2022-10-08
# Runtime: 433 ms, Memory: 28.6 MB
# Submission Id: 817942040


class TrieNode:
    def __init__(self):
        self.prefix = 0
        self.word = 0
        self.children = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
            curr.prefix += 1
        curr.word += 1

    def countWordsEqualTo(self, word: str) -> int:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return 0
            curr = curr.children[ch]
            if curr.prefix == 0:
                return 0
        return curr.word
            
    def countWordsStartingWith(self, prefix: str) -> int:
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return 0
            curr = curr.children[ch]
            if curr.prefix == 0:
                return 0
        return curr.prefix

    def erase(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return
            curr = curr.children[ch]
            curr.prefix -= 1
        curr.word -= 1


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)