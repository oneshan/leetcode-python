# 2884 - Length of the Longest Valid Substring
# Date: 2024-06-01
# Runtime: 2569 ms, Memory: 226 MB
# Submission Id: 1273510957


class TrieNode:
    def __init__(self):
        self.child = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.child:
                curr.child[ch] = TrieNode()
            curr = curr.child[ch]
        curr.is_word = True
        curr.word_len = len(word)


class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        
        trie = Trie()
        for pattern in forbidden:
            trie.insert(pattern)

        ans = left = 0
        curr_tries = [trie.root]
        for right, ch in enumerate(word):
            next_tries = [trie.root]
            for node in curr_tries:
                if ch in node.child:
                    if node.child[ch].is_word:
                        left = max(left, right-node.child[ch].word_len+2)
                    else:
                        next_tries.append(node.child[ch])
            curr_tries = next_tries
            ans = max(ans, right - left+1)
        return ans
