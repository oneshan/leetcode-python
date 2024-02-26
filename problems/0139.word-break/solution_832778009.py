# 0139 - Word Break
# Date: 2022-10-30
# Runtime: 91 ms, Memory: 15.7 MB
# Submission Id: 832778009


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
           
        stack = [-1]
        seen = {-1}
        while stack:
            i = stack.pop()
            if i == n-1:
                return True
            node = tree.root
            for j in range(i+1, n):
                if s[j] not in node.children:
                    break
                node = node.children[s[j]]
                if node.is_word and j not in seen:
                    stack.append(j)
                    seen.add(j)
        return False