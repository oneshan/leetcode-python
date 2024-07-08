# 0139 - Word Break
# Date: 2024-05-25
# Runtime: 50 ms, Memory: 18.4 MB
# Submission Id: 1267200659


class TrieNode:
    def __init__(self):
        self.child = {}
        self.is_word = False
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.child:
                curr.child[ch] = TrieNode()
            curr = curr.child[ch]
        curr.is_word = True
        curr.word = word

    

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)

        n = len(s)

        @cache
        def dfs(i):
            if i == n:
                return True
            
            res = False
            curr = trie.root
            for j in range(i, n):
                if s[j] not in curr.child:
                    break
                curr = curr.child[s[j]]
                if curr.is_word:
                    res |= dfs(j+1)
            return res

        return dfs(0)