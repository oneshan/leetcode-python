# 0139 - Word Break
# Date: 2022-10-30
# Runtime: 38 ms, Memory: 15.4 MB
# Submission Id: 832780095


class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        tree = Trie()
        for word in wordDict:
            tree.insert(word)
           
        tries = set([tree.root])
        for ch in s:
            tries = {trie.children[ch] for trie in tries if ch in trie.children} 
            if any(trie.is_word for trie in tries):
                tries.add(tree.root)
        return any(trie.is_word for trie in tries)