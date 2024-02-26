# 0212 - Word Search II
# Date: 2022-11-24
# Runtime: 881 ms, Memory: 18.7 MB
# Submission Id: 849106442


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
            stack.append((node, ch))
            node = node.child[ch]
        
        if node.child:
            node.is_word = False
            node.word = None
            return
        
        while stack:
            node, ch = stack.pop()
            del node.child[ch]
            if node.child or node.is_word:
                break
        
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        len_r, len_c = len(board), len(board[0])
        trie = Trie()
        for word in words:
            trie.insert(word)
                
        def backtrack(r, c, node):
            
            ch = board[r][c]
            node = node.child[ch]
            if node.is_word:
                ans.append(node.word)
                trie.remove(node.word)
            
            board[r][c] = '#'
            for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                if 0 <= r+dx < len_r and 0 <= c+dy < len_c and board[r+dx][c+dy] in node.child:
                    backtrack(r+dx, c+dy, node)
            board[r][c] = ch
        
        ans = []
        for r in range(len_r):
            for c in range(len_c):
                if board[r][c] in trie.root.child:
                    backtrack(r, c, trie.root)
        return ans