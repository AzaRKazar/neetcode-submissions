class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=len(s)
        #brute
        # s=s.lower()
        # output=""
        # for i in range(len(s)):
        #     if s[i].isalnum():
        #         output+=s[i]

        # if output==output[::-1]:
        #     return True
        
        # return False

        #optimal:
        # left=0
        # n=len(s)
        # right=n-1
        # while left<right:
        #     while left<right and not s[left].isalnum():
        #         left+=1
        #     while left<right and not s[right].isalnum():
        #         right-=1
        #     if s[left].lower()!=s[right].lower():
        #         return False
        #     left+=1
        #     right-=1
        # return True

