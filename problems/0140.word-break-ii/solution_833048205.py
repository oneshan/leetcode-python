# 0140 - Word Break II
# Date: 2022-10-30
# Runtime: 36 ms, Memory: 13.9 MB
# Submission Id: 833048205


from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

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
    
    def get_valid_sentences(self, s):
        n = len(s)
        ans = []
        def backtrack(i, words):
            node = self.root
            for j in range(i, n):
                if s[j] not in node.children:
                    break
                node = node.children[s[j]]
                if node.is_word:
                    words.append(s[i:j+1])
                    backtrack(j+1, words)
                    words.pop()
            else:
                if node.is_word:
                    ans.append(' '.join(words + [s[i:]]))

        backtrack(0, [])
        return ans
        
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        tree = Trie()
        for word in wordDict:
            tree.insert(word)
        return tree.get_valid_sentences(s)