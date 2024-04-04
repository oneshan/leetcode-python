# 3376 - Longest Common Suffix Queries
# Date: 2024-03-24
# Runtime: 1719 ms, Memory: 183.8 MB
# Submission Id: 1212198301


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
        min_len, min_idx = len(wordsContainer[0]), 0
        for idx, word in enumerate(wordsContainer):
            tree.insert(word, idx)
            if len(word) < min_len:
                min_len, min_idx = len(word), idx

        ans = []
        for suffix in wordsQuery:
            idx = tree.search(suffix)
            if idx == -1:
                ans.append(min_idx)
            else:
                ans.append(idx)
        return ans