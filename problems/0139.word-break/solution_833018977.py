# 0139 - Word Break
# Date: 2022-10-30
# Runtime: 97 ms, Memory: 15.5 MB
# Submission Id: 833018977


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
            next_tries = set()
            for trie in tries:
                if ch not in trie.children:
                    continue
                node = trie.children[ch]
                next_tries.add(node)
                if node.is_word:
                    next_tries.add(tree.root)
            if not next_tries:
                return False
            tries = next_tries
        return tree.root in tries