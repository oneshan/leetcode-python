# 0341 - Flatten Nested List Iterator
# Date: 2024-06-09
# Runtime: 50 ms, Memory: 19.1 MB
# Submission Id: 1282622333


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [[0, nestedList]]

    def next(self) -> int:
        if not self.hasNext():
            return None
        
        idx, obj = self.stack[-1]
        self.stack[-1][0] += 1
        return obj[idx].getInteger()
    
    def hasNext(self) -> bool:
        while self.stack:
            idx, obj = self.stack[-1]
            if idx == len(obj):
                self.stack.pop()
                continue
            if obj[idx].isInteger():
                break
            self.stack[-1][0] += 1
            self.stack.append([0, obj[idx].getList()])

        return len(self.stack) > 0
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())