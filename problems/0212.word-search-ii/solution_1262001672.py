# 0212 - Word Search II
# Date: 2024-05-19
# Runtime: 653 ms, Memory: 19.9 MB
# Submission Id: 1262001672


class TrieNode:
    def __init__(self):
        self.child = {}
        self.count = 0
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.child:
                curr.child[ch] = TrieNode()
            curr = curr.child[ch]
            curr.count += 1
        curr.word = word

    def delete(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.child:
                break
            curr = curr.child[ch]
            curr.count -= 1
        curr.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        len_r, len_c = len(board), len(board[0])
        ans = []

        trie = Trie()
        for word in words:
            trie.insert(word)

        def backtrack(r, c, node):
            if not (0 <= r < len_r and 0 <= c < len_c):
                return
            if board[r][c] not in node.child:
                return

            node = node.child[board[r][c]]
            if node.count == 0:
                return
            if node.word:
                ans.append(node.word)
                trie.delete(node.word)

            origin = board[r][c]
            board[r][c] = '#'
            for nr, nc in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                backtrack(nr, nc, node)
            board[r][c] = origin


        for r in range(len_r):
            for c in range(len_c):
                backtrack(r, c, trie.root)

        return ans