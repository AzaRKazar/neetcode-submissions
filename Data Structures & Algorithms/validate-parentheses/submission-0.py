class Solution:
    def isValid(self, s: str) -> bool:
        '''You use a stack when:
You need to remember items in order, 
but process them in reverse order.
You need to handle nested or matching relationships.
You need to undo or backtrack recent actions.'''
        mapping={')':'(',']':'[','}':'{'}
        stack=[]
        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                # if not stack:
                    # return False
                if stack[-1] != mapping[c]:
                    return False
                stack.pop()
        return len(stack)==0