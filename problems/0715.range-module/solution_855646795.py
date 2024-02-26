# 0715 - Range Module
# Date: 2022-12-07
# Runtime: 7087 ms, Memory: 31.8 MB
# Submission Id: 855646795


class Node:
    def __init__(self, lx, rx, cover=False):
        self.start = lx
        self.end = rx
        self.left = None
        self.right = None
        self.cover = cover
    
    
class RangeModule:

    def __init__(self):
        self.root = Node(1, 1_000_000_000)

    def _update(self, node, val, query_s, query_e):
        # Non overlap
        if query_e < node.start or query_s > node.end:
            return
        
        # Full overlap
        if query_s <= node.start and node.end <= query_e:
            node.cover = val
            node.left = node.right = None
            return
        
        # Partial overlap
        if not node.left:
            mid = (node.start + node.end) // 2
            node.left = Node(node.start, mid, node.cover)
            node.right = Node(mid+1, node.end, node.cover)
        self._update(node.left, val, query_s, query_e)
        self._update(node.right, val, query_s, query_e)
        node.cover = node.left.cover and node.right.cover

    def _query(self, node, left, right):
        if right < node.start or node.end < left:
            return True
        if not node.left or (left <= node.start and node.end <= right):
            return node.cover
        return self._query(node.left, left, right) and self._query(node.right, left, right)
        
    def addRange(self, left: int, right: int) -> None:
        self._update(self.root, True, left, right-1)

    def queryRange(self, left: int, right: int) -> bool:
        return self._query(self.root, left, right-1)
    
    def removeRange(self, left: int, right: int) -> None:
        self._update(self.root, False, left, right-1)        


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)