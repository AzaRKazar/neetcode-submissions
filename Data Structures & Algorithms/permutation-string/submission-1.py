class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #brute
        # s1=sorted(s1)
        # for i in range(len(s2)):
        #     for j in range(i,len(s2)):
        #         s2_sub=s2[i:j+1]
        #         s2_sub=sorted(s2_sub)
        #         if s2_sub==s1:
        #             return True
        # return False
        


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #optimal
        #slding window
        # window=len(s1)
        # count_s1={}
        # left=0
        # count_s2={}
        # for char in s1:
        #     count_s1[char]=count_s1.get(char,0)+1
        # for right in range(len(s2)):
        #     count_s2[s2[right]]=count_s2.get(s2[right],0)+1

        #     if right -left+1>window:
        #         count_s2[s2[left]]-=1
        #         if count_s2[s2[left]]==0:
        #             del count_s2[s2[left]]
        #         #or 
        #         # 
        #         left+=1
        #     if right-left+1==window:
        #         if count_s2==count_s1:
        #             return True
        # return False




        hm1={}
        for i in s1:
            hm1[i]=hm1.get(i,0)+1
        
        hm2={}
        left=0
        for right in range(len(s2)):
            hm2[s2[right]]=hm2.get(s2[right],0)+1
            # count_s2[s2[right]]=count_s2.get(s2[right],0)+1

            if right-left+1>len(s1):
                hm2[s2[left]]-=1
                if hm2[s2[left]]==0:
                    del hm2[s2[left]]
                left+=1

            if right-left+1==len(s1):
                if len(s2)==len(s1):
                    return True 
        return False





















            
        

        