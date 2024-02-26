# 0139 - Word Break
# Date: 2024-02-12
# Runtime: 40 ms, Memory: 17.6 MB
# Submission Id: 1172721525


class Trie:
    def __init__(self):
        self.child = {}
        self.is_word = False

class TrieTree:
    def __init__(self):
        self.root = Trie()
    
    def add(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.child:
                curr.child[ch] = Trie()
            curr = curr.child[ch]
        curr.is_word = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        tree = TrieTree()
        for word in wordDict:
            tree.add(word)
        
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(n):
            if not dp[i]:
                continue
            curr = tree.root
            for j in range(i, n):
                ch = s[j]
                if ch not in curr.child:
                    break
                curr = curr.child[ch]
                if curr.is_word:
                    dp[j+1] = True
        return dp[-1]