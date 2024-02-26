# 2755 - Extra Characters in a String
# Date: 2023-09-02
# Runtime: 186 ms, Memory: 17.3 MB
# Submission Id: 1038238750


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
        
        dp = [0] * (n+1)
        dp[-1] = 0

        for i in range(n-1, -1, -1):
            dp[i] = 1 + dp[i+1]
            curr = trie.root
            for j in range(i, n):
                if s[j] not in curr.child:
                    break
                curr = curr.child[s[j]]
                if curr.is_word:
                    dp[i] = min(dp[i], dp[j+1])
            
        return dp[0]