# 0139 - Word Break
# Date: 2024-05-25
# Runtime: 36 ms, Memory: 17.7 MB
# Submission Id: 1267201869


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
        dp = [False] * (1 + n)
        dp[0] = True

        for i in range(n):
            if not dp[i]:
                continue
            curr = trie.root
            for j in range(i, n):
                if s[j] not in curr.child:
                    break
                curr = curr.child[s[j]]
                if curr.is_word:
                    dp[j+1] |= True
        return dp[-1]