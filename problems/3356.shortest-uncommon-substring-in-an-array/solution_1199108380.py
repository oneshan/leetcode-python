# 3356 - Shortest Uncommon Substring in an Array
# Date: 2024-03-10
# Runtime: 630 ms, Memory: 19.9 MB
# Submission Id: 1199108380


class TrieNode:
    def __init__(self):
        self.children = {}
        self.set = set()

        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word, idx):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.set.add(idx)
        
    def search(self, word, idx):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return len(curr.set - {idx})
    
    
class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        trie = Trie()
        for i, word in enumerate(arr):
            for j in range(len(word)):
                for k in range(j+1, len(word)+1):
                    sub = word[j:k]
                    trie.insert(sub, i)
                        
        ans = []
        for i, word in enumerate(arr):
            shorest_sub = ''
            for j in range(len(word)):
                for k in range(j+1, len(word)+1):
                    sub = word[j:k]
                    if trie.search(sub, i):
                        continue
                    if not shorest_sub or len(sub) < len(shorest_sub) or (len(sub) == len(shorest_sub) and sub < shorest_sub):
                        shorest_sub = sub
            ans.append(shorest_sub)
        return ans