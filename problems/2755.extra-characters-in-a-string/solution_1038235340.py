# 2755 - Extra Characters in a String
# Date: 2023-09-02
# Runtime: 232 ms, Memory: 20.3 MB
# Submission Id: 1038235340


class TrieNode:
    def __init__(self):
        self.child = {}
        self.is_word = False

class TrieTree:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.child:
                curr.child[ch] = TrieNode()
            curr = curr.child[ch]
        curr.is_word = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        trie = TrieTree()
        for word in dictionary:
            trie.insert(word)
        
        n = len(s)
        
        @cache
        def dp(i):
            if i == n:
                return 0
            result = 1 + dp(i+1)
            curr = trie.root
            while i < n and s[i] in curr.child:
                curr = curr.child[s[i]]
                if curr.is_word:
                    result = min(result, dp(i+1))
                i += 1
            return result
        
        return dp(0)