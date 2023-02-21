# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        stack = []
        for st in s:
            if st == ',':
                if stack and not isinstance(stack[-1], NestedInteger):
                    val = NestedInteger(int(stack.pop()))
                    stack.append(val)
            elif st.isnumeric() or st == '-':
                if stack and not isinstance(stack[-1], NestedInteger) and (stack[-1][0] == '-' or stack[-1].isnumeric() ):
                    stack[-1] += st
                else:
                    stack.append(st)
            elif st == ']':
                if stack and not isinstance(stack[-1], NestedInteger) and stack[-1] != '[':
                    stack.append(NestedInteger(int(stack.pop())))
                value , poped, arr = NestedInteger(), stack.pop(), []
                while stack and poped != "[":
                    arr.append(poped)
                    poped = stack.pop()
                while arr:
                    value.add(arr.pop())
                stack.append(value)
            else:
                stack.append(st)
        if stack and not isinstance(stack[-1], NestedInteger):
            stack.append(NestedInteger(int(stack.pop())))
        return stack.pop()
                    
        