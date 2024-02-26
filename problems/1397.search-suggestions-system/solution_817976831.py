# 1397 - Search Suggestions System
# Date: 2022-10-09
# Runtime: 202 ms, Memory: 21.3 MB
# Submission Id: 817976831


class TrieNode:
    def __init__(self):
        self.candidates = []
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
            curr.candidates.append(word)
            
    def search(self, word):
        curr = self.root
        ans = [[] for _ in range(len(word))]
        for idx, ch in enumerate(word):
            if ch not in curr.children:
                break
            curr = curr.children[ch]
            ans[idx] = sorted(curr.candidates)[:3]
        return ans
    
        
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in products:
            trie.insert(product)
        return trie.search(searchWord) 
        
