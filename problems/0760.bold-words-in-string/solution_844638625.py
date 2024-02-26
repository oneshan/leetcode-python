# 0760 - Bold Words in String
# Date: 2022-11-16
# Runtime: 114 ms, Memory: 14.4 MB
# Submission Id: 844638625


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.length = 0
        
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
        node.length = len(word)


class Solution:
    def boldWords(self, words: List[str], s: str) -> str:
        intervals = []
        
        # create trie tree
        tree = Trie()
        for word in words:
            tree.insert(word)
        
        # find intervals
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