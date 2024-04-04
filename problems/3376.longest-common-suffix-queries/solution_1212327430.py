# 3376 - Longest Common Suffix Queries
# Date: 2024-03-24
# Runtime: 1692 ms, Memory: 183.8 MB
# Submission Id: 1212327430


class TrieNode:
    def __init__(self):
        self.children = {}
        self.min_len = float('inf')
        self.idx = -1

class TrieTree:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, idx):        
        curr = self.root
        if curr.min_len > len(word):
            curr.min_len = len(word)
            curr.idx = idx

        for ch in word[::-1]:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
            if curr.min_len > len(word):
                curr.min_len = len(word)
                curr.idx = idx
    
    def search(self, word):
        curr = self.root
        for ch in word[::-1]:
            if ch not in curr.children:
                return curr.idx
            curr = curr.children[ch]
        return curr.idx
    
    
class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        tree = TrieTree()
        for idx, word in enumerate(wordsContainer):
            tree.insert(word, idx)

        return [tree.search(word) for word in wordsQuery]