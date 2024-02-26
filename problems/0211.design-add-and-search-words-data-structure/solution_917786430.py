# 0211 - Design Add and Search Words Data Structure
# Date: 2023-03-19
# Runtime: 5049 ms, Memory: 78.1 MB
# Submission Id: 917786430


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_word = True

    def search(self, word: str) -> bool:
        curr_list = [self.root]
        for ch in word:
            next_curr_list = []
            for curr in curr_list:
                if ch == '.':
                    next_curr_list += curr.children.values()
                elif ch in curr.children:
                    next_curr_list.append(curr.children[ch])
            if not next_curr_list:
                return False
            curr_list = next_curr_list
        return any(curr.is_word for curr in curr_list)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)