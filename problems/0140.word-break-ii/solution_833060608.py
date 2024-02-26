# 0140 - Word Break II
# Date: 2022-10-30
# Runtime: 42 ms, Memory: 14 MB
# Submission Id: 833060608


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = ''

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
        node.word = word
    
    def get_sentences(self, s):
        n = len(s)
        ans = []
        def backtrack(i, words):
            if i == n:
                ans.append(' '.join(words))
                return
            
            node = self.root
            for j in range(i, n):
                if s[j] not in node.children:
                    break
                node = node.children[s[j]]
                if node.is_word:
                    words.append(node.word)
                    backtrack(j+1, words)
                    words.pop()

        backtrack(0, [])
        return ans
        
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        tree = Trie()
        for word in wordDict:
            tree.insert(word)
        return tree.get_sentences(s)