class Solution:
    def isValid(self, s: str) -> bool:
        '''You use a stack when:
You need to remember items in order, 
but process them in reverse order.
You need to handle nested or matching relationships.
You need to undo or backtrack recent actions.'''
        # mapping={')':'(',']':'[','}':'{'}
        # stack=[]
        # for c in s:
        #     if c in "({[":
        #         stack.append(c)
        #     else:
        #         if not stack:
        #             return False
        #         elif stack[-1] != mapping[c]:
        #             return False
        #         stack.pop()
        # return len(stack)==0




























        stack=[]
        matching = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in matching:
                if not stack or stack[-1]!=matching[char]:
                    return False
                
                stack.pop()
                
            else:
                stack.append(char)

        return (len(stack)==0)



















