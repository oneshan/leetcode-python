# 0140 - Word Break II
# Date: 2022-10-30
# Runtime: 46 ms, Memory: 14.1 MB
# Submission Id: 833026680


from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}
        self.len = 0

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
        node.len = len(word)
        
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        tree = Trie()
        for word in wordDict:
            tree.insert(word)
            
        table = defaultdict(set)
        tries = set([tree.root])
        for idx, ch in enumerate(s):
            next_tries = set()
            for node in tries:
                if ch not in node.children:
                    continue
                next_tries.add(node.children[ch])
                if node.children[ch].is_word:
                    next_tries.add(tree.root)
                    table[idx+1].add(idx+1-node.children[ch].len)
            if not next_tries:
                return []
            tries = next_tries
        
        ans = []
        stack = [[len(s), []]]
        while stack:
            idx, words = stack.pop()
            if idx == 0:
                ans.append(' '.join(words))
            for prev_idx in table[idx]:
                stack.append([prev_idx, [s[prev_idx:idx]]+words])
        return ans