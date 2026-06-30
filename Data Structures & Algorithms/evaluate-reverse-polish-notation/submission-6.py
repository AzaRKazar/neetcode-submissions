class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operators={'+','-','/','*'}

        for char in tokens:
            if char not in operators:
                stack.append(int(char))
            else:
                a=int(stack.pop())
                b=int(stack.pop())

                if char=='+':
                    stack.append(a+b)
                elif char=='-':
                    stack.append(b-a)
                elif char=='*':
                    stack.append(a*b)
                elif char=='/':
                    stack.append(int(b/a))
            
        return stack[-1]
