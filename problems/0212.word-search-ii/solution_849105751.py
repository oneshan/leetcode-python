# 0212 - Word Search II
# Date: 2022-11-24
# Runtime: 979 ms, Memory: 18.7 MB
# Submission Id: 849105751


class TrieNode:
    def __init__(self):
        self.child = {}
        self.is_word = False
        self.word = None
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.child:
                node.child[ch] = TrieNode()
            node = node.child[ch]
        node.is_word = True
        node.word = word
    
    def remove(self, word):
        node = self.root
        stack = []
        for ch in word:
            node = node.child[ch]
        
        if node.child:
            node.is_word = False
            node.word = None
        
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        len_r, len_c = len(board), len(board[0])
        trie = Trie()
        for word in words:
            trie.insert(word)
                
        def backtrack(r, c, node):
            
            ch = board[r][c]
            curr_node = node.child[ch]
            if curr_node.is_word:
                ans.append(curr_node.word)
                trie.remove(curr_node.word)
            
            board[r][c] = '#'
            for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                if 0 <= r+dx < len_r and 0 <= c+dy < len_c and board[r+dx][c+dy] in curr_node.child:
                    backtrack(r+dx, c+dy, curr_node)
            board[r][c] = ch
            if not curr_node.child:
                node.child.pop(ch)
        
        ans = []
        for r in range(len_r):
            for c in range(len_c):
                if board[r][c] in trie.root.child:
                    backtrack(r, c, trie.root)
        return ans