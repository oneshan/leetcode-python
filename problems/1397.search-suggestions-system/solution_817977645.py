# 1397 - Search Suggestions System
# Date: 2022-10-09
# Runtime: 432 ms, Memory: 21 MB
# Submission Id: 817977645


class TrieNode:
    def __init__(self):
        self.candidates = []
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
            if curr.count < 3:
                curr.candidates.append(word)
                curr.count += 1
            
    def search(self, word):
        curr = self.root
        ans = [[] for _ in range(len(word))]
        for idx, ch in enumerate(word):
            if ch not in curr.children:
                break
            curr = curr.children[ch]
            ans[idx] = curr.candidates
        return ans
    
        
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in sorted(products):
            trie.insert(product)
        return trie.search(searchWord) 
        
