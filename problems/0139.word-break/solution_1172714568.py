# 0139 - Word Break
# Date: 2024-02-12
# Runtime: 39 ms, Memory: 17.8 MB
# Submission Id: 1172714568


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
        
        stack = {tree.root}
        for ch in s:
            next_stack = set()
            for curr in stack:
                if ch in curr.child:
                    next_node = curr.child[ch]
                    if next_node.is_word:
                        next_stack.add(tree.root)
                    next_stack.add(next_node)
            if not next_stack:
                return False
            stack = next_stack
        return tree.root in stack