# 3329 - Find the Length of the Longest Common Prefix
# Date: 2024-02-18
# Runtime: 912 ms, Memory: 32.3 MB
# Submission Id: 1178449142


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_word = True

    def search(self, word):
        curr = self.root
        count = 0
        for ch in word:
            if ch not in curr.children:
                break
            curr = curr.children[ch]
            count += 1
        return count

    
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie()
        for num in arr1:
            trie.insert(str(num))
        
        ans = 0
        for num in arr2:
            count = trie.search(str(num))
            ans = max(ans, count)
        return ans