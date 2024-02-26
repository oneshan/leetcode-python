# 0341 - Flatten Nested List Iterator
# Date: 2023-10-20
# Runtime: 69 ms, Memory: 19.9 MB
# Submission Id: 1079945623


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
        self.stack = [[nestedList, 0]]

    def next(self) -> int:
        elem, idx = self.stack[-1]
        self.stack[-1][1] += 1
        return elem[idx].getInteger()
    
    def hasNext(self) -> bool:
        while self.stack:
            elem, idx = self.stack[-1]
            if len(elem) == idx:
                self.stack.pop()
                continue
            if elem[idx].isInteger():
                break
            
            self.stack[-1][1] += 1
            self.stack.append([elem[idx].getList(), 0])

        return len(self.stack) > 0
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())