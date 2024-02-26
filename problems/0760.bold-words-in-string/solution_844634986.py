# 0760 - Bold Words in String
# Date: 2022-11-16
# Runtime: 116 ms, Memory: 14.3 MB
# Submission Id: 844634986


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
        new_intervals = []
        for start, end in sorted(intervals):
            if new_intervals and new_intervals[-1][1] >= start:
                new_intervals[-1][1] = max(new_intervals[-1][1], end)
            else:
                new_intervals.append([start, end])
        
        # concat result
        ans, prev_end = [], 0
        for start, end in new_intervals:
            ans.extend([s[prev_end:start], '<b>', s[start:end],'</b>'])
            prev_end = end
        ans.append(s[prev_end:])
        return ''.join(ans)
