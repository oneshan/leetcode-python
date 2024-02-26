# 0139 - Word Break
# Date: 2023-08-04
# Runtime: 34 ms, Memory: 17.9 MB
# Submission Id: 1011672095


class TrieNode:
    def __init__(self):
        self.is_word = False
        self.child = {}

class TrieTree:
    def __init__(self):
        self.root = TrieNode()
        
    def add(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.child:
                curr.child[ch] = TrieNode()
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
            for node in stack:
                if ch not in node.child:
                    continue
                tmp = node.child[ch]
                next_stack.add(tmp)
                if tmp.is_word:
                    next_stack.add(tree.root)
                
            if not next_stack:
                return False
            stack = next_stack
        return tree.root in stack