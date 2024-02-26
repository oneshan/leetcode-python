# 0616 - Add Bold Tag in String
# Date: 2023-10-28
# Runtime: 278 ms, Memory: 29.3 MB
# Submission Id: 1085835795


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.length = 0
    
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
        curr.length = len(word)    
    
class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        n = len(s)
        bold = [False] * n
        
        tree = Trie()
        for word in words:
            tree.insert(word)
        
        # find intervals
        intervals = []
        tries = set([tree.root])
        for idx, ch in enumerate(s, 1):
            tries = {trie.children[ch] for trie in tries if ch in trie.children}
            for trie in tries:
                if trie.is_word:
                    intervals.append([idx-trie.length, idx])
            tries.add(tree.root)
        
        # merge intervals
        merged_intervals = []
        for start, end in sorted(intervals):
            if merged_intervals and merged_intervals[-1][1] >= start:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], end)
            else:
                merged_intervals.append([start, end])
        
        # concat result
        ans, prev_end = [], 0
        for start, end in merged_intervals:
            ans.append(s[prev_end:start])
            ans.append(f'<b>{s[start:end]}</b>')
            prev_end = end
        ans.append(s[prev_end:])
        return ''.join(ans)    