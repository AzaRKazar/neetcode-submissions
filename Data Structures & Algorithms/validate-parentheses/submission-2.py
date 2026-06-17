class Solution:
    def isValid(self, s: str) -> bool:
        '''You use a stack when:
You need to remember items in order, 
but process them in reverse order.
You need to handle nested or matching relationships.
You need to undo or backtrack recent actions.'''
        mapping={')':'(',']':'[','}':'{'}
        stack=[]
        for char in s:
            if char in "[({":
                stack.append(char)
            else:
                if stack[-1]!=mapping[char]:
                    return False
                stack.pop()
        return len(stack)==0