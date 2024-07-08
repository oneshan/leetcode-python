# 0140 - Word Break II
# Date: 2024-05-25
# Runtime: 39 ms, Memory: 16.5 MB
# Submission Id: 1267193484


class TrieNode:
    def __init__(self):
        self.child = {}
        self.word = None

class TrieTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.child:
                curr.child[ch] = TrieNode()
            curr = curr.child[ch]
        curr.word = word

    def get_sentence(self, s):
        n = len(s)
        res = []

        def backtrack(i, arr):
            curr = self.root
            if i == n:
                res.append(' '.join(arr))
                return
            for j in range(i, n):
                if s[j] not in curr.child:
                    break
                curr = curr.child[s[j]]
                if curr.word:
                    arr.append(curr.word)
                    backtrack(j+1, arr)
                    arr.pop()

        backtrack(0, [])
        return res

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = TrieTree()
        for word in wordDict:
            trie.insert(word)
        return trie.get_sentence(s)